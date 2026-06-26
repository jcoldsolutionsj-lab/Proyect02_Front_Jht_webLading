# 📦 Guía de Despliegue: Local + Producción (Render)

> **Objetivo:** Documento de referencia para configurar cualquier proyecto nuevo con esta misma estructura y que funcione tanto en **desarrollo local** como en **producción (Render)** sin errores.

---

## 📁 Estructura del Proyecto Esperada

```
proyecto/
├── docs/
├── src/
│   ├── assets/
│   │   ├── images/
│   │   └── videos/
│   ├── components/
│   ├── css/
│   │   ├── tailwind.css      ← Código fuente (con @tailwind directives)
│   │   └── style.css          ← CSS compilado (generado por Tailwind CLI)
│   ├── js/
│   │   └── main.js
│   └── pages/
│       └── index.html         ← Página principal
├── public/                     ← Carpeta generada por Vite (NO commitear)
├── .gitignore
├── package.json
├── postcss.config.js
├── tailwind.config.js
└── vite.config.ts
```

---

## 🔧 Archivos de Configuración Clave

### 1. `package.json` — Scripts

```json
{
  "scripts": {
    "dev": "vite --port=3000 --host=0.0.0.0",
    "build": "vite build",
    "preview": "vite preview",
    "build:css": "tailwindcss -i ./src/css/tailwind.css -o ./src/css/style.css --watch",
    "start": "live-server src/"
  },
  "devDependencies": {
    "autoprefixer": "^10.4.18",
    "postcss": "^8.4.35",
    "tailwindcss": "^3.4.1",
    "vite": "^6.4.3"
  }
}
```

| Script | Uso |
|---|---|
| `npm run dev` | Servidor de desarrollo con Vite (Hot Reload) |
| `npm run build` | Genera la carpeta `public/` para producción |
| `npm run preview` | Previsualiza el build de producción |
| `npm run build:css` | Compila Tailwind en modo watch (desarrollo local con live-server) |
| `npm start` | Servidor local simple con live-server |

---

### 2. `vite.config.ts` — Configuración de Vite

```typescript
import { defineConfig } from 'vite';

export default defineConfig({
  root: 'src/pages',
  build: {
    outDir: '../../public',
    emptyOutDir: true,
  },
});
```

> [!IMPORTANT]
> **`root: 'src/pages'`** le dice a Vite que el `index.html` está dentro de `src/pages/`.
> El `outDir` usa `../../public` porque es **relativo al root**, así que sube dos niveles para crear la carpeta `public/` en la raíz del proyecto.

> [!CAUTION]
> **NO uses `rollupOptions.input`** para apuntar al HTML si `root` no está configurado. Eso genera la salida en `public/src/pages/index.html` en vez de `public/index.html`, y las rutas de assets se rompen en producción.

---

### 3. `postcss.config.js` — PostCSS (para Tailwind)

```javascript
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  }
}
```

> Este archivo permite que Vite procese automáticamente el CSS de Tailwind durante el `vite build`.

---

### 4. `tailwind.config.js` — Tailwind CSS

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}",
  ],
  theme: {
    extend: {
      // tus colores, fuentes, animaciones...
    },
  },
  plugins: [],
}
```

> [!IMPORTANT]
> La ruta `content` **siempre es relativa a la raíz del proyecto**, NO al root de Vite. Esto es correcto: `"./src/**/*.{html,js}"`.

---

### 5. `.gitignore` — Archivos Ignorados

Asegúrate de que estas líneas estén presentes:

```gitignore
node_modules/
public/
dist/
```

> [!WARNING]
> **Nunca subas la carpeta `public/`** al repositorio. Render la genera automáticamente al ejecutar `npm run build`.

---

## 🌐 Configuración en Render (Static Site)

| Campo | Valor |
|---|---|
| **Build Command** | `npm run build` |
| **Publish Directory** | `public` |
| **Branch** | `main` |
| **Node Version** | 20+ (por defecto Render usa la última LTS) |

> [!CAUTION]
> El **Publish Directory** debe ser exactamente **`public`** (sin subcarpetas). Si pones `public/src/pages`, Render no encontrará el `index.html` y el deploy fallará.

---

## ⚠️ Errores Comunes y Cómo Evitarlos

### ❌ Error 1: `Could not resolve entry module "index.html"`

**Causa:** Vite busca `index.html` en la raíz del proyecto, pero el archivo está en `src/pages/`.

**Solución:** Configurar `root: 'src/pages'` en `vite.config.ts`.

---

### ❌ Error 2: `Publish directory public does not exist!`

**Causa:** El script `build` en `package.json` no usa Vite, solo compila CSS con Tailwind.

**Solución:** Cambiar el script `build` a `"vite build"`.

---

### ❌ Error 3: JavaScript no funciona en producción (animaciones, scroll, parallax)

**Causa:** El `<script>` en el HTML no tiene `type="module"`. Vite advierte:
```
<script src="../js/main.js"> can't be bundled without type="module" attribute
```
Vite NO empaqueta el archivo y en producción el navegador recibe un **404**.

**Solución:**
```html
<!-- ❌ INCORRECTO — Vite no lo empaqueta -->
<script src="../js/main.js" defer></script>

