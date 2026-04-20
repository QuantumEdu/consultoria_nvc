# MANUAL DE PROCEDIMIENTOS OPERATIVOS LIGEROS — NVC
## Versión 2.0 | Nutrición, Vacunas y Consultoría

---

| Campo | Detalle |
|------|---------|
| **Empresa** | NVC — Nutrición, Vacunas y Consultoría |
| **Documento** | Manual de Procedimientos Operativos Ligeros v2.0 |
| **Fecha** | 19 de abril de 2026 |
| **Elaboró** | Consultor Externo |
| **Estatus** | Borrador operativo — listo para piloto en matriz y 4 sucursales |
| **Revisión** | Mensual (primer trimestre), luego trimestral |

**Cambios en v2.0 (19/04/2026):** Fortalecimiento de procedimientos críticos (P01, P02, P06) para mayor ejecutabilidad en pilotos 30-60-90: (1) Tiempos máximos explícitos por paso; (2) Controles preventivos y umbrales de alerta; (3) Escalamiento detallado con tiempos límite; (4) KPIs con fórmulas, metas, frecuencia y acción correctiva; (5) Evidencia/registro mínimo requerido.

---

## 1. PROPÓSITO DEL DOCUMENTO

Definir los 10 procedimientos criticos de operacion (P01-P10) con un formato simple, repetible y facil de ejecutar para una empresa en crecimiento.

Este manual busca tres resultados:
- Reducir errores por improvisación entre sucursales
- Liberar tiempo operativo del Director General
- Asegurar control mínimo para escalar de 5 a 10 sucursales

Adicionalmente, cierra los faltantes detectados entre manuales, organizacion, funciones y sistemas con una logica de operacion ligera.

| Frente | Faltante detectado | Como se cubre en este manual |
|--------|---------------------|-------------------------------|
| Manuales | Procedimientos listados en plan, sin estandar de ejecucion | Fichas P01-P10 con entradas, pasos, salidas, KPI y riesgo-control |
| Organizacion | Sin secuencia formal para decidir cambios | Se incorpora seccion AS-IS/TO-BE y 3 puertas economicas |
| Funciones | Roles definidos, pero handoffs ambiguos | Matriz RACI transversal con responsable final por proceso |
| Sistemas | Politicas generales, sin rutina minima de control de datos | Anexo S1 de control operativo de sistemas y datos |

---

## 2. ENFOQUE ADMINISTRATIVO UTILIZADO (ISO 9001:2015 LIGERO)

NVC aplicará un enfoque de modernización administrativa inspirado en ISO 9001:2015, pero en versión ligera: control útil, cero burocracia innecesaria.

### 2.1 Principios aplicados

1. **Enfoque a procesos:** cada actividad crítica tiene dueño, entradas, salidas y métrica.
2. **Responsabilidad clara:** una persona responsable por resultado, aunque participen varias.
3. **Decisiones con datos:** KPI semanales y revisión mensual por excepción.
4. **Gestión de riesgos simple:** identificar fallas probables y su control preventivo.
5. **Mejora continua práctica (PDCA):** cambios cortos, medidos y documentados.

### 2.2 Qué SI se documenta (mínimo viable)

- Manual de Organización (estructura y políticas)
- Manual de Funciones (roles y KPIs)
- Este Manual de Procedimientos (P01-P10)
- Formatos maestros (caja, inventario, recepción, reporte semanal)
- Tablero de indicadores semanal
- Bitácora de incidencias y acciones correctivas

### 2.3 Qué NO se documenta (para evitar burocracia)

- Procedimientos de baja criticidad
- Reportes duplicados en papel y sistema
- Aprobaciones múltiples para tareas rutinarias
- Documentos extensos sin uso operativo

### 2.4 Ciclo de gobernanza ligero

- **Diario:** ejecución y registro operativo por sucursal
- **Semanal (viernes):** revisión de indicadores y desviaciones
- **Mensual:** ajustes de procedimiento, responsables y metas
- **Trimestral:** depuración documental (eliminar lo que no agrega valor)

### 2.5 Regla AS-IS -> TO-BE + 3 puertas economicas

Antes de digitalizar o escalar un proceso, NVC aplicara esta secuencia:

1. **AS-IS validado:** como opera hoy, con tiempos, errores y reprocesos reales.
2. **TO-BE simplificado:** menos pasos y menos dependencia del DG.
3. **Decision de implementacion:** solo si el caso economico es favorable.

