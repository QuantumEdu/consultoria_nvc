# Análisis de Sistema — DAMICH
**Versión:** 1.0
**Fecha:** 2026-03-09
**Elaborado por:** Sesión de análisis con IA

---

## Historial de versiones

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | 2026-03-09 | Documento inicial — análisis completo de datos, HTML, arquitectura e insights |

---

## 1. Contexto del Proyecto

DAMICH es una empresa con 3 sucursales activas que generan información operativa diaria:

- **Apatzingán** (sucursal central / servidor)
- **Nueva Italia**
- **San Simón** (internet inestable)

La información se envía diariamente a central. Actualmente se concentra en Excel con macros, lo cual no escala ni es mantenible. El objetivo es construir un sistema de captura + procesamiento + reportes que reemplace ese flujo.

---

## 2. Estructura de Archivos Existentes

### Por sucursal / carpeta:

```
DAMICH/
├── APATZINGAN/
│   └── 2026/
│       ├── CORTE DE CAJA/    → ENE + FEB (CSV)
│       ├── KILEADO/          → ENE (CSV)
│       └── TRASPASOS/        → ENE + FEB (CSV)
├── NUEVA ITALIA/
│   └── 2026/
│       ├── CORTE DE CAJA/    → ENE + FEB (CSV)
│       ├── KILEADO/          → ENE + FEB combinado (CSV)
│       └── TRASPASOS/        → ENE + FEB (CSV)
├── SAN SIMON/
│   └── 2026/
│       ├── CORTE DE CAJA/    → ENE + FEB (CSV)
│       ├── TRAPASOS/         → ENE + FEB parcial (CSV)
│       └── (sin Kileado)
├── PEDIDOS DE LAS 3 SUCURSALES/
│   └── 2026/                 → ENE + FEB (PDF)
└── modulo2_formularios.html  → formulario de captura actual
```

---

## 3. Análisis de los Datos CSV

### 3.1 Corte de Caja

**Formato:** Totales agregados por día de semana (intencional). Ejemplo real:

```
DIA DE LA SEMANA | VENTA DECLARADA | (PROMEDIO)
LUNES            | $356,438.00     | $187,195.67
MARTES           | $244,837.00     | $187,195.67
MIERCOLES        | $135,767.00     | $187,195.67
JUEVES           | $46,742.00      | $187,195.67
VIERNES          | $282,410.00     | $187,195.67
SABADO           | $56,980.00      | $187,195.67
```

**Nota:** Es la suma de todos los días del mismo nombre dentro del mes. No hay granularidad por fecha específica (ej: lunes 5 vs lunes 12). Esto es intencional en la etapa actual.

**Resumen por sucursal (Enero 2026):**

| Sucursal | Promedio semanal | Venta máxima (día) | Venta mínima (día) |
|---|---|---|---|
| Apatzingán | $187,195 | $356,438 (Lunes) | $46,742 (Jueves) |
| Nueva Italia | $169,446 | $306,639 (Lunes) | $46,579 (Jueves) |
| San Simón | $125,361 | *(datos menores)* | *(datos menores)* |

**San Simón — variación importante entre meses:**
- Enero 2026: Promedio $125,361 / semana
- Febrero 2026: Promedio $763,055 / semana → **Confirmado correcto**. Diferencia 6x respecto a Enero.

### 3.2 Kileado

**Formato:** Doble columna — izquierda folios de entrada/salida, derecha detalle de productos.
**Columnas:** FECHA, ENTRADA folio, SALIDA folio, DESCRIPCIÓN DEL PRODUCTO, CANTIDAD, TIPO (K=Kileado / S=Suelto)

**Operadores identificados por sucursal:**
- Apatzingán: ROSY, CECILIA V.
- Nueva Italia: CECILIA V., BRISEIDA D.
- San Simón: PAOLA

**San Simón** no tiene carpeta de Kileado — no genera este tipo de movimiento.

**Productos más frecuentes en Kileado (top por repetición):**

| Producto | Apariciones | Tipo |
|---|---|---|
| GATIMAR | 6+ | K |
| PRO-STAR | 5+ | K |
| KEY CAN | 4+ | K |
| PRO-FLOCK | 3+ | K |
| LAYINA | 2+ | K |
| ECTOLINE GOTERO 10ML | 2 | S |

