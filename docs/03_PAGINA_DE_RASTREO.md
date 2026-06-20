# Especificaciones - Página de Rastreo de Envíos

## 1. Objetivo de la Página
Permitir a los usuarios ingresar un código de seguimiento y visualizar el estado de su envío a través de una **línea de tiempo interactiva** que muestra el progreso en 5 pasos. La experiencia debe transmitir **seguridad, transparencia y control**, con microinteracciones que mantengan al usuario tranquilo e informado.

---

## 2. Flujo de Navegación (Desde el Home)

1. **En el Home (Hero):** Sobre los videos de fondo, hay un input con un botón **"Rastrear"**.
2. El usuario ingresa su código de seguimiento y hace clic en **"Rastrear"**.
3. Es redirigido a la página de rastreo (`/rastreo`), donde se muestran los resultados detallados de su envío.

---

## 3. Diseño Visual (Página de Rastreo)

- **Fondo:** `#E3E4E5` (gris claro, consistente con la landing).
- **Contenedor principal:** Blanco, con bordes redondeados (`rounded-2xl`), sombra suave (`shadow-lg`), y padding generoso.
- **Título superior:** `"Seguimiento de tu Carga"` (en `#1A3B6B`).
- **Número de guía:** `"Guía N° 3241307995"` (en `#57678E`, tamaño mediano).
- **Detalle del producto:** `"Repuestos Industriales"` (en `#1A3B6B`) y `"1 un. | 150 kg est."` (en `#909AB3`).

### 3.1 Línea de Tiempo (5 Pasos)

La línea de tiempo debe mostrar 5 pasos en orden:

1. **Solicitud recibida**
2. **En preparación**
3. **En tránsito**
4. **Listo para entrega**
5. **Entregado**

**Estados visuales para cada paso:**

| Estado | Color | Ícono | Descripción visual |
| :--- | :--- | :--- | :--- |
| **Completado** | `#4CAF50` (verde) | ✅ | Paso finalizado exitosamente. |
| **Estado Actual** | `#FFD400` (amarillo JHT) | ⏳ | Paso en progreso. Se marca con un círculo o barra animada. |
| **Pendiente** | `#909AB3` (gris apoyo) | ○ | Paso aún no iniciado. |

**Ejemplo visual (basado en la captura):**

- **Solicitud recibida:** Completado ✅
- **En preparación:** Estado Actual ⏳ (resaltado en amarillo)
- **En tránsito:** Pendiente ○
- **Listo para entrega:** Pendiente ○
- **Entregado:** Pendiente ○

**Texto adicional:** Debajo de "Estado Actual", se muestra: *"Terminamos de preparar tu pedido, te avisaremos cuando esté listo para el despacho."* (en `#57678E`, tamaño pequeño, cursiva).

### 3.2 Microinteracciones (Seguridad y Calidez)

- **Puntitos animados ("..."):** Al hacer clic en "Rastrear" y mientras se simula la búsqueda, mostrar tres puntitos animados (como "cargando") para que el usuario sepa que el sistema está procesando su solicitud.
- **Tooltips en la línea de tiempo:** Al pasar el cursor sobre cada paso, mostrar un tooltip con una frase cálida y tranquilizadora:
  - **Solicitud recibida:** *"¡Ya recibimos tu solicitud! Estamos iniciando el proceso."*
  - **En preparación:** *"Estamos alistando tu carga con el mayor cuidado."*
  - **En tránsito:** *"Tu carga está en camino. ¡Pronto llegará!"*
  - **Listo para entrega:** *"¡Casi listo! El transportista está en camino."*
  - **Entregado:** *"¡Tu carga fue entregada con éxito! Gracias por confiar en JHT."*

---

## 4. Lógica de Estados (JavaScript Vanilla + Alpine.js)

La página debe manejar 4 estados visuales:

| Estado | Descripción | Elementos visibles |
| :--- | :--- | :--- |
| **idle** | Estado inicial, sin búsqueda. | Input + Botón. Área de resultados vacía (solo el contenedor limpio). |
| **loading** | El usuario hizo clic en "Rastrear". | Input + Botón (deshabilitado). **Puntitos animados** ("...") y mensaje: *"Buscando tu envío..."*. |
| **found** | Se encontró el envío (simulado). | Input + Botón. Área de resultados con: Número de guía, Detalle del producto, Línea de tiempo con estados, Texto de estado actual. |
| **not-found** | No se encontró el envío. | Input + Botón. Área de resultados con mensaje de error: *"No encontramos ningún envío con ese código. Por favor, verifica el número ingresado."* (en `#FF6B6B`, rojo suave). |

### 4.1 Simulación de Datos (Para pruebas)
- Usar `setTimeout` para simular una respuesta de API después de **1.5 segundos**.
- **Para "found":** Mostrar:
  - Guía: `"3241307995"`
  - Producto: `"Repuestos Industriales"`
  - Peso: `"1 un. | 150 kg est."`
  - **Estado Actual:** `"En preparación"` (amarillo JHT)
  - **Texto descriptivo:** `"Terminamos de preparar tu pedido, te avisaremos cuando esté listo para el despacho."`
  - **Línea de tiempo:** `Solicitud recibida (Completado) → En preparación (Actual) → En tránsito (Pendiente) → Listo para entrega (Pendiente) → Entregado (Pendiente)`
- **Para "not-found":** Mostrar mensaje de error con un ícono de advertencia.

### 4.2 Validación Básica
- El input no debe estar vacío al hacer clic en "Rastrear".
- Si está vacío, mostrar un mensaje de error sutil (ej. borde rojo en el input y texto: *"Por favor, ingresa un código de seguimiento."*).

---

## 5. Integración con el Diseño General
- La página debe compartir el **Header** y **Footer** de la landing page para mantener la consistencia.
- Los colores, tipografías y estilos deben ser los mismos definidos en `01_ESTRUCTURA_Y_DISEÑO.md`.
- **Paleta:** Usar variables CSS o clases de Tailwind extendidas (no valores hex fijos).

---

## 6. Marcadores (IDs) para Conexión con Django

| Elemento | ID |
| :--- | :--- |
| Input de búsqueda | `id="tracking-input"` |
| Botón "Rastrear" | `id="tracking-button"` |
| Área de resultados | `id="tracking-results"` |
| Número de guía | `id="tracking-guia"` |
| Detalle del producto | `id="tracking-producto"` |
| Texto de estado actual | `id="tracking-estado-texto"` |
| Línea de tiempo (contenedor) | `id="tracking-timeline"` |
| Cada paso (1-5) | `id="tracking-paso-1"`, `id="tracking-paso-2"`, ..., `id="tracking-paso-5"` |

---

## 7. Instrucciones para el Agente

Genera el código HTML, CSS y JavaScript para esta página. El JavaScript debe ser **Vanilla JS** (sin frameworks) para la lógica de búsqueda y la manipulación del DOM. Usa **Alpine.js** (si es necesario) para manejar el estado de la línea de tiempo o las microinteracciones.

**Requisitos obligatorios:**
1. **Animación de puntitos:** Mientras se busca, mostrar tres puntitos animados (secuencia `...` con intervalo de 300ms).
2. **Tooltips en la línea de tiempo:** Al hacer hover sobre cada paso, mostrar un tooltip con una frase cálida.
3. **Línea de tiempo visual:** Los pasos deben estar conectados por una línea vertical o barras, con el estado actual resaltado en amarillo (`#FFD400`), los completados en verde (`#4CAF50`) y los pendientes en gris (`#909AB3`).
4. **Responsive:** El diseño debe adaptarse a móvil, tablet y escritorio.
5. **Colores:** Usar variables CSS o clases de Tailwind extendidas (no valores hex fijos).

---

**Entregable esperado:** Un archivo HTML completo (con CSS y JS incrustados o separados) que reproduzca esta página de rastreo con todos los estados, animaciones y tooltips funcionales. El código debe ser limpio, comentado y escalable para futura integración con Django.