Puertas economicas obligatorias:

| Puerta | Momento | Entregable minimo |
|-------|---------|-------------------|
| **Gate 1 - Discovery** | Antes del rediseño | Costo actual del problema (dinero, tiempo, mermas, cartera, ventas perdidas) |
| **Gate 2 - TO-BE** | Al validar el nuevo flujo | Beneficio esperado (ahorro + ingreso incremental) |
| **Gate 3 - Roadmap** | Antes de invertir | Business case: ROI, Payback, NPV y riesgos de adopcion |

Criterio recomendado de GO (alineado a reglas del framework):
- ROI > 50%
- Payback < 18 meses
- NPV > 0

---

## 3. MATRIZ RACI GENERAL (P01-P10)

| Rol | R en qué procedimientos | A en qué procedimientos | C | I |
|-----|-------------------------|-------------------------|---|---|
| Director General | P07 (compras estratégicas), P08 (casos críticos) | P07, revisión final de excepciones | Gerente Administrativa | Encargados |
| Gerente Administrativa | P06, P07, P09 | P06, P09 | DG, Responsable Logística y Cartera | Encargados |
| Responsable Logística y Cartera | P01, P05, P08, apoyo P07 | P01, P05 | Gerente Administrativa | DG |
| Encargado de sucursal | P02, P04, P09, P10 | P02, P04, P10 | Responsable Logística y Cartera | DG, Gerente Administrativa |
| Bodeguero / Auxiliar | P03, apoyo P02 y P08 | P03 | Encargado | Gerente Administrativa |
| Promotor de ventas | P05 | - | Encargado, Responsable Logística y Cartera | Gerente Comercial / DG |

Notas RACI:
- **R** = ejecuta, **A** = responde por el resultado.
- Si no existe gerente comercial formal, el DG asume validación de resultados comerciales.

---

## 4. PROCEDIMIENTOS OPERATIVOS

## P01 — CORTE DE CAJA DIARIO

**Objetivo:** cerrar ventas diarias con diferencia máxima tolerada de +/-1% del total de caja, mediante proceso estándar de 5 pasos con tiempos máximos.

**Alcance:** todas las sucursales, todos los turnos.

**Responsable (A):** Responsable de Logística y Cartera.
**Ejecutor (R):** cajero/a o encargado de sucursal.

**Entradas:**
- Tickets/ventas del día (MyBusiness report)
- Efectivo físico en caja (división por billetes, monedas)
- Transferencias bancarias confirmadas
- Notas de crédito pendientes
- Formato F-P01 en papel o digital

**Pasos críticos (máx. 5 pasos, tiempos máximos):**
1. **Cerrar ventas en MyBusiness** — <5 minutos (antes de iniciar conteo físico)
2. **Contar efectivo físico y clasificar** — <10 minutos (billetaje + monedas)
3. **Conciliar efectivo + transferencias vs sistema** — <10 minutos (validación automática)
4. **Registrar diferencia en Formato F-P01** — <5 minutos (si aplica, máximo 1 diferencia)
5. **Enviar evidencia (foto + captura) al grupo oficial** — <5 minutos (antes de 20:30 h)

**Salidas/Registros mínimos:**
- Formato F-P01 firmado (o digitalizado y firmado por la app)
- Evidencia de diferencias capturada (si aplica)
- Carpeta semanal con evidencias de cada sucursal

**KPIs mínimos (con metas y frecuencia):**

| KPI | Fórmula | Meta | Frecuencia | Acción correctiva si se incumple |
|-----|---------|------|------------|----------------------------------|
| **Exactitud de corte** | % cortes con diferencia ≤1% | ≥95% semanal | Semanal | 1. Revisar conteo físico con supervisión. 2. Capacitar equipo en billetaje. 3. Si <90% en 2 semanas, suspender turno hasta acondicionamiento. |
| **Tiempo de envío** | Tiempo entre cierre y envío de evidencia | <35 minutos | Semanal | 1. Corregir secuencia de pasos. 2. Automatizar foto con app. 3. Si >45 minutos en 2 turnos, ajustar distribución de turno. |
| **Cortes sin diferencia** | % cortes con diferencia 0% | ≥70% | Diario | 1. Analizar causas (errores de captura, faltantes, sobrantes). 2. Capacitación específica si >50% sin diferencia. |

