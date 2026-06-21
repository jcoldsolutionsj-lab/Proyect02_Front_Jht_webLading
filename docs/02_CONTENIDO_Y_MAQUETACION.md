# Especificaciones de Contenido y Maquetación - Landing Page y Web Oficial

## 1. Estructura General de la Página

La Landing Page debe tener las siguientes secciones, en este orden:

1.  **Header (Navegación)**
2.  **Hero (Portada)**
3.  **Widget de Seguimiento de Carga**
4.  **Nuestros Servicios** (Grid de cards con videos 1:1)
5.  **Nuestros Clientes Opinan** (Carrusel o Grid de logos)
6.  **Nuestra Flota** (Con Tabs: Liviana, Mediana, Pesada)
7.  **Testimonios** (Opcional, pero recomendado)
8.  **Contacto** (Formulario + Datos)
9.  **Footer**

---

## 2. Contenido por Sección

### 2.1 Header (NAV)
- **Logo:** `assets/images/branding/JHTmarca-transparente.png` (formato PNG con fondo transparente).
- **Comportamiento del logo:**
  - El logo es un enlace a la página de inicio (`/`).
  - Se mantiene visible y con su aspecto original al hacer scroll.
  - No cambia de color ni de versión, ya que al ser transparente se adapta visualmente tanto a fondos claros como oscuros.
- **Menú:** `Servicios | Flota | Clientes | Contacto | Área Cliente` (el último como botón destacado en `#FFD400`).
- **Comportamiento del nav:**
  - Estado inicial (scroll = 0): `background: transparent;`
  - Estado con scroll: `background: #1A3B6B; box-shadow: 0 4px 12px rgba(0,0,0,0.1);`
  - Transición: `transition: background 0.3s ease, box-shadow 0.3s ease;`
- **Responsive:** En móvil, el menú se colapsa en un botón hamburguesa (con Alpine.js) y el logo permanece visible.

### 2.2 Hero (Home)
- **Video de fondo (ancho completo):** `assets/videos/home/jhtOriginal.mp4` (20 segundos, `muted`, `playsinline`, `autoplay`, `loop`).
- **Video superpuesto (4:3):** `assets/videos/landing/Coordenadas_Continentes.mp4` (9 segundos, flotante, centrado, `muted`, `playsinline`).
- **Título principal:** `"Logística y Trazabilidad en Tiempo Real"`
- **Subtítulo:** `"Soluciones integrales de transporte para empresas que exigen precisión, seguridad y velocidad en su cadena de suministro."`
- **CTA Principal:** `"Conoce el estado de tu servicio"` (enlace a `/rastreo`).
- **Elementos decorativos:** Círculos abstractos en `#FFD400` y `#1A3B6B`.
- **Marcadores (IDs):**
  - `id="hero-titulo"`
  - `id="hero-subtitulo"`
  - `id="hero-cta"`

### 2.3 Widget de Seguimiento de Carga
- **Título:** `"Seguimiento de Carga"`
- **Estado (mockup):** `"En Tránsito"` con ícono de check.
- **Llegada estimada:** `"14:30 hrs"`.
- **Input:** `"Ingresa tu código de seguimiento"`.
- **Botón:** `"Consultar"` (en amarillo `#FFD400`).
- **Marcadores (IDs):**
  - `id="widget-titulo"`
  - `id="widget-estado"`
  - `id="widget-llegada"`
  - `id="widget-input"`
  - `id="widget-boton"`

### 2.4 Nuestros Servicios
- **Título:** `"Nuestros Servicios"`
- **Subtítulo:** `"Soluciones logísticas adaptadas a las necesidades específicas de tu negocio."`
- **Cards (4):**
  1.  **Transporte de Carga** | `"Movimiento seguro y eficiente de mercancías a nivel nacional."` | Ícono: `local_shipping` | **Video 1:1 (5-8s):** `assets/videos/flota/FlotaLiviana.mp4`
  2.  **Distribución** | `"Optimización de rutas para entregas capilares oportunas."` | Ícono: `route` | **Video 1:1 (5-8s):** `assets/videos/flota/FlotaMedia.mp4`
  3.  **Courier** | `"Servicio de mensajería rápida para documentos y paquetes pequeños."` | Ícono: `markunread_mailbox` | **Video 1:1 (5-8s):** `assets/videos/flota/FlotaPesada.mp4`
  4.  **Mudanzas** | `"Traslados corporativos y residenciales con embalaje especializado."` | Ícono: `home_work` | **Imagen estática:** `assets/images/servicios/Banner_Mudanza.webp`
- **Carrusel de 3 imágenes (en la sección):**
  - `assets/images/servicios/Banner_Almacenaje.webp`
  - `assets/images/servicios/Banner_CargaRefrigerada.webp`
  - `assets/images/servicios/Banner_Distribucion.webp`