### 3.3 Traspasos

**Formato:** Doble columna — izquierda: control de folios por fecha de envío; derecha: detalle de productos recibidos (con fecha real de recepción).

**Dirección de flujo identificado:**
- Apatzingán → Nueva Italia
- Nueva Italia → Apatzingán
- San Simón → Nueva Italia
- San Simón → Apatzingán

**Responsables frecuentes:**
- BRISEIDA D. (Nueva Italia)
- CECILIA V. (Apatzingán)
- VIANEY, PAOLA (San Simón)

**Nota:** Hay traspasos bidireccionales entre Apatzingán y Nueva Italia, lo que indica compensación mutua de inventario. Ninguna sucursal está completamente surtida desde central.

### 3.4 Pedidos

**Formato:** PDF
**Origen:** DAMICH central realiza pedidos al proveedor (no son pedidos de sucursal a central).
**Contenido:** Concentrado de pedidos de las 3 sucursales combinadas.

---

## 4. Análisis del HTML — `modulo2_formularios.html`

### 4.1 Tabs / Módulos existentes

| Tab | Módulo | Descripción |
|---|---|---|
| 1 | Corte de Caja | Registro diario de cierre de caja |
| 2 | Traspaso | Transferencias de productos entre sucursales |
| 3 | Kileado | Ventas a granel o sueltas |
| 4 | Pedido | Solicitudes de productos |
| 5 | Historial | Listado y exportación CSV de la sesión |
| 6 | Guía | Instrucciones para el usuario |

### 4.2 Campos por módulo

#### Corte de Caja
- Tienda (select: Apatzingán / Nueva Italia / San Simón)
- Fecha (auto-hoy)
- Folio (número)
- Cajero (texto, default "CAJA")
- Ventas, Cobranza, Egresos, Crédito (montos)
- Declarado (monto)
- **Calculados automáticamente:** Ingresos = Ventas + Cobranza | Total = Ingresos - Egresos | Diferencia = Total - Declarado
- Observaciones

#### Traspaso
- Fecha (auto-hoy), Folio
- Folio Salida / Folio Entrada
- Origen / Destino (selects)
- Responsable
- Productos dinámicos (producto, cantidad, unidad: pzas/kg/lt/cajas/sacos)
- Observaciones

#### Kileado
- Tienda, Fecha
- Folio Entrada / Folio Salida
- Operador (select: ROSY / CECILIA V. / BRISEIDA D. / Otro)
- Producto, Cantidad, Tipo (K/S), Precio
- **Calculado:** Valor = Precio × Cantidad
- Observaciones

#### Pedido
- Tienda, Fecha
- Tipo (Alimento / Medicamento / Accesorio / Papelería / Otro)
- Urgencia (Normal / Urgente / Puede esperar)
- Productos dinámicos (producto, cantidad, unidad: sacos/pzas/kg/lt/cajas/dosis/tabs)
- Observaciones

#### Historial
- Filtros: por tipo de registro, por tienda
- Exportar CSV (timestamped, UTF-8 BOM para Excel)
- Vista en cards por registro

### 4.3 Lógica JavaScript

- Cálculo en tiempo real del corte de caja
- Color-code de la diferencia: verde (<$1) / rojo (<−$1) / naranja (otros)
- Validación de campos requeridos con mensajes inline
- Alertas auto-dismiss a 5 segundos
- Exportación CSV con 21 columnas estructuradas
- Datos en memoria (`registros[]`) — **se pierden al cerrar el navegador**

---

## 5. Gaps Identificados (HTML v1 → v2.0)

| # | Gap | Impacto | Prioridad |
|---|---|---|---|
| 1 | Kileado captura **1 producto por registro** — en operación real hay múltiples productos por folio | Alto | P1 |
| 2 | **Sin módulo de Egresos detallados** — solo monto total, sin categoría/concepto | Alto | P1 |
| 3 | **Sin módulo de Deudas / Cobranza parcial** — no hay registro de quién debe, cuánto, y pagos abonados | Alto | P1 |
| 4 | **Datos se pierden al cerrar navegador** — solo viven en RAM de sesión | Alto | P1 |
| 5 | **Sin clasificación de egresos** — gasolina, electricidad, sueldos, etc. son indistinguibles | Alto | P1 |
| 6 | Sin validación de folios duplicados | Medio | P2 |
| 7 | Sin campo de inventario inicial para cuadre | Medio | P2 |
| 8 | Operadores hardcodeados (si cambia personal, hay que editar el código) | Bajo | P3 |

