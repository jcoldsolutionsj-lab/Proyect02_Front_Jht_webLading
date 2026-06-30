# Arquitectura Global y Esqueleto Visual de la Landing Page

## 1. Objetivo
Este documento define la estructura y el orden jerárquico de la Landing Page de JHT Transport, basándose en el prototipo original. Su propósito es guiar el ensamblaje de todas las secciones para que el resultado final sea visualmente idéntico al diseño aprobado.

## 2. Flujo Vertical (La Experiencia del Usuario)

La página debe guiar al usuario en este orden, de arriba a abajo, sin excepciones:

1.  **Hero (Sección Principal)**
    *   **Objetivo:** Impactar y captar la atención. El usuario debe saber inmediatamente qué hace JHT.
    *   **Elementos:** Video de fondo a pantalla completa (`jhtOriginal.mp4`), superpuesto con el eslogan "Logística y Trazabilidad en Tiempo Real" y el **Widget de Seguimiento**. Este widget es el punto de interacción principal y debe ser prominente.

2.  **Nuestros Servicios**
    *   **Objetivo:** Mostrar la oferta de valor principal de forma clara y rápida.
    *   **Elementos:** Título, subtítulo y **grid de 4 tarjetas** con iconos. Las tarjetas deben tener la misma altura y estar alineadas.

3.  **Nuestros Clientes Opinan** (Logos)
    *   **Objetivo:** Generar confianza y credibilidad a través de la prueba social.
    *   **Elementos:** Título y un **carrusel o grid de logos** de clientes conocidos. Debe sentirse como un respaldo visual.

4.  **Nuestra Flota** (Tabs)
    *   **Objetivo:** Mostrar la capacidad y modernidad de los vehículos.
    *   **Elementos:** Título, subtítulo y los **3 tabs** (Liviana, Mediana, Pesada). El contenido de cada tab debe mostrar una imagen/video y las especificaciones clave.

5.  **Sobre Nosotros**
    *   **Objetivo:** Humanizar la marca y explicar la misión/visión.
    *   **Elementos:** Título, texto descriptivo, valores (Transparencia, Innovación, etc.) y un **carrusel de 3 imágenes** relacionadas con la empresa.

6.  **Contacto**
    *   **Objetivo:** Convertir al usuario en lead o cliente. Es la llamada final a la acción.
    *   **Elementos:** Título, subtítulo, **formulario** (con validación) y datos de contacto (dirección, teléfono, email) con un **mapa**.

## 3. Reglas de Maquetación (El "Cómo")

*   **Ancho Máximo:** Todos los contenedores de contenido deben tener `max-w-7xl mx-auto`.
*   **Espaciado:** Cada sección debe tener `py-20` (padding vertical). El espacio entre secciones debe ser uniforme.
*   **Grid:** Usar el sistema de grid de Tailwind para alinear tarjetas y elementos (ej. `grid-cols-4` para escritorio, `grid-cols-2` para tablet, `grid-cols-1` para móvil).
*   **Jerarquía Tipográfica:** Los títulos principales (`h1`) deben ser más grandes que los subtítulos (`h2`), etc.
*   **Contraste:** El texto siempre debe ser legible sobre el fondo. Usar clases de texto `text-white` sobre fondos oscuros (`bg-brand-navy`).

## 4. Referencia Visual Final

El resultado final de este ensamblaje debe ser visualmente indistinguible del prototipo presentado en Stitch. La prioridad es la fidelidad al diseño.

## 5. Integración con Django

Todos los textos, imágenes y videos deben estar referenciados mediante marcadores (`id`) para que el backend de Django pueda inyectar el contenido dinámicamente. Los marcadores deben ser los definidos en `02_CONTENIDO_Y_MAQUETACION.md`.