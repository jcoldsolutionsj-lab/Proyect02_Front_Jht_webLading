# 🚛 JHT Transport - Frontend

Portal de servicios logísticos para JHT Transport Company SAC.

## 📋 Descripción

Landing page, sistema de rastreo de envíos y dashboard administrativo.  
Diseñado con enfoque en UI/UX profesional ("La Calidez de la Confianza"), con animaciones suaves y microinteracciones que transmiten seguridad y cercanía al usuario.

## 🛠️ Tecnologías

- **HTML5** (estructura semántica)
- **Tailwind CSS** (estilos y diseño responsive)
- **Alpine.js** (interacciones ligeras)
- **Vanilla JS** (scroll animations, tracking, dashboard)
- **Node.js / npm** (gestión de dependencias)

## 📂 Estructura de Ramas
main
└── develop
├── feature/configuracion (Tailwind, estructura base)
├── feature/components (Header, Footer, componentes reutilizables)
├── feature/home
├── feature/landing
├── feature/servicios
├── feature/flota
├── feature/nosotros
├── feature/contacto
├── feature/rastreo
└── feature/

## 🚀 Despliegue

**Static Site en Render.**  
El frontend se sirve desde un CDN, comunicándose con el backend (Django) mediante API REST.

## 📦 Instalación y desarrollo

```bash
npm install
npm run build:css
npm start
