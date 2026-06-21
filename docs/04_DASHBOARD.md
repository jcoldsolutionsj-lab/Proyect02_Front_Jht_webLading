# Especificaciones - Dashboard de Administración

## 1. Objetivo del Dashboard
Proveer a los administradores de JHT una vista rápida y clara del estado de las operaciones. El enfoque es **50% UI/UX limpio y 50% funcional**.

## 2. Diseño General
- **Layout:** Sidebar izquierdo + contenido principal.
- **Sidebar:**
  - Fondo: `#021E5F` (azul marino).
  - Ítems: `Dashboard | Servicios | Guías | Flota | Clientes | Configuración | Cerrar Sesión`.
  - El ítem activo debe tener un indicador (ej. barra lateral amarilla `#FDCF06`).
  - Hover con cambio de fondo sutil.
- **Contenido principal:**
  - Fondo: `#E3E4E5` (gris claro).
  - Header con título y botón de "Nuevo Servicio".

## 3. Componentes del Contenido Principal

### 3.1 Cards de Estadísticas (4 columnas)
- **Servicios Activos:** 24 (con ícono 📦)
- **Entregas Completadas:** 156 (con ícono ✅)
- **Pendientes:** 8 (con ícono ⏳)
- **Clientes Activos:** 42 (con ícono 👥)

Cada card debe tener:
- Fondo blanco.
- Borde izquierdo de 4px en un color distintivo (ej. `#FDCF06` para activos, `#4CAF50` para completados, etc.).
- Número grande y legible.
- Tendencia (ej. "↑ 12% vs ayer") en color verde o rojo.

### 3.2 Tabla de Servicios Recientes
- **Columnas:** `Guía | Cliente | Servicio | Estado | Fecha`
- **Estados con badges:**
  - `Completado` → Fondo verde (`#E8F5E9`), texto `#2E7D32`.
  - `En Ruta` → Fondo naranja (`#FFF3E0`), texto `#E65100`.
  - `Pendiente` → Fondo rojo (`#FFEBEE`), texto `#C62828`.
- **Acciones:** Botón "Ver todos" que lleva a la lista completa de servicios.

### 3.3 Gráfico de Servicios por Día (Última Semana)
- Representación visual simple (puede ser con CSS puro o con Chart.js).
- Mostrar barras o líneas con los días de la semana en el eje X.
- Los datos pueden ser estáticos y de ejemplo.

## 4. Interacciones y Comportamiento
- **Sidebar:** Colapsable en móvil (con botón hamburguesa).
- **Tabla:** Responsive (scroll horizontal en móvil).
- **Cards:** Hover con elevación sutil.

## 5. Instrucciones para el Agente

Construye un dashboard de administración con estas características. El diseño debe ser limpio, profesional y priorizar la legibilidad de los datos. Usa Tailwind CSS para el layout y Vanilla JS para cualquier interacción básica (apertura/cierre de sidebar en móvil). Los datos pueden ser estáticos y de ejemplo. No se necesita lógica de backend aún.