- **Marcadores (IDs):**
  - `id="servicios-titulo"`
  - `id="servicios-subtitulo"`
  - `id="servicio-1-titulo"`, `id="servicio-1-desc"`, `id="servicio-1-video"`
  - `id="servicio-2-titulo"`, `id="servicio-2-desc"`, `id="servicio-2-video"`
  - `id="servicio-3-titulo"`, `id="servicio-3-desc"`, `id="servicio-3-video"`
  - `id="servicio-4-titulo"`, `id="servicio-4-desc"`, `id="servicio-4-imagen"`
  - `id="servicios-carrusel-1"`, `id="servicios-carrusel-2"`, `id="servicios-carrusel-3"`

### 2.5 Nuestros Clientes Opinan
- **Título:** `"Nuestros Clientes Opinan"`
- **Logos (referencias a archivos):**
  - `assets/images/clientes/logos_1_1/Alicorp.png`
  - `assets/images/clientes/logos_1_1/inkafarma.jpg`
  - `assets/images/clientes/logos_1_1/sewEurodrive.jpg`
  - `assets/images/clientes/logos_1_1/linde.png`
  - `assets/images/clientes/logos_1_1/Movitecnica.jpg`
  - `assets/images/clientes/logos_1_1/ibermatica.jpg`
  - `assets/images/clientes/logos_1_1/inkacrops.jpg`
  - `assets/images/clientes/logos_1_1/quimicaBrisas.gif`
  - `assets/images/clientes/logos_1_1/lubtec.jpg`
- **Formato:** Carrusel automático o grid responsive. Los logos deben tener el efecto de "reconocimiento" (grises → color al hover).
- **Marcadores (IDs):**
  - `id="clientes-titulo"`
  - `id="cliente-1"`, `id="cliente-2"`, ..., `id="cliente-9"`

### 2.6 Nuestra Flota (con Tabs)
- **Título:** `"Nuestra Flota"`
- **Subtítulo:** `"Vehículos modernos equipados con tecnología de rastreo satelital."`
- **Tabs:** `Liviana | Mediana | Pesada` (funcionales con Alpine.js).
- **Carrusel de 3 imágenes (en la sección):**
  - `assets/images/flota/banner_1.webp`
  - `assets/images/flota/banner_dia_2.webp`
  - `assets/images/flota/banner_noche_3.webp`
- **Contenido de cada tab:**

  **Tab 1: Liviana**
  - **Descripción:** `"Vehículo multiusos diseñado para operaciones logísticas urbanas y regionales."`
  - **Capacidad:** `1-5 Toneladas`
  - **Medidas:** `Largo 6m | Ancho 2m | Altura 2m`
  - **Video:** `assets/videos/flota/FlotaLiviana.mp4` (1:1, 5-8s, `muted`, `playsinline`)

  **Tab 2: Mediana**
  - **Descripción:** `"Flota profesional diseñada para operaciones logísticas de alto tonelaje."`
  - **Capacidad:** `10-15 Toneladas`
  - **Medidas:** `Largo 8m | Ancho 2.5m | Altura 2.5m`
  - **Video:** `assets/videos/flota/FlotaMedia.mp4` (1:1, 5-8s, `muted`, `playsinline`)

  **Tab 3: Pesada**
  - **Descripción:** `"Diseñado para el transporte eficiente de cargas medianas a pesadas."`
  - **Capacidad:** `25-28 Toneladas`
  - **Medidas:** `Largo 12.5m | Ancho 2.5m | Altura 2.7m`
  - **Video:** `assets/videos/flota/FlotaPesada.mp4` (1:1, 5-8s, `muted`, `playsinline`)
- **Marcadores (IDs):**
  - `id="flota-titulo"`
  - `id="flota-subtitulo"`
  - `id="flota-liviana-desc"`, `id="flota-liviana-capacidad"`, `id="flota-liviana-medidas"`, `id="flota-liviana-video"`
  - `id="flota-mediana-desc"`, `id="flota-mediana-capacidad"`, `id="flota-mediana-medidas"`, `id="flota-mediana-video"`
  - `id="flota-pesada-desc"`, `id="flota-pesada-capacidad"`, `id="flota-pesada-medidas"`, `id="flota-pesada-video"`
  - `id="flota-carrusel-1"`, `id="flota-carrusel-2"`, `id="flota-carrusel-3"`

### 2.7 Testimonios (Opcional)
- Si el espacio lo permite, incluir 2-3 testimonios de clientes reales con foto, nombre y cargo.
- **Marcadores (IDs):**
  - `id="testimonios-titulo"`
  - `id="testimonio-1"`, `id="testimonio-2"`, `id="testimonio-3"`