**Controles preventivos y umbrales de alerta:**

| Nivel de alerta | Umbral | Acción inmediata | Responsable |
|-----------------|--------|------------------|-------------|
| **AMARILLO** | Diferencia 0.5% - 1% | Notificar a Responsable Logística y Cartera, planificar corrección en 48 h | Encargado de sucursal |
| **ROJO** | Diferencia >1% | Notificar Gerente Administrativa y DG antes de 21:00 h, iniciar investigación inmediata | Encargado + Cajero |
| **CRÍTICO** | Diferencia >3% o corte no enviado | Suspender turno del cajero, encender sirena de alerta en grupo oficial, investigar fraudes posiblemente | DG inmediatamente |

**Escalamiento y acciones correctivas:**

| Escenario | Tiempo límite de respuesta | Pasos de acción |
|-----------|---------------------------|-----------------|
| Diferencia >1% (ROJO) | <30 minutos de reporte | 1. Escalar al encargado (inmediato). 2. Si persiste >1h, escalar a Gerente Administrativa. 3. Investigación causa raíz en 24 h. 4. Acción correctiva planificada y comunicada en 48 h. |
| Corte no enviado antes de 20:30 h | <10 minutos de detectado | 1. Recordatorio en grupo oficial. 2. Si no se responde en 15 min, escalar a Responsable Logística y Cartera. 3. Ajuste en distribución de turno (inmediato). |
| Diferencia >3% (CRÍTICO) | <10 minutos de detectado | 1. Escalar a DG inmediatamente. 2. Iniciar investigación completa (billeteraje, captura, faltantes). 3. Acción correctiva definida y ejecutada en <24 h. 4. Reentrenamiento obligatorio del cajero (si aplica). |

**Riesgo y control:**
- **Riesgo:** omisión de ventas, faltantes por captura incorrecta, robo o malversación.
- **Control preventivo:** (1) Bloqueo de cierre sin conciliación automática; (2) Triple validación (efectivo + sistema + formato); (3) Evidencia digital obligatoria; (4) Umbral de alerta ROJO con DG inmediatamente.

---

## P02 — INVENTARIO DIARIO (A) Y SEMANAL (COMPLETO)

**Objetivo:** mantener exactitud de inventario físico vs sistema ≥97%, mediante inventario ABC (diario) y completo (semanal), con tiempos máximos por tipo de conteo.

**Alcance:** productos A (diario, todos los turnos) y todo el catálogo (semanal, viernes).

**Responsable (A):** encargado de sucursal.
**Ejecutor (R):** encargado + bodeguero.
**Validador (C):** Responsable Logística y Cartera (semanal).

**Entradas:**
- Lista ABC de productos críticos (actualizada cada semana)
- Existencias en MyBusiness (reporte de existencias)
- Conteo físico por productos A (diario)
- Conteo completo de inventario (semanal)
- Formato F-P02 en papel o digital

**Pasos críticos (con tiempos máximos):**

### Inventario Diario (Productos A) — Máx. 20 minutos:
1. **Actualizar lista ABC de productos A** — <5 minutos (cargar reporte de MyBusiness)
2. **Contar productos A al cierre de cada día** — <10 minutos (conteo rápido por categoría)
3. **Registrar diferencias inmediatas en Formato F-P02** — <5 minutos (si aplica)

### Inventario Semanal Completo — Máx. 60 minutos:
4. **Revisar reporte de MyBusiness** — <10 minutos
5. **Conteo físico completo** — <40 minutos (por producto, por categoría)
6. **Registrar diferencias en Formato F-P02** — <10 minutos

**Salidas/Registros mínimos:**
- F-P02 diario (productos A) + F-P02 semanal (todo inventario)
- Solicitud de ajuste de sistema (cuando aplique)
- Bitácora de diferencias por categoría (opcional)

**KPIs mínimos (con metas y frecuencia):**

