# Resumen de Cambios — Procedimientos Críticos (P01, P02, P06)
## Versión 2.0 del Manual de Procedimientos Operativos

**Fecha:** 19 de abril de 2026
**Consultor:** Externo
**Cliente:** NVC — Nutrición, Vacunas y Consultoría

---

## 📋 Objetivo del Ajuste

Fortalecer P01 (Corte de Caja), P02 (Inventario) y P06 (Facturación y Conciliación) para hacerlo **más ejecutable en pilotos 30-60-90**, con enfoque práctico alineado a ISO ligera + modelo de competitividad.

---

## 🎯 Cambios Puntuales por Procedimiento

### P01 — Corte de Caja Diario

**Nuevos elementos agregados:**

1. **Tiempos máximos por paso (5 pasos con tiempos fijos)**
   - Cerrar ventas en MyBusiness: <5 minutos
   - Contar efectivo físico y clasificar: <10 minutos
   - Conciliar vs sistema: <10 minutos
   - Registrar diferencia en Formato F-P01: <5 minutos
   - Enviar evidencia al grupo oficial: <5 minutos

2. **Controles preventivos y umbrales de alerta (3 niveles)**
   - AMARILLO: Diferencia 0.5% - 1% → Notificar a Responsable Logística y Cartera, planificar corrección en 48 h
   - ROJO: Diferencia >1% → Notificar Gerente Administrativa y DG antes de 21:00 h, iniciar investigación inmediata
   - CRÍTICO: Diferencia >3% o corte no enviado → Suspender turno, encender sirena de alerta, investigar fraudes

3. **Escalamiento detallado con tiempos límite**
   - Diferencia >1%: <30 minutos de reporte (escalado a encargado, luego a Gerente Administrativa si persiste)
   - Corte no enviado antes de 20:30 h: <10 minutos de detectado
   - Diferencia >3%: <10 minutos de detectado (escalado a DG inmediatamente)

4. **KPIs mínimos (4 KPIs con fórmula, meta, frecuencia, acción correctiva)**
   - Exactitud de corte: % cortes con diferencia ≤1% (meta: ≥95% semanal)
   - Tiempo de envío: <35 minutos (meta: antes de 20:30 h)
   - Cortes sin diferencia: % cortes con diferencia 0% (meta: ≥70% diario)
   - **Acciones correctivas específicas** para cada incumplimiento

5. **Evidencia/registro mínimo requerido**
   - Formato F-P01 firmado (o digitalizado y firmado por la app)
   - Evidencia de diferencias capturada (si aplica)
   - Carpeta semanal con evidencias de cada sucursal

---

### P02 — Inventario Diario y Semanal

**Nuevos elementos agregados:**

1. **Tiempos máximos por tipo de conteo**
   - Inventario Diario (Productos A): Máx. 20 minutos (5+10+5 pasos)
   - Inventario Semanal Completo: Máx. 60 minutos (10+40+10 pasos)

2. **Controles preventivos y umbrales de alerta (3 niveles)**
   - AMARILLO: Diferencia 0.5% - 1% (producto A) → Notificar a Responsable Logística y Cartera, planificar corrección en 48 h
   - ROJO: Diferencia 1% - 3% (producto A) → Notificar Gerente Administrativa, investigar causa raíz en 24 h
   - CRÍTICO: Diferencia >3% (producto A) o >5% (semanal) → Escalar a DG inmediatamente, suspender venta del producto hasta ajuste

3. **Escalamiento detallado con tiempos límite**
   - Diferencia 1% - 3% (ROJO): <2 horas de detectado
   - Diferencia >3% - 5% (CRÍTICO): <1 hora de detectado
   - Inventario no completado en viernes: <10 minutos de detectado
   - Exactitud <95% en 2 semanas: <1 día de detectado