---

## 6. Preguntas de Definición y Respuestas

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Los CSVs de Corte de Caja tienen totales por día de semana (todos los lunes juntos). ¿Es intencional? | **Sí, es intencional** en esta etapa |
| 2 | San Simón en Febrero tiene ventas 6x mayores que Enero. ¿Es correcto o error? | **Es correcto** |
| 3 | ¿Qué contienen los PDFs de pedidos? | **Pedidos de DAMICH central al proveedor** (concentrado de las 3 sucursales) |
| 4 | ¿Con qué frecuencia se envía la información? | **Diario** |
| 5 | ¿Hay registro de deudas de clientes? | **Sí** — se generan notas y sistema de **pagos parciales** |
| 6 | ¿Los egresos se detallan por concepto? | **Sí, se requiere clasificación general** (categorías) |
| 7 | ¿El HTML se usa en celular o computadora? | **Ambos** — intención principal: **celular**; también computadora |
| 8 | ¿Internet estable en sucursales? | **Apatzingán y Nueva Italia: estable** / **San Simón: inestable** |
| 9 | ¿Dónde correría el servidor? | **En Apatzingán** (sucursal central) |
| 10 | ¿El sistema necesita funcionar offline? | **HTML sí (por simplicidad)** / el servidor que importa CSVs puede tener internet |

---

## 7. Arquitectura Recomendada

### 7.1 Diagrama de flujo

```
[Sucursales]
  Apatzingán  → HTML Form → Export CSV → [Servidor local Apatzingán]
  Nueva Italia → HTML Form → Export CSV → (envío por WhatsApp/Drive)
  San Simón   → HTML Form → Export CSV → (envío por WhatsApp, offline-tolerant)
                                                    ↓
                                          [FastAPI Backend]
                                          ├── POST /import-csv    → parsea CSVs
                                          ├── GET  /reportes      → datos filtrados
                                          ├── GET  /pdf/{tipo}    → genera PDF
                                          └── SQLite              → persistencia local
                                                    ↓
                                          [Dashboard Web]
                                          └── HTML + JS puro
                                              ├── Filtros: sucursal / mes / tipo
                                              ├── Tablas de reportes
                                              └── Exportar PDF / CSV
```

### 7.2 Stack tecnológico

| Componente | Tecnología | Justificación |
|---|---|---|
| Backend API | **FastAPI (Python)** | Liviano, rápido, tipado, excelente para CSV/PDF |
| Procesamiento CSV | **Pandas** | Estándar para este tipo de trabajo |
| Base de datos | **SQLite** | Sin instalación de servidor, archivos locales |
| Generación PDF | **WeasyPrint** o **ReportLab** | HTML→PDF o programático |
| Frontend Dashboard | **HTML + JS puro** | Sin frameworks, consistente con el HTML actual |
| Formulario captura | **modulo2_formularios.html** (evolucionado) | Mantener lo que ya existe, agregar gaps |

### 7.3 Módulos del sistema (definitivos)

| Módulo | Tipo | Descripción |
|---|---|---|
| Captura — Corte de Caja | Form HTML | Registro diario con egresos categorizados |
| Captura — Traspaso | Form HTML | Transferencias multi-producto |
| Captura — Kileado | Form HTML | Multi-producto por folio |
| Captura — Egresos | Form HTML (nuevo) | Con clasificación: combustible / luz / sueldos / otros |
| Captura — Deudas / Cobranza | Form HTML (nuevo) | Cliente, monto total, abonos, saldo pendiente |
| Captura — Pedido | Form HTML | Solicitudes a central |
| Importador CSV | FastAPI | Lee y normaliza los CSVs exportados |
| Dashboard — Reportes | Web App | Filtros por sucursal / mes / semana / tipo |
| Generador PDF | FastAPI | Exporta reportes listos para presentar |
| Historial / Auditoría | Web App | Trazabilidad de registros |

