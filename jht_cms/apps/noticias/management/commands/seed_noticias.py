"""
Comando de Django para poblar la base de datos con los artículos
iniciales del módulo Noticias de JHT.

Uso:
    python manage.py seed_noticias
    python manage.py seed_noticias --flush   # Borra todo y vuelve a crear
"""
import shutil
from pathlib import Path
from datetime import datetime, timezone as dt_timezone

from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Carga los artículos iniciales de noticias en la base de datos y copia las imágenes a media/.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--flush',
            action='store_true',
            help='Elimina todos los datos existentes antes de crear los nuevos.',
        )

    def handle(self, *args, **options):
        # Importar modelos aquí para evitar problemas de importación temprana
        from apps.noticias.models import Categoria, Etiqueta, Autor, Articulo, ArticuloEtiqueta

        if options['flush']:
            self.stdout.write('[DEL]  Eliminando datos existentes...')
            ArticuloEtiqueta.objects.all().delete()
            Articulo.objects.all().delete()
            Autor.objects.all().delete()
            Etiqueta.objects.all().delete()
            Categoria.objects.all().delete()
            self.stdout.write(self.style.WARNING('   Datos eliminados.'))

        # ── Directorios de imágenes ─────────────────────────────────────
        # Las imágenes originales están en static_src (o static)
        static_img_dir = settings.BASE_DIR / 'static_src' / 'assets' / 'images' / 'noticias'
        if not static_img_dir.exists():
            static_img_dir = settings.BASE_DIR / 'static' / 'assets' / 'images' / 'noticias'

        media_portadas_dir = settings.MEDIA_ROOT / 'noticias' / 'portadas'
        media_portadas_dir.mkdir(parents=True, exist_ok=True)

        def copiar_imagen(nombre_archivo):
            """Copia imagen de static → media y retorna la ruta relativa para el modelo."""
            src = static_img_dir / nombre_archivo
            dst = media_portadas_dir / nombre_archivo
            if src.exists() and not dst.exists():
                shutil.copy2(src, dst)
            if dst.exists():
                return f'noticias/portadas/{nombre_archivo}'
            self.stdout.write(self.style.WARNING(f'   [!]  Imagen no encontrada: {nombre_archivo}'))
            return ''

        # ── 1. CATEGORÍAS ───────────────────────────────────────────────
        self.stdout.write('\n[DIR] Creando categorías...')
        cats_data = [
            ('Normativas MTC',  'normativas-mtc',  'bg-red-600 text-white'),
            ('Tecnología',      'tecnologia',       'bg-blue-600 text-white'),
            ('Transporte',      'transporte',       'bg-jht-dark text-jht-gold'),
            ('Sostenibilidad',  'sostenibilidad',   'bg-green-600 text-white'),
            ('Almacenaje',      'almacenaje',       'bg-purple-600 text-white'),
            ('Comercio',        'comercio',         'bg-orange-500 text-white'),
        ]
        categorias = {}
        for nombre, slug, color in cats_data:
            cat, created = Categoria.objects.get_or_create(
                slug=slug,
                defaults={'nombre': nombre, 'color_badge': color}
            )
            categorias[slug] = cat
            status = '[OK] Creado' if created else '[--]  Ya existe'
            self.stdout.write(f'   {status}: {nombre}')

        # ── 2. ETIQUETAS ────────────────────────────────────────────────
        self.stdout.write('\n[TAG]  Creando etiquetas...')
        etiquetas_nombres = [
            'MTC', 'GPS', 'BASC', 'SUNAT', 'GRE', 'Euro 6', 'IQBF',
            'Chancay', 'WMS', 'Aduana', 'IoT', 'Telemetría', 'B2B',
        ]
        etiquetas = {}
        for nombre in etiquetas_nombres:
            slug = slugify(nombre)
            et, created = Etiqueta.objects.get_or_create(
                slug=slug,
                defaults={'nombre': nombre}
            )
            etiquetas[slug] = et
            status = '[OK]' if created else '[--] '
            self.stdout.write(f'   {status} #{nombre}')

        # ── 3. AUTOR ────────────────────────────────────────────────────
        self.stdout.write('\n[USR] Creando autor...')
        autor, created = Autor.objects.get_or_create(
            nombre='Equipo de Ingeniería y Operaciones JHT',
            defaults={
                'cargo': 'Especialistas en Transporte y Logística',
                'bio': 'Especialistas en transporte de carga pesada, logística de materiales '
                       'peligrosos y normativas de comercio exterior en el Perú. Con más de '
                       '15 años de experiencia operando en los principales corredores logísticos del país.',
            }
        )
        self.stdout.write(f'   {"[OK] Creado" if created else "[--]  Ya existe"}: {autor.nombre}')

        # ── 4. ARTÍCULOS ────────────────────────────────────────────────
        self.stdout.write('\n[ART] Creando artículos...')

        articulos_data = [
            {
                'titulo':      'La Nueva Regulación de Carga Pesada Redefine las Rutas en Perú',
                'bajada':      'El diseño masivo de nuevos corredores logísticos y los tiempos de entrega '
                               'globales están obligando a las empresas a adaptarse rápidamente a las nuevas '
                               'normativas del Ministerio de Transportes y Comunicaciones (MTC).',
                'imagen':      'noticia_Semi-truck_passing_toll_booth_Peru_202607261810_11zon.webp',
                'categoria':   'normativas-mtc',
                'destacado':   True,
                'fecha':       datetime(2026, 10, 15, 10, 0, 0, tzinfo=dt_timezone.utc),
                'etiquetas':   ['mtc', 'basc'],
                'contenido':   """<h2>1. El impacto en las rutas troncales de carga pesada</h2>
<p>La nueva regulación establece horarios de tránsito restringidos para vehículos de configuración T3S3 y mayores en las principales vías de acceso a la capital y rutas interprovinciales. Esto significa que la planificación logística debe ser aún más precisa.</p>

<blockquote>
"La adaptabilidad operativa ya no es una ventaja competitiva opcional; es un requisito de supervivencia en el mercado actual de transporte de carga pesada."
<span class="block mt-3 text-xs font-bold uppercase tracking-wider text-jht-blue-support not-italic">— Gerencia de Operaciones, JHT Transport</span>
</blockquote>

<h2>2. Medidas de mitigación para flotas corporativas</h2>
<p>Para garantizar el flujo ininterrumpido de suministros B2B y evitar sanciones en ruta, nuestro equipo de ingeniería recomienda las siguientes acciones inmediatas:</p>

<ul>
<li><strong>Auditoría de pesos:</strong> Verificación de bonificaciones por eje neumático según normativa MTC vigente.</li>
<li><strong>Geocercas GPS:</strong> Alertas automáticas de desvío de ruta preaprobada con respuesta en menos de 2 minutos.</li>
<li><strong>Certificación BASC:</strong> Cero incidencias en seguridad patrimonial bajo estándares internacionales.</li>
</ul>

<h2>3. Impacto en costos operativos</h2>
<p>Las empresas que no se adapten a tiempo a las nuevas normativas podrían enfrentar multas de hasta 20 UIT por unidad vehicular. JHT Transport ha invertido en un sistema de auditoría preventiva que permite detectar incumplimientos antes de que ocurran en ruta.</p>

<p>Contamos con un equipo de 12 especialistas en normativa MTC que monitorean en tiempo real el estado de cada unidad, garantizando el cumplimiento al 100% de las disposiciones vigentes.</p>""",
            },
            {
                'titulo':    'Telemetría e IoT en Torres de Control 24/7',
                'bajada':    'Monitoreo satelital activo, alertas automáticas de desvío y reporte continuo '
                             'a la central de operaciones. Cómo la tecnología transforma la gestión de flotas pesadas.',
                'imagen':    'noticia_Logistics_control_tower_showing.webp',
                'categoria': 'tecnologia',
                'destacado': False,
                'fecha':     datetime(2026, 10, 12, 9, 0, 0, tzinfo=dt_timezone.utc),
                'etiquetas': ['gps', 'iot', 'telemetria'],
                'contenido': """<h2>La revolución de los datos en tiempo real</h2>
<p>Las torres de control inteligentes de JHT procesan más de 2 millones de puntos de datos diarios provenientes de nuestra flota de vehículos pesados. Esta infraestructura tecnológica nos permite anticipar incidencias antes de que ocurran.</p>

<h2>Sensores y conectividad de última generación</h2>
<p>Cada unidad de nuestra flota cuenta con sensores de temperatura, presión de neumáticos, nivel de combustible y detector de fatiga del conductor, transmitiendo datos cada 30 segundos mediante conexión satelital de banda Ka.</p>

<ul>
<li><strong>Tiempo de respuesta:</strong> Menos de 90 segundos ante cualquier alerta crítica</li>
<li><strong>Cobertura:</strong> 100% del territorio nacional, incluidas zonas sin señal celular</li>
<li><strong>Uptime:</strong> 99.97% de disponibilidad del sistema de monitoreo</li>
</ul>""",
            },
            {
                'titulo':    'Guías de Remisión Electrónicas GRE-SUNAT: Todo lo que debes saber',
                'bajada':    'Fiscalización digital en ruta: lo que todo generador de carga debe certificar '
                             'este año. Guía completa de implementación GRE según las disposiciones vigentes de SUNAT.',
                'imagen':    'noticia_Tablet_displaying_Guia_SUNAT_truck.webp',
                'categoria': 'normativas-mtc',
                'destacado': False,
                'fecha':     datetime(2026, 10, 8, 11, 0, 0, tzinfo=dt_timezone.utc),
                'etiquetas': ['sunat', 'gre', 'mtc'],
                'contenido': """<h2>¿Qué es la GRE y por qué es obligatoria?</h2>
<p>La Guía de Remisión Electrónica (GRE) reemplaza definitivamente a las guías físicas en papel. Desde el 1 de enero de 2024, todos los generadores de carga están obligados a emitir sus guías de forma electrónica a través del sistema SOL de SUNAT.</p>

<h2>Infracciones y sanciones vigentes</h2>
<p>Las fiscalizaciones en ruta se realizan mediante el sistema SISCO de SUNAT, que valida la GRE en tiempo real. Las infracciones pueden resultar en:</p>
<ul>
<li>Retención del vehículo hasta por 72 horas</li>
<li>Multa equivalente al 15% del valor de los bienes transportados</li>
<li>Comiso de los bienes en casos de reincidencia</li>
</ul>

<h2>¿Cómo JHT garantiza el cumplimiento?</h2>
<p>Nuestro sistema de coordinación de carga integra directamente con la API de SUNAT, generando automáticamente la GRE en el momento de la carga, antes de que la unidad salga del almacén del cliente.</p>""",
            },
            {
                'titulo':    'Eficiencia Energética y Flotas Euro 6: El Futuro del Transporte Sostenible',
                'bajada':    'Reducción de huella de carbono y optimización del consumo de combustible en '
                             'largas distancias. JHT lidera la transición hacia una flota más sostenible en Perú.',
                'imagen':    'flotas-euro6.webp',
                'categoria': 'sostenibilidad',
                'destacado': False,
                'fecha':     datetime(2026, 10, 5, 10, 0, 0, tzinfo=dt_timezone.utc),
                'etiquetas': ['euro-6', 'b2b'],
                'contenido': """<h2>La norma Euro 6 y su impacto en el transporte peruano</h2>
<p>Los motores Euro 6 representan una reducción del 95% en emisiones de óxidos de nitrógeno (NOx) y del 97% en partículas sólidas comparado con las generaciones anteriores. JHT ha completado la renovación del 60% de su flota con estas unidades.</p>

<h2>Beneficios operativos medibles</h2>
<ul>
<li><strong>Consumo de combustible:</strong> Reducción del 18% en consumo por tonelada-kilómetro</li>
<li><strong>Mantenimiento:</strong> Intervalos de servicio 40% más largos gracias a los sistemas SCR</li>
<li><strong>Disponibilidad:</strong> Mayor uptime operativo y menor tiempo en taller</li>
</ul>

<h2>Compromiso con el medio ambiente</h2>
<p>En 2025, JHT redujo su huella de carbono en 2,400 toneladas de CO2 equivalente gracias a la implementación de rutas optimizadas y la transición tecnológica de su flota. Para 2027, el objetivo es alcanzar el 100% de unidades Euro 6.</p>""",
            },
            {
                'titulo':    'El Impacto del Megapuerto de Chancay en la Logística Nacional',
                'bajada':    'Reorganización de corredores viales y nuevas oportunidades intermodales en Perú. '
                             'El Puerto de Chancay redefine la cadena de suministro del país.',
                'imagen':    'noticia_Aerial_view_Chancay_Megaport_trucks_202607261809_11zon.webp',
                'categoria': 'transporte',
                'destacado': False,
                'fecha':     datetime(2026, 9, 28, 10, 0, 0, tzinfo=dt_timezone.utc),
                'etiquetas': ['chancay', 'aduana', 'b2b'],
                'contenido': """<h2>Chancay: El hub logístico del Pacífico Sur</h2>
<p>El Megapuerto de Chancay, con una inversión de USD 3,600 millones, tiene capacidad para atender buques de hasta 18,000 TEUs y procesará inicialmente 1 millón de contenedores anuales. Esto posiciona a Perú como el principal hub logístico del Pacífico Sur.</p>

<h2>Nuevos corredores terrestres</h2>
<p>La apertura del puerto genera tres nuevos corredores de alto tráfico que impactan directamente las operaciones de transporte terrestre:</p>
<ul>
<li><strong>Corredor Centro:</strong> Chancay → Lima → La Oroya → Huancayo</li>
<li><strong>Corredor Norte:</strong> Chancay → Variante de Pasamayo → Ancón</li>
<li><strong>Corredor Sur:</strong> Chancay → Lima → Ica → Arequipa</li>
</ul>

<h2>Oportunidades para JHT</h2>
<p>JHT ha establecido alianzas estratégicas con 3 agencias de aduanas y 2 operadores portuarios de Chancay para ofrecer soluciones de transporte puerta-a-puerta integradas, desde el descargo del buque hasta el almacén del importador.</p>""",
            },
            {
                'titulo':    'Protocolos Avanzados de Seguridad para Transporte de Carga Crítica',
                'bajada':    'Implementación de certificaciones BASC, cumplimiento normativo SUCAMEC y '
                             'estándares globales en la gestión de insumos industriales y químicos (IQBF).',
                'imagen':    'noticia_Tanker_truck_driving_Andean_road_202607261809_11zon.webp',
                'categoria': 'transporte',
                'destacado': False,
                'fecha':     datetime(2026, 10, 8, 8, 0, 0, tzinfo=dt_timezone.utc),
                'etiquetas': ['basc', 'iqbf', 'mtc'],
                'contenido': """<h2>Certificación BASC: Seguridad en toda la cadena</h2>
<p>JHT Transport mantiene la certificación BASC (Business Anti Smuggling Coalition) que garantiza estándares internacionales de seguridad en toda la cadena logística. Esto incluye verificación de antecedentes del 100% del personal operativo y sistemas de control de acceso biométrico en todas nuestras instalaciones.</p>

<h2>Manejo de Insumos Químicos y Bienes Fiscalizados (IQBF)</h2>
<p>Contamos con autorización SUCAMEC para el transporte de insumos químicos fiscalizados, con conductores certificados y vehículos equipados con sistemas especiales de contención, sensores de detección de fugas y comunicación satelital dedicada para emergencias.</p>

<ul>
<li><strong>Tiempo de respuesta en emergencias:</strong> Menos de 15 minutos con coordinación SUCAMEC</li>
<li><strong>Cobertura de seguro especial:</strong> Hasta USD 5 millones por siniestro</li>
<li><strong>Rutas preaprobadas:</strong> Geocercas activas en todos los despachos IQBF</li>
</ul>""",
            },
            {
                'titulo':    'Garantía de Cadena de Frío en Distribución B2B',
                'bajada':    'Control de temperatura garantizado con sistemas de monitoreo continuo desde '
                             'la carga en planta hasta la entrega final en almacén destino.',
                'imagen':    'noticia_Refrigerated_truck_on_highway_2K_202607261809_11zon.webp',
                'categoria': 'sostenibilidad',
                'destacado': False,
                'fecha':     datetime(2026, 10, 5, 9, 0, 0, tzinfo=dt_timezone.utc),
                'etiquetas': ['b2b', 'telemetria'],
                'contenido': """<h2>¿Por qué la cadena de frío es crítica en el B2B?</h2>
<p>Productos farmacéuticos, alimentos procesados, químicos sensibles y componentes electrónicos requieren control de temperatura estricto durante todo el trayecto. Una ruptura en la cadena de frío puede significar pérdidas millonarias y responsabilidad legal para el transportista.</p>

<h2>Tecnología de monitoreo implementada</h2>
<p>Cada unidad refrigerada de JHT está equipada con sensores de temperatura IoT que registran y transmiten lecturas cada 5 minutos, con alertas automáticas cuando la temperatura se desvía ±0.5°C del rango programado.</p>

<ul>
<li><strong>Rango de temperatura:</strong> -25°C a +25°C según requerimiento del cliente</li>
<li><strong>Informe de temperatura:</strong> Reporte digital firmado digitalmente entregado con cada despacho</li>
<li><strong>Trazabilidad:</strong> Registro histórico de temperatura disponible por 5 años</li>
</ul>""",
            },
            {
                'titulo':    'Gestión de Inventarios y Almacenaje WMS: Eficiencia Operativa al Máximo',
                'bajada':    'Optimización del flujo de picking, cross-docking y trazabilidad de lotes para '
                             'operaciones corporativas. El WMS que transforma los almacenes en centros de eficiencia.',
                'imagen':    'noticia_Modern_logistics_warehouse_with_._202607261809.webp',
                'categoria': 'almacenaje',
                'destacado': False,
                'fecha':     datetime(2026, 10, 2, 10, 0, 0, tzinfo=dt_timezone.utc),
                'etiquetas': ['wms', 'b2b', 'iot'],
                'contenido': """<h2>¿Qué es un WMS y por qué lo necesitas?</h2>
<p>Un Warehouse Management System (WMS) es el cerebro digital de un centro de distribución. Controla en tiempo real la ubicación de cada SKU, optimiza las rutas de picking de los operarios y garantiza la trazabilidad completa de cada lote desde recepción hasta despacho.</p>

<h2>Funcionalidades implementadas por JHT</h2>
<ul>
<li><strong>Picking por voz y RFID:</strong> Reducción de errores de picking en 98%</li>
<li><strong>Cross-docking:</strong> Mercadería en tránsito con tiempo de estadía mínimo</li>
<li><strong>FIFO/FEFO automático:</strong> Control de vencimientos y rotación por lote</li>
<li><strong>Integración ERP:</strong> Sincronización bidireccional con SAP, Oracle y sistemas propios</li>
</ul>

<h2>Resultados medibles</h2>
<p>Los clientes que han migrado a nuestra plataforma WMS reportan una reducción promedio del 35% en costos de almacenaje y un incremento del 42% en la velocidad de procesamiento de órdenes.</p>""",
            },
            {
                'titulo':    'Comercio Exterior y Logística Internacional: Estrategias para Importadores',
                'bajada':    'Estrategias de agilidad aduanera y fletes terrestres intermodales para importadores '
                             'y exportadores. Cómo optimizar tu cadena de suministro internacional desde Perú.',
                'imagen':    'noticia_Gantry_cranes_unloading_containe._2K_202607261809.webp',
                'categoria': 'comercio',
                'destacado': False,
                'fecha':     datetime(2026, 9, 25, 10, 0, 0, tzinfo=dt_timezone.utc),
                'etiquetas': ['aduana', 'chancay', 'b2b'],
                'contenido': """<h2>El ecosistema del comercio exterior peruano</h2>
<p>Perú cuenta con 12 tratados de libre comercio activos que cubren el 95% de sus exportaciones. Sin embargo, la eficiencia logística sigue siendo el principal cuello de botella para competir en mercados internacionales.</p>

<h2>Soluciones intermodales JHT</h2>
<p>Ofrecemos servicios de transporte terrestre integrado con los principales operadores portuarios y aéreos del país, con despacho aduanero incluido y gestión de documentos de exportación/importación.</p>

<ul>
<li><strong>Tiempo de despacho aduanero:</strong> 24-48 horas en canales verde y naranja</li>
<li><strong>Cobertura de seguro internacional:</strong> Hasta USD 1 millón por embarque</li>
<li><strong>Agentes en destino:</strong> Red de corresponsales en 18 países</li>
</ul>

<h2>Optimización de incoterms</h2>
<p>Nuestro equipo de especialistas en comercio exterior asesora a cada cliente en la selección del incoterm más conveniente según el tipo de mercadería, destino y perfil de riesgo del negocio.</p>""",
            },
        ]

        for data in articulos_data:
            # Copiar imagen a media
            ruta_imagen = copiar_imagen(data['imagen'])

            # Crear o actualizar artículo
            slug = slugify(data['titulo'])
            articulo, created = Articulo.objects.get_or_create(
                slug=slug,
                defaults={
                    'titulo':             data['titulo'],
                    'bajada':             data['bajada'],
                    'contenido_html':     data['contenido'],
                    'categoria':          categorias[data['categoria']],
                    'autor':              autor,
                    'estado':             'publicado',
                    'es_destacado':       data['destacado'],
                    'fecha_publicacion':  data['fecha'],
                }
            )

            # Asignar imagen (solo si no tiene)
            if ruta_imagen and not articulo.imagen_portada:
                articulo.imagen_portada = ruta_imagen
                articulo.save()

            # Asignar etiquetas
            for et_slug in data.get('etiquetas', []):
                et = etiquetas.get(et_slug)
                if et:
                    ArticuloEtiqueta.objects.get_or_create(articulo=articulo, etiqueta=et)

            icono = '[OK]' if created else '[--] '
            estrella = ' [*] DESTACADO' if data['destacado'] else ''
            self.stdout.write(f'   {icono} {data["titulo"][:65]}{estrella}')

        # ── RESUMEN ─────────────────────────────────────────────────────
        self.stdout.write('\n' + '-' * 60)
        self.stdout.write(self.style.SUCCESS(
            f'[OK] Semilla completada:\n'
            f'   • {Categoria.objects.count()} categorías\n'
            f'   • {Etiqueta.objects.count()} etiquetas\n'
            f'   • {Autor.objects.count()} autores\n'
            f'   • {Articulo.objects.count()} artículos ({Articulo.objects.filter(estado="publicado").count()} publicados)\n'
            f'   • Imágenes copiadas a: {media_portadas_dir}\n'
            f'\n>>> Visita http://127.0.0.1:8001/noticias/ para ver el resultado.'
        ))