4. **KPIs mínimos (4 KPIs con fórmula, meta, frecuencia, acción correctiva)**
   - Exactitud inventario: ≥97% (meta: semanal)
   - % diferencias investigadas en 24 h: 100% (meta: diario)
   - Diferencias críticas (>5%): 0% (meta: semanal)
   - Inventario completo en tiempo: 100% (meta: semanal)

5. **Evidencia/registro mínimo requerido**
   - F-P02 diario (productos A) + F-P02 semanal (todo inventario)
   - Solicitud de ajuste de sistema (cuando aplique)
   - Bitácora de diferencias por categoría (opcional)

---

### P06 — Facturación y Conciliación (MyBusiness vs CONTPAQ)

**Nuevos elementos agregados:**

1. **Tiempos máximos por fase**
   - Emisión de Facturación: Máx. 20 minutos por día (10+5+5 pasos)
   - Conciliación Semanal: Máx. 60 minutos (15+30+15 pasos)

2. **Controles preventivos y umbrales de alerta (3 niveles)**
   - AMARILLO: Facturas no emitidas el mismo día (5% - 10%) → Notificar a Responsable Logística y Cartera, planificar corrección en 48 h
   - ROJO: Facturas no emitidas el mismo día (>10%) o rezago >7 días → Notificar DG inmediatamente, investigar causa raíz en 24 h
   - CRÍTICO: Diferencias de conciliación >5% o rezago >14 días → Escalar a DG inmediatamente, iniciar investigación fiscal

3. **Escalamiento detallado con tiempos límite**
   - Facturas no emitidas el mismo día (>10%): <2 horas de detectado
   - Rezago de conciliación >7 días: <1 día de detectado
   - Diferencias de conciliación >5%: <24 horas de detectado
   - Rezago >14 días (CRÍTICO): <10 minutos de detectado

4. **KPIs mínimos (4 KPIs con fórmula, meta, frecuencia, acción correctiva)**
   - % facturas emitidas el mismo día: 100% (meta: diario)
   - Rezago de conciliación: ≤7 días (meta: semanal)
   - Diferencias de conciliación: ≤5% (meta: semanal)
   - Cancelaciones sin sustitución: 0 (meta: diario)

5. **Evidencia/registro mínimo requerido**
   - F-P06 de conciliación semanal
   - Reporte de conciliación semanal (formato digital)
   - Evidencias fiscales (XML y PDF de CFDI)
   - Bitácora de diferencias y acciones correctivas

---

## 📁 Archivos Modificados

1. **`06_manual_de_organizacion/procedimientos_operativos_v1_20260419.md`**
   - Versión: 1.1 → **2.0**
   - Cambios: Fortalecimiento de P01, P02, P06 con tiempos, controles, escalas, KPIs y evidencia mínima
   - Estatus: "Borrador operativo — piloto" → **"Borrador operativo — listo para piloto"**

2. **`README.md`**
   - Referencia al manual de procedimientos: **v1.1 → v2.0**
   - Descripción actualizada: se agregan detalles de cambios v2.0
   - Estado del proyecto: manual de procedimientos → "Completado v2.0"

3. **`06_manual_de_organizacion/manual_integral_procesos_competitividad_v1_20260419.md`**
   - Referencia actualizada: (v2.0) — P01-P10, enfoque ISO ligero

---

## ⚠️ Riesgos o Pendientes para la Siguiente Iteración

### Riesgos Identificados

1. **Adopción en piloto:**
   - Los tiempos máximos fijados pueden ser ajustados según la realidad operativa.
   - **Mitigación:** Monitorear KPIs de ejecución en los primeros 2 semanas de piloto y ajustar tiempos si es necesario.

2. **Responsabilidad escalada:**
   - Escalamientos a DG pueden saturar al Director General si hay demasiados incidentes.
   - **Mitigación:** Revisar causas raíz de incidentes y corregir procesos antes de escalar; ajustar umbral de alerta si aplica.