| KPI | Fórmula | Meta | Frecuencia | Acción correctiva si se incumple |
|-----|---------|------|------------|----------------------------------|
| **Exactitud inventario** | (Conteo físico - Sistema) / Conteo físico × 100% | ≥97% | Semanal | 1. Revisar conteo ABC diario. 2. Capacitar en método de conteo. 3. Si <95% en 2 semanas, revisar sistema de inventario + capacitación intensiva. |
| **% diferencias investigadas en 24 h** | (Diferencias investigadas / Total diferencias) × 100% | 100% | Diario | 1. Registrar causa raíz de cada diferencia. 2. Si 0% en 2 días, capacitar en método de conteo. 3. Automatizar proceso si es repetitivo. |
| **Diferencias críticas (>5%)** | % productos con diferencia >5% | 0% | Semanal | 1. Escalar a Gerente Administrativa. 2. Investigación causa raíz completa (merma, captura, traspaso). 3. Acción correctiva definida y comunicada. 4. Si >1% de productos críticos, revisar calidad de mercancía. |
| **Inventario completo en tiempo** | % inventarios completados en viernes | 100% | Semanal | 1. Ajustar distribución de turnos si aplica. 2. Capacitar en método de conteo si exceden 60 minutos. 3. Si no se completa, escalar a Responsable Logística y Cartera. |

**Controles preventivos y umbrales de alerta:**

| Nivel de alerta | Umbral | Acción inmediata | Responsable |
|-----------------|--------|------------------|-------------|
| **AMARILLO** | Diferencia 0.5% - 1% (producto A) | Notificar a Responsable Logística y Cartera, planificar corrección en 48 h | Encargado |
| **ROJO** | Diferencia 1% - 3% (producto A) | Notificar Gerente Administrativa, investigar causa raíz en 24 h | Encargado |
| **CRÍTICO** | Diferencia >3% (producto A) o >5% (semanal) | Escalar a DG inmediatamente, suspender venta del producto hasta ajuste | Encargado + DG |

**Escalamiento y acciones correctivas:**

| Escenario | Tiempo límite de respuesta | Pasos de acción |
|-----------|---------------------------|-----------------|
| Diferencia 1% - 3% (ROJO) | <2 horas de detectado | 1. Escalar a Gerente Administrativa. 2. Investigación causa raíz en 24 h (captura, traspaso no registrado, mermas). 3. Acción correctiva planificada y comunicada en 48 h. 4. Capacitación si aplica. |
| Diferencia >3% - 5% (CRÍTICO) | <1 hora de detectado | 1. Escalar a DG inmediatamente. 2. Suspender venta del producto hasta ajuste. 3. Investigación completa en 24 h. 4. Acción correctiva definida en <48 h. 5. Reentrenamiento obligatorio si aplica. |
| Inventario no completado en viernes | <10 minutos de detectado | 1. Escalar a Responsable Logística y Cartera. 2. Ajustar distribución de turno (inmediato). 3. Si no se completa en 2 semanas, revisar proceso completo. |
| Exactitud <95% en 2 semanas | <1 día de detectado | 1. Escalar a Gerente Administrativa. 2. Revisar método de conteo ABC. 3. Capacitación intensiva en 3 días. 4. Re-conteo pilot en 1 semana. |

**Riesgo y control:**
- **Riesgo:** sobrestock (inventario alto sin rotación), quiebres (stock bajo sin anticipación), captura incorrecta.
- **Control preventivo:** (1) Inventario ABC diario para productos críticos; (2) Conteo completo semanal para todos los productos; (3) Umbral de alerta ROJO con suspensión de venta si aplica; (4) Ajuste de sistema con autorización explícita; (5) Revisión semanal por Responsable Logística y Cartera.

---

## P03 — RECEPCION DE MERCANCIA

**Objetivo:** asegurar que toda mercancia recibida coincida con orden de compra y factura.

**Alcance:** todas las recepciones de proveedores en matriz y sucursales.

**Responsable (A):** bodeguero lider o encargado de sucursal.
**Ejecutor (R):** bodeguero / auxiliar.

**Entradas:** orden de compra, factura proveedor, guia/remision, espacio de descarga.

**Pasos:**
1. Verificar datos de proveedor, fecha y numero de orden.
2. Contar bultos y revisar estado fisico de empaque.
3. Comparar cantidades recibidas vs orden y factura.
4. Registrar faltantes/sobrantes/danos en F-P03.
5. Solicitar firma de entrega al transportista y responsable de recepcion.
6. Capturar recepcion en MyBusiness el mismo dia.
7. Escalar discrepancias relevantes a Gerente Administrativa en menos de 2 h.

**Salidas/Registros:** F-P03 firmado, evidencia fotografica, entrada de almacen en sistema.

**KPI:**
- % recepciones registradas el mismo dia (meta: 100%)
- % discrepancias cerradas <48 h (meta: 95%)

