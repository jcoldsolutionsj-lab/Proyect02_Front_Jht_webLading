# Especificaciones de Diseño UI/UX - "La Calidez de la Confianza"

## 1. Objetivo del Diseño
Transformar el prototipo actual en una experiencia digital (Responsivo) donde el usuario sienta **seguridad, cercanía y absoluto control**. La percepción debe ser: *"JHT cuida mi carga como si fuera mía"*.

---

## 2. Paleta de Colores (Con Propósito Emocional)

Utiliza estrictamente estos colores, asignándoles el siguiente propósito:

| Color | Hex | Uso | Emoción |
| :--- | :--- | :--- | :--- |
| **Azul JHT (Estructura)** | `#1A3B6B` | Navbars, Footers, títulos principales | Solidez, autoridad, calma |
| **Amarillo JHT (Acento)** | `#FFD400` | Botones CTA, estados de éxito, iconos decorativos | Calidez, acción, confianza |
| **Gris Claro (Base)** | `#E3E4E5` | Fondo principal del cuerpo | Acogedor, mate, "pared de caliza" |
| **Azul Apoyo 1** | `#909AB3` | Bordes, divisores, textos secundarios | Sutileza, profesionalismo |
| **Azul Apoyo 2** | `#57678E` | Textos secundarios, subtítulos | Profundidad, descanso visual |

**Regla de oro:** El Amarillo JHT (`#FFD400`) es el **foco de atención**. Solo debe aparecer en elementos que requieran acción del usuario. El resto de la página debe ser un remanso de paz visual con los azules y grises.

---

### 🧩 Paleta de Colores Modular (Mantenimiento y Escalabilidad)

Para garantizar que el proyecto sea **fácil de mantener y escalar**, los colores deben definirse en un **único punto de control** dentro del código. Esto permite realizar cambios globales (ej. ajustar el tono del azul o del amarillo) sin necesidad de modificar archivo por archivo.

**Estrategia de implementación:**

1. **Variables CSS (Custom Properties):**
   - Definir todos los colores en el selector `:root` dentro del archivo CSS principal.
   - Ejemplo:
     ```css
     :root {
       --color-primary: #1A3B6B;
       --color-accent: #FFD400;
       --color-bg: #E3E4E5;
       --color-border: #909AB3;
       --color-text-secondary: #57678E;
     }```


## 3. Efectos y Movimientos (Obligatorios)

### 3.1 Parallax Scrolling
- Aplicar **ÚNICAMENTE** en la sección Hero.
- El video de fondo (`videos/home/jhtOriginal.mp4`) debe moverse un **15% más lento** que el texto y los botones del primer plano.
- **Debe ser sutil** para no marear ni ralentizar la página.

### 3.2 Scroll-Triggered Animations
- Todas las secciones (Servicios, Clientes, Flota, Testimonios, Contacto) deben tener animaciones al hacer scroll.
- **Efecto:** `fade-in` + `slide-up`.
  - Estado inicial: `opacity: 0; transform: translateY(40px);`
  - Estado final (cuando entra al viewport): `opacity: 1; transform: translateY(0);`
- **Transición:** 0.6s ease-out.
- Usar **Intersection Observer API** para detectar cuándo los elementos entran en el viewport.

### 3.3 Sticky Navigation + Smooth Scroll
- El menú debe ser **fijo (sticky)** en la parte superior al hacer scroll.
- **Comportamiento:**
  - Al inicio (scroll = 0): Fondo **transparente**.
  - Al hacer scroll: Fondo **sólido #1A3B6B** con una sombra sutil.
  - Transición suave entre ambos estados.
- Todos los enlaces internos (anclas como `#servicios`, `#flota`, etc.) deben tener **Smooth Scroll** (desplazamiento suave, no salto brusco).

### 3.4 Microinteracciones (La "Sonrisa" del Diseño)
- **Botones:** Hover con `scale-[1.02]` y sombra amarilla suave (`shadow-[#FFD400]/40`).
- **Tarjetas de Servicios:** Hover con elevación (`translateY(-8px)`) y sombra más profunda.
- **Campos de formulario (Inputs):**
  - Borde por defecto: `#909AB3`.
  - Al hacer focus: Borde `#1A3B6B` con un **glow sutil** (box-shadow).
- **Logos de Clientes:**
  - Por defecto: Escala de grises (opacidad 60%).
  - Hover: 100% opaco (efecto de "reconocimiento").

### 3.5 Efecto de Carga Inicial
- Toda la página debe tener un **fade-in suave** al cargar.
- Duración: 0.8s.
- Esto mejora la velocidad de carga percibida.

---

## 4. Componentes UI Específicos

### 4.0 NAV (Menú de Navegación)

- **Logo:**  
  - Ruta: `/assets/images/branding/JHTmarca-transparente.png`  
  - Formato: PNG con fondo transparente.  
  - Comportamiento: El logo debe ser un enlace a la página de inicio (`/`).  
  - Al hacer scroll: el logo se mantiene visible y conserva su aspecto, pero el **contenedor del nav** cambia de fondo (de transparente a `#1A3B6B` con una transición suave). El logo no necesita cambiar de color ni de versión, ya que al ser transparente se adapta visualmente a ambos fondos (claro y oscuro).