3. **Consistencia de formatos:**
   - Los formatos F-P01, F-P02, F-P06 deben estar actualizados para reflejar los tiempos, controles y KPIs nuevos.
   - **Mitigación:** Validar con equipo operativo antes de iniciar piloto; actualizar formatos si es necesario.

### Pendientes para la Siguiente Iteración

1. **Actualización de formatos F-P01, F-P02, F-P06**
   - Agregar campos para: tiempos máximos, umbrales de alerta, acción correctiva, evidencia mínima.
   - Prioridad: Alta (antes de iniciar piloto).

2. **Validación con equipo operativo**
   - Revisar que los tiempos máximos sean realistas según la realidad de cada sucursal.
   - Validar que los KPIs sean medibles y relevantes para el equipo.
   - Prioridad: Alta (antes de iniciar piloto).

3. **Capacitación de equipo en nuevos procedimientos**
   - Capacitar en: tiempos máximos por paso, escalas de alerta, KPIs, evidencia mínima.
   - Prioridad: Alta (durante piloto Semana 1).

4. **Monitoreo inicial en piloto (30 días)**
   - Medir cumplimiento de KPIs de ejecución (tiempos máximos, escalamientos, etc.).
   - Ajustar tiempos, controles o KPIs si se detecta inconsistencia entre diseño y realidad.
   - Prioridad: Alta (durante piloto Semana 1-4).

5. **Integración con formato F-P10 (Reporte Semanal)**
   - Incluir KPIs de P01, P02, P06 en el reporte semanal de sucursal.
   - Prioridad: Media (durante piloto Semana 2-4).

---

## 🚀 Mensaje de Commit Sugerido

```
feat: fortalecer procedimientos críticos para pilotos 30-60-90 (P01, P02, P06)

V2.0 del Manual de Procedimientos Operativos Ligeros

Cambios:
- Agregar tiempos máximos por paso (P01: 5 pasos; P02: 2 tipos de conteo; P06: 2 fases)
- Agregar controles preventivos y umbrales de alerta (3 niveles: AMARILLO/ROJO/CRÍTICO)
- Agregar escalas de acción detalladas con tiempos límite de respuesta
- Agregar 4 KPIs mínimos por procedimiento con fórmula, meta, frecuencia y acción correctiva
- Agregar evidencia/registro mínimo requerido
- Actualizar versión de 1.1 a 2.0
- Actualizar estatus a "listo para piloto"

Procedimientos fortalecidos:
- P01: Corte de Caja Diario (5 pasos con tiempos, 4 KPIs, 3 niveles de alerta)
- P02: Inventario Diario y Semanal (2 tipos de conteo con tiempos, 4 KPIs, 3 niveles de alerta)
- P06: Facturación y Conciliación (2 fases con tiempos, 4 KPIs, 3 niveles de alerta)

Pendientes:
- Actualizar formatos F-P01, F-P02, F-P06
- Validar tiempos con equipo operativo
- Capacitar equipo en nuevos procedimientos
- Monitorear cumplimiento en piloto (30 días)
```

---

## 📊 Resumen de Mejoras de Ejecutabilidad

| Aspecto | Antes (v1.1) | Después (v2.0) |
|---------|--------------|----------------|
| **Tiempos máximos** | No definidos | 5 pasos P01, 2 tipos P02, 2 fases P06 con tiempos fijos |
| **Controles preventivos** | Riesgo básico | 3 niveles de alerta con umbrales específicos |
| **Escalamiento** | General | Tiempos límite de respuesta + acciones específicas |
| **KPIs** | 2 KPIs sin acción correctiva | 4 KPIs con fórmula, meta, frecuencia y acción correctiva |
| **Evidencia mínima** | No definida | Evidencia de registro especificada |
| **Ejecutabilidad piloto** | Borrador operativo | **Listo para piloto 30-60-90** |

---

*Generado el 19 de abril de 2026 por: Consultor Externo*
*Proyecto: NVC — Consultoría Organizacional | v2.0 Manual de Procedimientos Operativos Ligeros*