---

## 8. Insights del Análisis de Datos

### 8.1 Patrones de venta identificados

- **El Lunes es el día de mayor venta** en las 3 sucursales consistentemente.
- **El Jueves es el día de menor venta** — también consistente en las 3.
- Oportunidad: planificar reposición de inventario los jueves / miércoles tarde.
- Oportunidad: campañas o promociones puntuales los jueves para levantar el valle.

### 8.2 Inventario y traspasos

- Existen traspasos **bidireccionales** entre Apatzingán y Nueva Italia.
- Esto indica que **ninguna sucursal está completamente surtida** desde central — se compensan mutuamente.
- Señal de falla en la planificación de inventario o pedidos irregulares.
- San Simón recibe traspasos pero no genera kileado → posible perfil de sucursal distribuidora/depósito.

### 8.3 Productos estrella

Basado en frecuencia de aparición en Kileado y Traspasos:

| Posición | Producto | Presencia |
|---|---|---|
| 1 | GATIMAR | Todas las sucursales, todos los meses |
| 2 | PRO-STAR | Alta frecuencia en Apa y NI |
| 3 | ENGORDA 5.5 | Mayor volumen en traspasos |
| 4 | KEY CAN | Regular en kileado |
| 5 | DESARROLLO 3.5 | Regular en traspasos NI ↔ Apa |
| 6 | PRO-FLOCK | Presente en kileado múltiple |
| 7 | CASTA BRAVA | Alta en traspasos NI → Apa |

### 8.4 Responsables operativos clave

| Persona | Sucursal | Rol operativo |
|---|---|---|
| BRISEIDA D. | Nueva Italia | Responsable principal de traspasos |
| CECILIA V. | Apatzingán | Responsable principal de traspasos |
| ROSY | Apatzingán | Operador de kileado |
| PAOLA | San Simón | Responsable de traspasos |

### 8.5 Prospectiva y lo que no vemos (aún)

- **Sin datos de márgenes:** Los CSVs muestran ventas declaradas pero no precio de compra → no se puede calcular rentabilidad por producto.
- **Sin datos de clientes:** No hay CRM — no sabemos quién compra más, con qué frecuencia, si hay clientes de alto valor.
- **Deudas sin sistema:** Las notas de deuda son manuales → riesgo de pérdida de información y falta de seguimiento.
- **Pedidos en PDF:** No hay estructura digital → no se pueden cruzar con ventas para calcular rotación.
- **San Simón en Febrero ($1.7M jueves):** Ese pico puntual merece investigación — ¿fue una venta especial, un evento, una feria?

---

## 9. Próximos Pasos

### Etapa 1 — HTML v2.0 (corto plazo)
- [ ] Agregar multi-producto en Kileado
- [ ] Agregar módulo de Egresos con categorías
- [ ] Agregar módulo de Deudas / Pagos parciales
- [ ] Persistencia con `localStorage` (datos sobreviven al cerrar)
- [ ] Validación de folios duplicados en sesión

### Etapa 2 — Backend FastAPI (mediano plazo)
- [ ] Importador de CSVs exportados desde el HTML
- [ ] Base de datos SQLite con esquema normalizado
- [ ] API de reportes con filtros (sucursal, mes, semana, tipo)
- [ ] Generación de PDFs de reportes

### Etapa 3 — Dashboard (mediano plazo)
- [ ] Vista consolidada por sucursal
- [ ] Comparativa mensual
- [ ] Top productos
- [ ] Estado de deudas y cobranza

---

## 10. Notas y Decisiones Pendientes

- [ ] Definir categorías exactas de egresos (lista con el cliente)
- [ ] Definir estructura de nota de deuda (campos: cliente, monto, fecha, abonos)
- [ ] Confirmar si San Simón necesita modo offline completo o solo tolerancia a intermitencias
- [ ] Revisar el pico de San Simón Febrero ($1.7M jueves) con el cliente
- [ ] Definir quién administra el servidor en Apatzingán y con qué SO corre

---

*Documento generado en sesión de análisis técnico — DAMICH / Consultoría Alimentos*
*Para actualizaciones futuras: incrementar número de versión y fecha en el encabezado.*