- **Fondo del nav:**  
  - Estado inicial (scroll = 0): `background: transparent;`  
  - Estado con scroll: `background: #1A3B6B; box-shadow: 0 4px 12px rgba(0,0,0,0.1);`  
  - Transición: `transition: background 0.3s ease, box-shadow 0.3s ease;`

- **Elementos del menú:**  
  - Enlaces: `Servicios`, `Flota`, `Nosotros`, `Contacto`, `Área Cliente` (este último como botón destacado en `#FFD400`).  
  - Comportamiento: Al hacer clic en un enlace interno (ancla), la página debe desplazarse suavemente (Smooth Scroll) hasta la sección correspondiente.

- **Responsive:**  
  - En móvil, el menú se colapsa en un botón hamburguesa (con Alpine.js) y el logo permanece visible.

### 4.1 Hero (Home) - Portada de Bienvenida
- **Fondo:** Degradado sutil de `#E3E4E5` a blanco.
- **Video de fondo:** `videos/home/jhtOriginal.mp4` (20 segundos, ancho completo, `muted`, `playsinline`, `autoplay`, `loop`).
- **Video superpuesto (4:3):** `assets/videos/home/RutasEstados_jht.mp4` (9 segundos, flotante, centrado, `muted`, `playsinline`).
- **Elementos decorativos:** Círculos abstractos en `#FFD400` y `#1A3B6B`.
- **CTA principal:** Botón amarillo (`#FFD400`) con texto en azul marino (`#1A3B6B`): **"Rastrear mi envío"**.

### 4.2 Landing Page (Banner secundario)
- **Video de fondo:** `videos/landing/banner_landingPage.mp4` (10 segundos, ancho completo, `muted`, `playsinline`).
- **Texto superpuesto:** Título y subtítulo de la sección (según contenido en `02_CONTENIDO_Y_MAQUETACION.md`).

### 4.3 Tarjetas de Servicios (y secciones)
- Fondo: Blanco (`bg-white`).
- Borde superior de 4px en `#FFD400` (simula una "luz" que entra por el techo).
- Sombra: `shadow-lg`.
- Hover: Elevación (`translateY(-8px)`).
- **Videos 1:1 en tarjetas:** Entre 2 y 3 videos por sección (Home, Landing, Servicios, Flota, Nosotros, Contacto), con duración de 5-8 segundos, formato 1:1, `muted`, `playsinline`.

### 4.4 Widget de Seguimiento (El Centro de Control)
- Rectángulo blanco con bordes redondeados (`rounded-2xl`).
- Montado sobre un fondo gris (`#E3E4E5`).
- El botón de "Buscar" debe ser el **único elemento en amarillo absoluto** (`#FFD400`).
- Texto circundante en `#1A3B6B`.

### 4.5 Sección "Confían en Nosotros" (Logos)
- Mostrar logos de clientes en escala de grises (opacidad al 60%).
- Hover: 100% opacos (efecto de "reconocimiento").
- **Rutas:** `images/clientes/logos_1_1/*.png|jpg|gif` (para landing) y `images/clientes/home_4_3/*.webp` (para home).

### 4.6 Carrusel de 3 imágenes por sección
- **Servicios:** `images/servicios/Banner_Almacenaje.webp`, `Banner_CargaRefrigerada.webp`, `Banner_Distribucion.webp` (o los que definas).
- **Flota:** `images/flota/banner_1.webp`, `banner_dia_2.webp`, `banner_noche_3.webp`.
- **Nosotros:** `images/nosotros/banner_1.webp`, `banner_2.webp`, `banner_3.webp`.
- **Contacto:** `images/contacto/banner_dia_2.webp`, `banner_dia_cola_3.webp`, `banner_noche_1.webp`.

---

## 5. Tipografía y Espaciado

- **Títulos:** Montserrat (bold, fuerte).
- **Párrafos:** Open Sans (font-light, legible, amigable).
- **Espaciado:** Generoso (`p-10`, `py-20`). El "espacio en blanco" (gris claro) es orden y limpieza.

---

## 6. Lenguaje Cercano (La Voz de la Marca)

- Acompañar los datos técnicos con frases cálidas.
- Ejemplo: Donde diga "Número de Guía", añadir un subtítulo pequeño en `#57678E` que diga: *"¡Estamos al pendiente de tu envío!"*.

---

## 7. Reglas de Implementación Técnica

- **Framework CSS:** Tailwind CSS (con los colores personalizados definidos en `tailwind.config.js`).
- **JavaScript:** Alpine.js para interacciones ligeras (menú móvil, tabs). Vanilla JS para Scroll-Triggered Animations y Parallax.
- **Responsive:** Mobile First. Todos los componentes deben adaptarse a móvil, tablet y escritorio.
- **Rendimiento:** Las animaciones deben usar `transform` y `opacity` (propiedades que no causan reflow). El Parallax debe ser suave y no consumir muchos recursos.
- **Videos:** Todos deben tener `muted` y `playsinline` para reproducción automática sin audio.

---