**Riesgo y control:** pagos por mercancia no recibida; control: triple validacion OC-factura-fisico.

---

## P04 — ATENCION AL CLIENTE EN MOSTRADOR

**Objetivo:** estandarizar atencion para aumentar conversion y evitar perdida de clientes.

**Alcance:** atencion presencial en todas las sucursales.

**Responsable (A):** encargado de sucursal.
**Ejecutor (R):** vendedor/cajero/encargado.

**Entradas:** protocolo comercial, catalogo actualizado, politicas de precio y credito.

**Pasos:**
1. Recibir al cliente en menos de 1 minuto.
2. Levantar necesidad: producto, especie, volumen, urgencia.
3. Recomendar opcion tecnica/comercial adecuada.
4. Verificar stock y condiciones de venta en sistema.
5. Cerrar venta con registro obligatorio en MyBusiness.
6. Ofrecer seguimiento tecnico/comercial cuando aplique.
7. Registrar cliente nuevo o actualizar datos de contacto.

**Salidas/Registros:** ticket/factura, alta/actualizacion de cliente, observacion de atencion.

**KPI:**
- Tiempo de atencion inicial (meta: <1 min)
- Tasa de conversion mostrador (meta inicial: >=70%)

**Riesgo y control:** fuga por mala atencion; control: guion base + capacitacion mensual breve.

---

## P05 — SEGUIMIENTO POST-VENTA Y RECUPERACION

**Objetivo:** retener clientes activos y recuperar clientes inactivos (>30 dias sin compra).

**Alcance:** cartera comercial por sucursal y clientes de campo.

**Responsable (A):** Responsable Logistica y Cartera.
**Ejecutor (R):** promotor de ventas + encargado.

**Entradas:** reporte de clientes, historial de compras, lista de inactivos.

**Pasos:**
1. Generar lista semanal de clientes top e inactivos.
2. Definir ruta de llamadas/mensajes/visitas.
3. Contactar cliente con guion: seguimiento, satisfaccion y nueva necesidad.
4. Registrar compromiso comercial en F-P05.
5. Escalar casos tecnicos al promotor tecnico o DG.
6. Dar cierre semanal con estatus: recuperado, en seguimiento, perdido.

**Salidas/Registros:** F-P05, lista de recuperacion, resumen semanal comercial.

**KPI:**
- Clientes recuperados por mes (meta inicial: +10)
- % clientes top con contacto semanal (meta: 100%)

**Riesgo y control:** perdida silenciosa de cartera; control: semaforo semanal de inactivos.

---

## P06 — FACTURACIÓN Y CONCILIACIÓN (MYBUSINESS VS CONTPAQ)

**Objetivo:** asegurar integridad fiscal-contable y cero rezago en conciliaciones mediante emisión inmediata de CFDI y conciliación semanal, con tiempos máximos por fase.

**Alcance:** ventas, facturación CFDI y conciliación contable en matriz y sucursales.

**Responsable (A/R):** Gerente Administrativa.
**Validador (C):** Responsable Logística y Cartera (mensual).
**Aprueba (I):** Director General (si hay incidencia fiscal crítica).

**Entradas:**
- Ventas diarias en MyBusiness
- CFDI emitidos (XML y PDF)
- Reporte de ventas consolidado (semanal)
- Pólizas de CONTPAQ
- Formato F-P06 en papel o digital

**Pasos críticos (con tiempos máximos):**

### Emisión de Facturación — Máx. 20 minutos por día:
1. **Emitir facturación pendiente el mismo día de la venta** — <10 minutos (por turno, si aplica)
2. **Revisar cancelaciones y sustituciones CFDI autorizadas** — <5 minutos
3. **Registrar emisiones en MyBusiness y CONTPAQ** — <5 minutos

### Conciliación Semanal — Máx. 60 minutos:
4. **Consolidar reporte semanal de ventas y facturas** — <15 minutos (MyBusiness + CONTPAQ)
5. **Conciliar semanalmente MyBusiness vs CONTPAQ** — <30 minutos (cross-check)
6. **Registrar diferencias y plan de corrección en F-P06** — <15 minutos

**Salidas/Registros mínimos:**
- F-P06 de conciliación semanal
- Reporte de conciliación semanal (formato digital)
- Evidencias fiscales (XML y PDF de CFDI)
- Bitácora de diferencias y acciones correctivas

