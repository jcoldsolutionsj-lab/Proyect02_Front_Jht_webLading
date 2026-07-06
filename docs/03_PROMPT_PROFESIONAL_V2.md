# Directrices de Desarrollo - Prompt Profesional Landing Page JHT v2.0

Este documento contiene las reglas, arquitectura y especificaciones del Prompt Profesional v2.0 para garantizar consistencia en cada cambio realizado, enfocado en SEO técnico, Core Web Vitals, Accesibilidad WCAG 2.1 AA y preparación para sistemas empresariales.

---

## 1. Regla de Oro e Identidad Visual
* **No Rediseñar:** Respetar la arquitectura y diseño visual existente. Todo cambio debe ser una mejora técnica incremental sin romper la experiencia de usuario.
* **Colores Corporativos:**
  * **Primarios:** Azul JHT (`#1A3B6B`), Amarillo JHT (`#FFD400`)
  * **Secundarios:** Gris Claro (`#E3E4E5`), Azul Apoyo 1 (`#909AB3`), Azul Apoyo 2 (`#57678E`)
  * **Neutros:** Blanco (`#FFFFFF`), Gris Claro Base (`#F8F9FA`), Oscuro (`#212529`)
* **Tipografía:** Montserrat para títulos, Open Sans para textos de cuerpo.

---

## 2. Estructura de Navegación y Arquitectura de Secciones
El flujo de secciones de la Landing Page debe respetarse estrictamente en el siguiente orden:

1. **HEADER (Menú de Navegación):**
   * Logo transparente. Enlaces: *Inicio, Servicios, Flota, Nosotros, Contacto, Área Cliente*.
   * Sticky Nav (cambio de fondo transparente a azul sólido `#1A3B6B` al hacer scroll).
   * Menú móvil colapsable con Alpine.js.
2. **HERO (Portada Principal):**
   * Principal generador de conversiones y prospectos (leads).
   * **Contenido obligatorio:** H1 optimizado SEO, Subtítulo, Indicadores de Valor (Empresas, Envíos, Cobertura, GPS) y **Formulario de Cotización** (Servicio requerido, Nombre, Empresa, Correo, Celular, Botón de acción).
   * **PROHIBIDO:** No colocar módulo de rastreo en el Hero (este vivirá de forma independiente).
3. **SERVICIOS (Mudanzas, Carga Refrigerada, Almacenaje, Personal de Estiba, Courier, Distribución, Transporte de Carga):**
   * Mantener exactamente las **7 tarjetas de servicios** del catálogo.
   * Cada tarjeta debe tener: Imagen de cabecera, icono representativo, título (H3), descripción, listado de beneficios y botón interactivo que abra el modal dialog de detalles (`onclick="openModal(this)"`).
4. **FLOTA:**
   * Pestañas (Tabs) interactivas con Alpine.js: *Liviana, Mediana y Pesada*.
   * Muestra de especificaciones técnicas (Capacidad, medidas y cobertura) junto a sus respectivos videos y carruseles.
5. **POR QUÉ ELEGIRNOS / BENEFICIOS:**
   * Tarjetas informativas de propuesta de valor: *Entrega Puntual, Monitoreo GPS 24/7, Seguro de Carga y Cobertura Nacional*.
6. **CÓMO TRABAJAMOS:**
   * Proceso logístico en 4 pasos con iconografía: *1. Solicitud ➔ 2. Recojo ➔ 3. Seguimiento ➔ 4. Entrega*.
7. **SOBRE NOSOTROS:**
   * Historia, Misión, Visión, Valores e imágenes corporativas.
8. **EMPRESAS QUE CONFÍAN EN NOSOTROS:**
   * Sección elegante con carrusel automático de logotipos (escala de grises a color al hover), ubicada inmediatamente después de *Sobre Nosotros*.
9. **COBERTURA NACIONAL:**
   * Mapa interactivo/estático, descripción y listado estructurado de ciudades principales de cobertura.
10. **TESTIMONIOS:**
    * Carrusel con valoraciones de 5 estrellas (★★★★★), comentarios de clientes reales, logos de empresas y cargos de los representantes.
11. **PREGUNTAS FRECUENTES (FAQ):**
    * Acordeón interactivo desarrollado con Alpine.js que contiene al menos **8 preguntas clave** optimizadas para SEO semántico y búsquedas web.
12. **CTA FINAL (Banner de Acción):**
    * Mensaje comercial de alto impacto con dos CTAs claros: *Solicitar Cotización* (scroll al Hero/formulario) y *Hablar con un Asesor* (enlace directo a WhatsApp).
13. **CONTACTO:**
    * Sección de cierre con Formulario Completo de consultas, mapa embebido de Google Maps, dirección física, horarios de atención, teléfonos y enlaces a WhatsApp y correo.
14. **FOOTER:**
    * Logo corporativo, enlaces rápidos de navegación, enlaces legales, redes sociales oficiales y copyright.

---

## 3. SEO Técnico y Semántico
* **Jerarquía de Encabezados:** Exactamente un único `H1` por página. Utilizar `H2` para los títulos de cada sección y `H3` para los títulos de tarjetas y elementos repetitivos.
* **Palabra Clave Principal:** *"Transporte de carga"*, integrada de manera natural (con una densidad recomendada de 1%-2%) en el H1, metas, primer párrafo, Sobre Nosotros y Footer, evitando malas prácticas de sobreoptimización (*keyword stuffing*).
* **Metaetiquetas SEO y Metadata:** Integración obligatoria de title descriptivo, meta description llamativa, etiquetas canonical, robots index, etiquetas Open Graph (OG) y Twitter Cards.
* **Datos Estructurados JSON-LD:** Configurar y validar esquemas semánticos estructurados para buscadores (`Organization`, `LocalBusiness`, `WebSite`, `Service`, `FAQPage`, `BreadcrumbList`, `ContactPoint`).

---

## 4. Rendimiento (Core Web Vitals) y Accesibilidad (WCAG 2.1 AA)
* **Atributos Multimedia de Rendimiento:** Usar `loading="lazy"` y `decoding="async"` para todas las imágenes y videos fuera del primer viewport. Agregar enlaces de preconexión (`preconnect`) a fuentes externas.
* **Animaciones Seguras (Evitar Layout Shift):** Las animaciones de transición, revelación o hover deben implementarse utilizando estrictamente propiedades CSS aceleradas por hardware (`opacity` y `transform`), evitando modificar dimensiones geométricas (`width`, `height`, `top`, `left`) que provoquen reflujo del documento.
* **WCAG 2.1 AA Compliant:**
  * Uso de atributos `aria-label`, `aria-current`, `aria-expanded` y `aria-controls`.
  * Estados visuales claros de focus (`focus-visible`), contraste de color adecuado para lectura y soporte para reducción de movimiento (`prefers-reduced-motion`).
  * Enlaces descriptivos y etiquetas `label` asociadas a sus respectivos controles de formulario.

---

## 5. Arquitectura de Código y Preparación para el Futuro
* **Desacoplamiento Absoluto:** El frontend debe diseñarse sin lógica de negocio hardcodeada ni acoplamientos a bases de datos. Cada componente debe identificarse mediante selectores e IDs lógicos (`id="[seccion]-[elemento]"`) que faciliten la futura integración con Django, APIs REST y sistemas CRM/ERP.
* **Tecnologías Permitidas:** HTML5 semántico, Tailwind CSS v3 (vía variables o configurador), Alpine.js y Vanilla JavaScript.
* **PROHIBIDO:** Incorporar frameworks robustos de JS (React, Vue, Angular) o librerías heredadas como Bootstrap y jQuery.
