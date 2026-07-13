Jimy
Alta
REQF01
Loguin
Acceso restringido al aplicativo en donde solo los colaboradores puedan ingresar mediante credenciales asignadas por un administrador.
Adriana
Alta
REQF02
Listar Ordenes pendientes
El conductor debe visualizar una lista de pendientes de las ordenes de envío.
Adriana
Alta
REQF03
Actualización de ordenes pendientes
El conductor debe realizar la actualización del estado de la orden.
Adriana
Alta
REQF04
Registrar ordenes de envíos
El administrador solo tendrá el acceso para este módulo de registro de orden.
Adriana
Baja
REQF05
Consultar pedido
Modulo libre en donde estará el form de consulta por medio del código de orden para que realicen el seguimiento los clientes

REQUISITOS NO FUNCIONALES:
STAKEHOLDER
PRIORIDAD OTORGADA POR EL STAKEHOLDER
REQUERIMIENTOS
CODIGO
CONCEPTO
DESCRIPCIÓN
Jimy
Alta
REQN06
Despliegue por Servidor web
El aplicativo debe desplegarse en un servidor web para la parte administrativa.
Jimy
Alta
REQN07
Despliegue por Sistema Android
El módulo conductor debe desplegarse en Android desde la versión 14 en adelante.
Jimy
Media
REQN08
Motor DB PostgreSQL
El proyecto debe contar con el motor de base de datos PostgreSQL versión 16 y ser desarrollado con software libre
Jimy
Baja
REQN09
Interfaz intuitiva
Debe tener una interfaz gráfica intuitiva.
Jimy
Baja
REQN10
Tiempo de respuesta
El tiempo de consulta de las actividades debe ser como máximo 5 segundos
REQUISITOS DE CALIDAD:
STAKEHOLDER
PRIORIDAD OTORGADA POR EL STAKEHOLDER
REQUERIMIENTOS
CODIGO
CONCEPTO
DESCRIPCIÓN
Jimy
Media
REQC11
Sistema cerrado
Se debe prohibir el acceso a usuarios no autorizados, para esto se manejará credenciales gestionadas por el encargado administrador.
Jimy
Alta
REQC12
Sistema seguro
El aplicativo web debe estar seguro de las inyecciones SQL y mitigar otros riesgos de seguridad.
Jimy
Media
REQC13
Sistema Cifrado Hash
Las credenciales deben estar ocultas en la DB con un nivel de encriptación avanzado.
CRITERIOS DE ACEPTACIÓN:
CONCEPTO
CRITERIOS DE ACEPTACIÓN
Iniciar el proceso con disponibilidad 24X7.
Que el MPF cuente con un trabajo continuo sin interrupción.
Revisar las ordenes pendientes desde el mas antiguo al más reciente.
Contar con un algoritmo de filtro de antigüedad de casos.
Gestionar los errores.
Ser capaz de tomar flujos alternos al observar errores de los sistemas.
Comunicar una base de trazabilidad.
Brindar como datos de salida la base de trazabilidad.
Integridad con otros sistemas.
Que el MPF se comunique con los diferentes recursos habilitados.
REGLAS DE NEGOCIO:
REGLA 1 los clientes solo pueden revisar el estado de su orden.
REGLA 2 los clientes no necesitan credenciales para utilizar el servicio de consulta, solo deben contar con su código.
REGLA 3 El cliente puede realizar la consulta y descarga de sus documentos con el código de orden y su ruc
REGLA 4 El administrador puede realizar cualquier gestión.
REGLA 5 Los conductores solo se limitarán a realizar la actualización de las órdenes y adjuntar documento en caso así lo solicite el sistema.
IMPACTOS EN OTRAS ÁREAS:
Generar una trazabilidad de las ordenes de servicio.
Mayor control y trazabilidad de la flota.
Generar una base para su análisis posterior.
Agilizar el proceso de asignación de órdenes.
IMPACTOS EN OTRAS ENTIDADES:
El cliente JHT mejorará su prestigio frente al cliente final.
REQUISITOS DE SOPORTE Y ENTRENAMIENTO:
Capacitación para todos los miembros del proyecto durante el primer mes.
SUPUESTOS RELATIVOS A REQUISITOS:
La recopilación de los requisitos fue completa y pertinente.
RESTRICCIONES RELATIVAS A REQUISITOS:
--