**KPIs mínimos (con metas y frecuencia):**

| KPI | Fórmula | Meta | Frecuencia | Acción correctiva si se incumple |
|-----|---------|------|------------|----------------------------------|
| **% facturas emitidas el mismo día** | (Facturas emitidas el día de la venta / Total ventas del día) × 100% | 100% | Diario | 1. Revisar flujo de emisión (captura, autorización). 2. Capacitar en método de emisión. 3. Si <95% en 2 días, escalado a Gerente Administrativa. |
| **Rezago de conciliación** | (Fecha de conciliación - Fecha de venta) | ≤7 días | Semanal | 1. Revisar proceso de conciliación. 2. Automatizar reporte si es manual. 3. Si >10 días en 2 semanas, escalado a DG. |
| **Diferencias de conciliación** | % de ventas no conciliadas | ≤5% | Semanal | 1. Investigar causa raíz (captura, traspaso, error de sistema). 2. Plan de corrección definido en 24 h. 3. Si >10% en 2 semanas, revisar proceso completo. |
| **Cancelaciones sin sustitución** | (CFDI cancelados - CFDI sustituidos) | 0 | Diario | 1. Revisar autorización de cancelaciones. 2. Capacitar en método de sustitución. 3. Si >2 cancelaciones sin sustitución en 1 semana, revisar política. |

**Controles preventivos y umbrales de alerta:**

| Nivel de alerta | Umbral | Acción inmediata | Responsable |
|-----------------|--------|------------------|-------------|
| **AMARILLO** | Facturas no emitidas el mismo día (5% - 10%) | Notificar a Responsable Logística y Cartera, planificar corrección en 48 h | Gerente Administrativa |
| **ROJO** | Facturas no emitidas el mismo día (>10%) o rezago >7 días | Notificar DG inmediatamente, investigar causa raíz en 24 h | Gerente Administrativa |
| **CRÍTICO** | Diferencias de conciliación >5% o rezago >14 días | Escalar a DG inmediatamente, iniciar investigación fiscal | Gerente Administrativa + DG |

**Escalamiento y acciones correctivas:**

| Escenario | Tiempo límite de respuesta | Pasos de acción |
|-----------|---------------------------|-----------------|
| Facturas no emitidas el mismo día (>10%) | <2 horas de detectado | 1. Revisar flujo de emisión. 2. Capacitar en método de emisión. 3. Acción correctiva planificada y ejecutada en 24 h. 4. Monitoreo diario en 3 días. |
| Rezago de conciliación >7 días | <1 día de detectado | 1. Escalar a Responsable Logística y Cartera. 2. Revisar proceso manual vs automático. 3. Automatizar si es posible. 4. Si >10 días en 2 semanas, escalado a DG. |
| Diferencias de conciliación >5% | <24 horas de detectado | 1. Investigar causa raíz (captura, traspaso, error de sistema). 2. Plan de corrección definido en 24 h. 3. Ejecutar en 48 h. 4. Capacitación si aplica. |
| Rezago >14 días (CRÍTICO) | <10 minutos de detectado | 1. Escalar a DG inmediatamente. 2. Iniciar investigación fiscal completa. 3. Acción correctiva definida en 24 h. 4. Reentrenamiento obligatorio si aplica. 5. Revisión mensual por DG. |

**Riesgo y control:**
- **Riesgo:** contingencia fiscal (facturas no emitidas, diferencias no resueltas, cancelaciones sin sustitución).
- **Control preventivo:** (1) Emisión inmediata de CFDI el mismo día de la venta; (2) Conciliación semanal obligatoria; (3) Umbral de alerta ROJO con DG inmediatamente si aplica; (4) Registro de diferencias y acciones correctivas; (5) Validación mensual por Responsable Logística y Cartera.

---

## P07 — PEDIDOS Y COMPRAS

**Objetivo:** abastecer sin sobreinventario, con flujo de autorizacion claro y rapido.

**Alcance:** compras rutinarias y especiales de todas las sucursales.

**Responsable (A):** Gerente Administrativa.
**Aprobador final:** Director General (cuando supere umbral o sea proveedor nuevo).
**Ejecutor (R):** Responsable Logistica y Cartera + Gerente Administrativa.

**Entradas:** reporte de faltantes, minimo-maximo, cartera pendiente, presupuesto.