<!-- ✅ CORRECTO — Vite lo empaqueta y lo incluye en /assets/ -->
<script type="module" src="../js/main.js"></script>
```

> [!IMPORTANT]
> Los módulos (`type="module"`) ya son `defer` por defecto, así que no necesitas agregar el atributo `defer`.

---

### ❌ Error 4: CSS se pierde en producción (diseño roto)

**Causa:** El HTML apunta a `style.css` (compilado manualmente) pero en producción Vite debería compilar Tailwind automáticamente.

**Solución:** Verificar que `postcss.config.js` exista con Tailwind configurado. Vite procesa el CSS automáticamente si PostCSS está configurado.

> [!TIP]
> Si usas `style.css` (precompilado) localmente, Vite lo incluirá tal cual en el build. Eso funciona bien siempre y cuando tu `style.css` esté actualizado con todos los cambios de Tailwind.

---

### ❌ Error 5: `Publish directory public/src/pages does not exist!`

**Causa:** Usaste `rollupOptions.input` para apuntar al HTML **sin configurar `root`**. Vite genera el HTML respetando la estructura de carpetas: `public/src/pages/index.html`.

**Solución:** Usar `root: 'src/pages'` en lugar de `rollupOptions.input`. Así Vite genera `public/index.html` directamente.

---

### ❌ Error 6: Imágenes/Videos no cargan en producción

**Causa:** Vite solo empaqueta archivos que están **referenciados directamente** en el HTML o importados en JS/CSS. Archivos sueltos no se copian.

**Solución:** Verificar que todas las imágenes y videos estén referenciados en el HTML con rutas relativas correctas:
```html
<!-- Desde src/pages/index.html, las imágenes están en: -->
<img src="../assets/images/branding/logo.png">
<video>
  <source src="../assets/videos/home/video.mp4" type="video/mp4">
</video>
```

---

## 🚀 Checklist para Nuevo Proyecto

- [ ] Instalar dependencias: `npm install -D vite tailwindcss autoprefixer postcss`
- [ ] Crear `vite.config.ts` con `root: 'src/pages'` y `outDir: '../../public'`
- [ ] Crear `postcss.config.js` con tailwindcss y autoprefixer
- [ ] Crear `tailwind.config.js` con `content: ["./src/**/*.{html,js}"]`
- [ ] Script `build` en package.json: `"vite build"`
- [ ] Todos los `<script>` propios deben tener `type="module"`
- [ ] Agregar `public/` al `.gitignore`
- [ ] Probar `npm run build` localmente antes de subir
- [ ] En Render: Build Command = `npm run build`, Publish Directory = `public`

---

## 🔄 Flujo de Trabajo Recomendado

```
┌─────────────────────────────────────────────────┐
│              DESARROLLO LOCAL                    │
│                                                  │
│  Terminal 1: npm run build:css  (compila CSS)    │
│  Terminal 2: npm start          (live-server)    │
│                                                  │
│  O usar Vite directamente:                       │
│  Terminal 1: npm run dev        (todo en uno)    │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│          ANTES DE SUBIR A PRODUCCIÓN             │
│                                                  │
│  1. npm run build     (verificar que compila)    │
│  2. npm run preview   (probar el build local)    │
│  3. git add . && git commit                      │
│  4. git push origin main                         │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│              RENDER (PRODUCCIÓN)                 │
│                                                  │
│  Render detecta el push automáticamente          │
│  Ejecuta: npm install → npm run build            │
│  Sirve: carpeta public/                          │
│  URL: https://tu-proyecto.onrender.com           │
└─────────────────────────────────────────────────┘
```

---

> **Última actualización:** Junio 2026
> **Proyecto de referencia:** JHT Transport Landing Page
> **Stack:** HTML + Tailwind CSS 3 + Alpine.js + Vite 6 + Render (Static Site)
