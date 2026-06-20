1. Estructura de Carpetas del Proyecto

# Configuración del Proyecto Frontend - JHT Transport

## 1. Estructura de Carpetas del Proyecto
# Configuración del Proyecto Frontend - JHT Transport

## 1. Estructura de Carpetas del Proyecto
Proyect02_jht_Front_PaginaWebLading/
├── src/
│ ├── assets/
│ │ ├── images/
│ │ │ ├── branding/
│ │ │ │ ├── JHTmarca-transparente.png
│ │ │ │ └── JHTmarca.webp
│ │ │ ├── clientes/
│ │ │ │ ├── home_4_3/
│ │ │ │ │ ├── alicorp_4_3.webp
│ │ │ │ │ ├── ibermatica_4_3.webp
│ │ │ │ │ ├── inkacrops_4_3.webp
│ │ │ │ │ ├── inkafarma_4_3.webp
│ │ │ │ │ ├── linde_4_3.webp
│ │ │ │ │ ├── lubtec_4_3.webp
│ │ │ │ │ ├── movitecnica_4_3.webp
│ │ │ │ │ ├── quibrimsac_4_3.webp
│ │ │ │ │ └── sew_4_3.webp
│ │ │ │ └── logos_1_1/
│ │ │ │ ├── Alicorp.png
│ │ │ │ ├── ibermatica.jpg
│ │ │ │ ├── inkacrops.jpg
│ │ │ │ ├── inkafarma.jpg
│ │ │ │ ├── linde.png
│ │ │ │ ├── lubtec.jpg
│ │ │ │ ├── Movitecnica.jpg
│ │ │ │ ├── quimicaBrisas.gif
│ │ │ │ └── sewEurodrive.jpg
│ │ │ ├── servicios/
│ │ │ │ ├── Banner_Almacenaje.webp
│ │ │ │ ├── Banner_CargaRefrigerada.webp
│ │ │ │ ├── Banner_Carga_Sobredimensionada.webp
│ │ │ │ ├── Banner_DeliveryExpress.webp
│ │ │ │ ├── Banner_Distribucion.webp
│ │ │ │ ├── Banner_Mudanza.webp
│ │ │ │ └── Banner_PersonaldeEstiba.webp
│ │ │ ├── nosotros/
│ │ │ │ ├── banner_1.webp
│ │ │ │ ├── banner_2.webp
│ │ │ │ └── banner_3.webp
│ │ │ ├── flota/
│ │ │ │ ├── banner_1.webp
│ │ │ │ ├── banner_dia_2.webp
│ │ │ │ └── banner_noche_3.webp
│ │ │ └── contacto/
│ │ │ ├── banner_dia_2.webp
│ │ │ ├── banner_dia_cola_3.webp
│ │ │ └── banner_noche_1.webp
│ │ └── videos/
│ │ ├── home/
│ │ │ ├── jhtOriginal.mp4
│ │ │ └── RutasEstados_jht.mp4
│ │ ├── landing/
│ │ │ ├── banner_landingPage.mp4
│ │ │ ├── CoberturaMapa_LandingPage.mp4
│ │ │ └── Coordenadas_Continentes.mp4
│ │ └── flota/
│ │ ├── FlotaLiviana.mp4
│ │ ├── FlotaMedia.mp4
│ │ └── FlotaPesada.mp4
│ ├── css/
│ │ ├── tailwind.css
│ │ └── style.css
│ ├── js/
│ │ ├── main.js
│ │ ├── tracking.js
│ │ └── dashboard.js
│ ├── pages/
│ │ ├── index.html
│ │ ├── rastreo.html
│ │ └── dashboard.html
│ └── components/
├── public/
├── package.json
├── tailwind.config.js
├── postcss.config.js
└── README.md

## 2. Instalación de Dependencias (Versiones Exactas)

bash
# Inicializar proyecto
npm init -y

# Instalar Tailwind CSS y sus dependencias
npm install -D tailwindcss@3.4.1 postcss@8.4.35 autoprefixer@10.4.18

# Instalar Alpine.js
npm install alpinejs@3.13.3

# Instalar Live Server para desarrollo local
npm install -D live-server@1.2.2

3. Archivos de Configuración
tailwind.config.js
javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'jht-dark': '#1A3B6B',
        'jht-gold': '#FFD400',
        'jht-gray': '#E3E4E5',
        'jht-gray-dark': '#909AB3',
        'jht-blue-support': '#57678E',
      }
    },
  },
  plugins: [],
}
postcss.config.js
javascript
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
package.json (scripts)
json
"scripts": {
  "build:css": "tailwindcss -i ./src/css/tailwind.css -o ./src/css/style.css --watch",
  "build": "tailwindcss -i ./src/css/tailwind.css -o ./src/css/style.css --minify",
  "build:all": "npm run build && npm run build:css",
  "start": "live-server src/"
}

## 4. Despliegue en Render (Static Site - Recomendado)

**Pasos:**

1. **Construir el proyecto localmente** (opcional, o que Render lo haga):
   ```bash
   npm run build:all