**Pasos:**
1. Encargados envian faltantes en formato estandar cada jueves.
2. Responsable Logistica consolida necesidades por sucursal.
3. Gerente Administrativa valida inventario, rotacion y flujo de efectivo.
4. Si compra es rutinaria y dentro de umbral, autoriza Gerente Administrativa.
5. Si compra excede umbral o es no rutinaria, solicita autorizacion DG.
6. Emitir orden de compra y confirmar fecha de entrega.
7. Monitorear cumplimiento de proveedor y registrar incidencias.

**Salidas/Registros:** OC emitida, matriz de seguimiento de compras, incidencias proveedor.

**KPI:**
- Fill rate de compra (meta: >=95%)
- Quiebres de stock por sucursal (meta: <=2 por semana)

**Riesgo y control:** compra reactiva sin criterio; control: ciclo semanal fijo + umbrales de autorizacion.

---

## P08 — LOGISTICA Y ENTREGAS

**Objetivo:** cumplir entregas completas, a tiempo y con cobro trazable.

**Alcance:** entregas locales y regionales de productos.

**Responsable (A):** Responsable Logistica y Cartera.
**Ejecutor (R):** repartidores y apoyo de sucursal.

**Entradas:** pedidos confirmados, ruta diaria, unidad asignada, politicas de cobro.

**Pasos:**
1. Consolidar pedidos por ruta y prioridad (horario/zona).
2. Validar carga fisica contra remision antes de salida.
3. Ejecutar ruta con bitacora de tiempos y entregas.
4. Cobrar segun condicion pactada (contado/credito autorizado).
5. Registrar evidencia de entrega y cobro (firma/foto/transferencia).
6. Reportar entregas no completadas el mismo dia.
7. Cerrar ruta con conciliacion de documentos y valores.

**Salidas/Registros:** bitacora de ruta F-P08, remisiones firmadas, comprobantes de cobro.

**KPI:**
- OTIF (entrega completa y a tiempo) meta inicial: >=92%
- % cobros conciliados mismo dia (meta: 100%)

**Riesgo y control:** fuga de efectivo y entregas sin evidencia; control: cierre diario de ruta.

---

## P09 — GESTION DE PERMISOS Y ASISTENCIA

**Objetivo:** ordenar asistencia y permisos con criterio uniforme entre sucursales.

**Alcance:** todo el personal operativo y administrativo.

**Responsable (A):** Gerente Administrativa.
**Ejecutor (R):** encargados de sucursal.

**Entradas:** registro de asistencia, solicitudes de permiso, politicas vigentes.

**Pasos:**
1. Registrar entrada/salida diaria en libro o app autorizada.
2. Recibir solicitud de permiso con causa y fecha.
3. Autorizar segun politica (encargado <=1 dia, DG >1 dia).
4. Notificar resolucion al colaborador y a Administracion.
5. Actualizar incidencias de nomina semanalmente.
6. Escalar reincidencias de retardos/faltas al DG.

**Salidas/Registros:** bitacora asistencia, formato permiso F-P09, reporte de incidencias.

**KPI:**
- % asistencia registrada correctamente (meta: 100%)
- Tasa de ausentismo mensual (meta inicial: <=4%)

**Riesgo y control:** conflictos laborales y nomina inexacta; control: registro diario obligatorio.

---

## P10 — REPORTE SEMANAL DE SUCURSAL

**Objetivo:** estandarizar comunicacion de resultados para toma de decisiones rapida.

**Alcance:** todas las sucursales, cada semana.

**Responsable (A):** encargado de sucursal.
**Revisor:** Gerente Administrativa + DG.

**Entradas:** ventas, cartera, inventario, incidencias operativas, acciones comerciales.

**Pasos:**
1. Consolidar indicadores semanales en formato unico F-P10.
2. Reportar semaforo por rubro: verde/amarillo/rojo.
3. Anotar causas de desvio y accion correctiva propuesta.
4. Enviar reporte al grupo oficial antes de viernes 12:00 h.
5. Presentar puntos criticos en reunion semanal de KPIs.
6. Cerrar acuerdos con responsable y fecha compromiso.

**Salidas/Registros:** F-P10 por sucursal, minuta de acuerdos semanales.

**KPI:**
- % reportes enviados en tiempo (meta: 100%)
- % acuerdos cerrados en fecha (meta: >=85%)