### 2.8 Contacto
- **Título:** `"¿Listo para optimizar tu logística?"`
- **Subtítulo:** `"Contáctanos y descubre cómo podemos ayudarte."`
- **Carrusel de 3 imágenes (en la sección):**
  - `assets/images/contacto/banner_dia_2.webp`
  - `assets/images/contacto/banner_dia_cola_3.webp`
  - `assets/images/contacto/banner_noche_1.webp`
- **Formulario:** Campos para `Nombre`, `Email`, `Teléfono`, `Mensaje`.
- **Botón:** `"Enviar mensaje"` (en amarillo `#FFD400`).
- **Datos de contacto:**
  - **Teléfono:** `(+51) 935 833 467`
  - **Email:** `info@jhttransport.com`
  - **Dirección:** `Santa Anita, Lima - Perú`
- **Mapa:** Google Maps embebido (opcional).
- **Marcadores (IDs):**
  - `id="contacto-titulo"`
  - `id="contacto-subtitulo"`
  - `id="contacto-telefono"`
  - `id="contacto-email"`
  - `id="contacto-direccion"`
  - `id="contacto-carrusel-1"`, `id="contacto-carrusel-2"`, `id="contacto-carrusel-3"`

### 2.9 Footer
- **Logo:** `assets/images/branding/JHTmarca-transparente.png`.
- **Enlaces rápidos:** `Inicio | Servicios | Flota | Contacto`.
- **Datos de contacto:** Teléfono, Email, Dirección.
- **Redes sociales:** Íconos de LinkedIn, Facebook, etc. (si aplica).
- **Copyright:** `© 2025 JHT Transport Company SAC. Todos los derechos reservados.`
- **Marcadores (IDs):**
  - `id="footer-logo"`
  - `id="footer-copyright"`

---

## 3. Videos 1:1 en Tarjetas (por sección)

| Sección | Ubicación | Videos 1:1 (5-8s) | Cantidad |
| :--- | :--- | :--- | :--- |
| **Home** | Tarjetas destacadas | `videos/flota/FlotaLiviana.mp4`, `videos/flota/FlotaMedia.mp4` | 2 |
| **Landing Page** | Tarjetas de servicios | `videos/flota/FlotaPesada.mp4`, `videos/landing/CoberturaMapa_LandingPage.mp4` | 2 |
| **Servicios** | Cards de servicios | `videos/flota/FlotaLiviana.mp4`, `videos/flota/FlotaMedia.mp4`, `videos/flota/FlotaPesada.mp4` | 3 |
| **Flota** | Tabs (cada tab) | `videos/flota/FlotaLiviana.mp4`, `videos/flota/FlotaMedia.mp4`, `videos/flota/FlotaPesada.mp4` | 3 (1 por tab) |
| **Nosotros** | Sección de valores | `videos/landing/Coordenadas_Continentes.mp4`, `videos/landing/CoberturaMapa_LandingPage.mp4` | 2 |
| **Contacto** | Sección de ubicación | `videos/landing/CoberturaMapa_LandingPage.mp4` | 1 |

**Nota:** Todos los videos deben tener los atributos `muted` y `playsinline` para reproducción automática sin audio.

---

## 4. Sistema de Marcadores (IDs) para Conexión con Django

Para facilitar la integración futura con Django, todos los elementos de contenido dinámico deben tener un `id` único y descriptivo. Los IDs deben seguir esta convención:

- **Secciones principales:** `id="[seccion]-titulo"`, `id="[seccion]-subtitulo"`
- **Elementos repetitivos:** `id="[seccion]-[numero]"` (ej. `cliente-1`, `servicio-2`)
- **Elementos multimedia:** `id="[seccion]-[tipo]-[numero]"` (ej. `flota-liviana-video`, `contacto-carrusel-1`)

**Nota:** Estos marcadores serán llenados por un script de JavaScript que, en el futuro, leerá los datos desde la API de Django.

---

## 5. Instrucciones para el Agente

Genera el código HTML para la Landing Page y la Página de Rastreo siguiendo esta estructura y contenido. Usa Tailwind CSS para los estilos y Alpine.js para las interacciones (tabs de flota, menú móvil). Asegúrate de que:

1. **Todos los textos y rutas de imágenes/videos** coincidan con lo especificado aquí.
2. **Los marcadores (`id`)** estén presentes para facilitar la conexión con Django.
3. **Todos los videos** tengan `muted` y `playsinline`.
4. **Los carruseles de 3 imágenes** estén implementados en las secciones: Servicios, Flota, Nosotros y Contacto.
5. **Los videos 1:1** estén integrados en las tarjetas según la tabla de la sección 3.
6. **La paleta de colores** use variables CSS o clases de Tailwind extendidas (no valores hex fijos).
7. **El código sea responsive** (Mobile First) y accesible.

---

**Entregable esperado:** Un proyecto frontend completo, con estructura de carpetas, archivos HTML, CSS y JS, listo para ejecutarse localmente y desplegarse en producción. El código debe ser limpio, comentado y escalable.