**Riesgo y control:** decisiones tardias por falta de datos; control: formato unico y hora limite.

---

## ANEXO S1 — CONTROL OPERATIVO DE SISTEMAS Y DATOS

**Objetivo:** asegurar continuidad operativa y trazabilidad minima de la informacion.

**Alcance:** MyBusiness, CONTPAQ, respaldos, accesos y catalogos maestros por sucursal.

**Responsable (A):** Gerente Administrativa.
**Ejecutor (R):** Responsable Logistica y Cartera + encargado de sucursal.

**Entradas:** altas/bajas de personal, cambios de catalogo, bitacora de incidencias, estado de respaldo.

**Pasos:**
1. Alta/baja de usuarios solo por solicitud autorizada y folio de control.
2. Respaldo diario automatico y validacion semanal de restauracion de prueba.
3. Cambios de precio/catalogo solo por rol autorizado (sin cuentas compartidas).
4. Registro de incidente con causa, impacto, accion y tiempo de resolucion.
5. Cierre semanal de salud del sistema en formato F-S1.

**Salidas/Registros:** bitacora de accesos, check de respaldos, registro de incidentes, reporte F-S1.

**KPI:**
- % respaldos diarios exitosos (meta: 100%)
- Incidentes criticos abiertos >48 h (meta: 0)

**Riesgo y control:** perdida de datos o operacion sin trazabilidad; control: restauracion semanal de prueba + segregacion de accesos.

---

## 5. FORMATOS MAESTROS MINIMOS

Para operar este manual, NVC solo necesita 8 formatos:

1. **F-P01** Corte de caja diario
2. **F-P02** Inventario diario/semanal
3. **F-P03** Recepcion de mercancia
4. **F-P05** Seguimiento y recuperacion de clientes
5. **F-P06** Conciliacion MyBusiness vs CONTPAQ
6. **F-P08** Bitacora de ruta y entrega
7. **F-P10** Reporte semanal de sucursal
8. **F-S1** Control semanal de sistemas y datos

Regla de simplificacion:
- Si un dato ya existe en MyBusiness, no duplicarlo en otro formato.

---

## 6. REGLAS DE CONTROL DOCUMENTAL LIGERO

- Un documento por proceso critico; no duplicados por sucursal.
- Versionado por fecha en nombre del archivo y tabla interna.
- Cambios se prueban 2 semanas en piloto antes de estandarizar.
- Cada procedimiento debe poder explicarse en menos de 10 minutos.

---

## 7. IMPLEMENTACION SUGERIDA (30 DIAS)

| Semana | Foco | Entregable |
|-------|------|------------|
| 1 | P01, P02, P03, P09 | Control base de caja, inventario, recepcion y asistencia |
| 2 | P04, P05, P10 | Control comercial y reporte semanal estandar |
| 3 | P06, P07 | Orden administrativo-fiscal y compras |
| 4 | P08 + S1 + ajuste general | Logistica cerrada, control de sistemas activo y version estabilizada |

---

## 8. VIGENCIA Y ACTUALIZACION

| Campo | Detalle |
|------|---------|
| **Version** | 1.1 |
| **Fecha de emision** | 19 de abril de 2026 |
| **Proxima revision** | 19 de julio de 2026 |
| **Custodio** | Gerente Administrativa |
| **Aprobo** | Director General |

### Historial de versiones

| Version | Fecha | Cambios | Elaboro |
|--------|-------|---------|---------|
| 2.0 | 19/04/2026 | Fortalecimiento de procedimientos críticos (P01, P02, P06) para pilotos 30-60-90: tiempos máximos por paso, controles preventivos, umbrales de alerta, escalas de acción, KPIs con fórmulas/metas/frecuencia/acción correctiva, evidencia mínima. Ajuste de estatus a "listo para piloto". | Consultor Externo |
| 1.1 | 19/04/2026 | Se agregan: cobertura de faltantes por frente (manuales/organizacion/funciones/sistemas), gobernanza AS-IS/TO-BE con 3 puertas economicas y Anexo S1 de control operativo de sistemas y datos | Consultor Externo |
| 1.0 | 19/04/2026 | Creacion inicial de procedimientos P01-P10 bajo enfoque ISO 9001:2015 ligero | Consultor Externo |

---

*NVC — Manual de Procedimientos Operativos Ligeros v1.1 | Consultoria Externa | Confidencial*
