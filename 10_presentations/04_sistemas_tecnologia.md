# MÓDULO 04 — Sistemas y Tecnología
## NVC — Nutrición, Vacunas y Consultoría

---

<!-- DIAPOSITIVA 1: PORTADA MÓDULO -->
# Tema: Sistemas | Diapositiva 1
## MyBusiness 2017 — Análisis y Hoja de Ruta

![Logo NVC](./logo_nvc.jpg)

**Análisis Técnico v2.0 | Abril 2026**

> *"El problema no siempre es el sistema. A veces es la disciplina de captura."*

---

<!-- DIAPOSITIVA 2: EL ECOSISTEMA ACTUAL -->
# Tema: Sistemas | Diapositiva 2
## El ecosistema tecnológico de NVC hoy

```
┌─────────────────────────────────────────┐
│          MyBusiness 2017                 │
│   POS · Inventario · Facturación CFDI   │
│   Cobranza · Cuentas por Pagar          │
└──────────────────┬──────────────────────┘
                   │ AnyDesk (soporte remoto)
┌──────────────────┴──────────────────────┐
│         MyNube / POS Tools              │
│   Concentrador multi-sucursal (nube)    │
└──────────────────┬──────────────────────┘
                   │
     ┌─────────────┼─────────────┐
     │             │             │
[Apatzingán] [San Simón] [Nueva Italia]
 BD Local     BD Local    BD Local
```

**+ CONTPAQ** (contabilidad, con contador externo)
**+ WhatsApp** (reportes diarios y cortes)
**+ Excel** (gastos diarios, concentrado de cortes)

---

<!-- DIAPOSITIVA 3: QUÉ HACE MYBUSINESS EN NVC -->
# Tema: Sistemas | Diapositiva 3
## Qué hace MyBusiness en NVC

| Módulo | Estado | Uso real |
|--------|--------|---------|
| ✅ Punto de Venta | Activo | Ventas en mostrador todas las sucursales |
| ✅ Facturación CFDI | Activo | Facturas emitidas por Rossy |
| ✅ Cuentas por Cobrar | Activo | Nueva Italia |
| ✅ Cuentas por Pagar | Activo | Apatzingán (compras a crédito) |
| ✅ Inventario (Almacén 1) | Activo | Cada sucursal tiene su propio almacén |
| ✅ Traspasos entre sucursales | Activo | **Manual — con errores frecuentes** |
| ✅ Corte Z | Activo | Cada tienda genera su propio corte |
| ✅ Concentrador MyNube | Activo | Dashboard de cortes consolidado |
| ⚠️ Módulo gastos adicionales | **No se usa** | Se lleva en Excel |
| ⚠️ Cobranza sistemática | **Parcial** | Depósitos no siempre se capturan |

---

<!-- DIAPOSITIVA 4: ARQUITECTURA MULTI-SUCURSAL -->
# Tema: Sistemas | Diapositiva 4
## Arquitectura multi-sucursal — Cómo funciona

**Cada sucursal es independiente:**
- Tiene su propia **Base de Datos local** (SQL Server)
- Opera aunque **no haya internet** (BD local)
- Tiene su propio **inventario en Almacén 1**
- Genera su propio **corte de caja** (Corte Z)

**La concentración es en la nube:**
- **MyNube / POS Tools** sincroniza la información
- El DG y Vianey pueden ver el concentrado de cortes
- La conexión entre sucursales es vía **internet** (no red local)

**Traspasos — el talón de Aquiles:**
- Se hace una **salida** en origen
- Se da de alta **manualmente** la entrada en destino
- Sin validación automática → errores frecuentes

---

<!-- DIAPOSITIVA 5: LOS TRES FLUJOS DE DINERO -->
# Tema: Sistemas | Diapositiva 5
## El problema central: 3 flujos de dinero no unificados

| Flujo | Qué incluye | Dónde se registra |
|-------|------------|-------------------|
| **1. Fiscal** | Ventas con CFDI, facturas formales | MyBusiness ✅ |
| **2. No fiscal** | Ventas sin factura, operaciones informales | Fuera del sistema ⚠️ |
| **3. Efectivo real** | Egresos en caja, retiros DG, cargadores, fletes | Excel + manual ⚠️ |

> **Consecuencia:** Al final del mes, la utilidad que muestra MyBusiness **no es la utilidad real** del negocio. Hay que sumar y restar los otros dos flujos manualmente.

**Solución propuesta:** Activar el módulo de gastos adicionales de MyBusiness + tipificar categorías de gasto.

---

<!-- DIAPOSITIVA 6: GASTOS DIARIOS — EL HALLAZGO -->
# Tema: Sistemas | Diapositiva 6
## Hallazgo: Gastos operativos fuera del sistema

**¿Qué gastos NO entran a MyBusiness?**

| Tipo de gasto | Ejemplos |
|---------------|---------|
| Servicios básicos menores | Pago de basura, agua, mantenimiento |
| Gastos de operación diaria | Comida del personal, mandados |
| Fletes y cargadores | Pagos en efectivo a cargadores |
| Retiros del DG | Gastos personales cargados al negocio |
| Otros | Todo lo que "se paga en cash sin factura" |

**¿Cómo se lleva hoy?** Excel → se reporta al contador mensualmente

**¿Qué falta?**
- Tipificar categorías de gasto
- Capturar en el módulo de MyBusiness que YA existe
- Definir quién lo captura (¿Rossy? ¿Encargados?)

---

<!-- DIAPOSITIVA 7: COBRANZA — PROBLEMA CRÍTICO -->
# Tema: Sistemas | Diapositiva 7
## Cobranza — El tema más complejo

> *"El sistema sabe lo que se vendió, pero no lo que se recuperó."*

**El ciclo roto:**

```
Cliente compra a crédito → Se registra en MyBusiness ✅
     ↓
Cliente paga (depósito bancario) → ¿Se registra? ⚠️
     ↓
En físico: Vianey sabe que pagó
En sistema: Sigue apareciendo como deudor ❌
     ↓
RESULTADO: Cartera sin certeza real
```

**Impacto:** No se puede tomar decisiones de crédito confiables. No se sabe cuánto dinero real se tiene en cartera.

**Solución:** Proceso obligatorio de captura de depósitos en MyBusiness el mismo día que se reciben.

---

<!-- DIAPOSITIVA 8: MYBUSINESS 2017 VS V24 -->
# Tema: Sistemas | Diapositiva 8
## MyBusiness 2017 vs. v24 — ¿Qué nos perdemos?

| Funcionalidad | MyBusiness 2017 (NVC hoy) | MyBusiness v24 |
|---------------|--------------------------|----------------|
| CFDI 4.0 nativo | ⚠️ No completo | ✅ Sí |
| Venta en ruta (celular) | ❌ No disponible | ✅ POS Tools integrado |
| Envío de comprobantes por WhatsApp | ❌ No disponible | ✅ Sí (2024) |
| Modo desconectado | Limited | ✅ Mejorado |
| Personalización BVisual | ⚠️ Visual Basic | ✅ Visual Studio |
| Costo actualización | — | ~$3,790/equipo |

**Veredicto:** La actualización a v24 es recomendable pero no emergencia inmediata. Primero ordenar procesos.

---

<!-- DIAPOSITIVA 9: 3 CAMINOS PARA MYBUSINESS -->
# Tema: Sistemas | Diapositiva 9
## Los 3 caminos con MyBusiness

| | Camino A | Camino B | Camino C |
|---|---------|---------|---------|
| **¿Qué?** | Optimizar 2017 | Ampliar con desarrollo | Migrar a ERP |
| **¿Cuándo?** | **HOY** | Mes 3–6 | Mes 18–24 |
| **Costo** | $0–$5,000 | $15,000–$60,000 | $30,000–$150,000 |
| **Riesgo** | Muy bajo | Bajo | Alto |
| **¿Cambia el sistema?** | No | No | Sí |
| **Recomendación** | ✅ Hacer ya | Planear | Evaluar después |

**Camino A inmediato:**
1. Activar módulo gastos adicionales (gratis)
2. Estandarizar captura de depósitos en cobranza (gratis)
3. Corregir proceso de traspasos (gratis)
4. Activar respaldo en nube ($1,799/año)
5. Evaluar actualización a v24 (~$3,790/equipo)

---

<!-- DIAPOSITIVA 10: HOJA DE RUTA TECNOLÓGICA -->
# Tema: Sistemas | Diapositiva 10
## Hoja de ruta tecnológica — Próximos 12 meses

| Mes | Acción | Costo estimado |
|-----|--------|---------------|
| Inmediato | Activar módulo gastos adicionales | $0 |
| Inmediato | Estandarizar registro de depósitos | $0 |
| Inmediato | Corregir proceso de traspasos manuales | $0 |
| Mes 1 | Activar MyNube (respaldo en nube) | $1,799/año |
| Mes 2 | Dashboard en Google Looker Studio | $0 |
| Mes 2 | Exportar historial 24 meses para análisis | $0 |
| Mes 3 | Evaluar actualización a v24 | ~$11,370 (3 equipos) |
| Mes 6 | Power BI conectado a SQL Server | $3,000–$8,000 |
| Mes 12+ | Evaluar Bind ERP si se cumplen triggers | $3,000–$8,000/mes |

---
*NVC — Módulo 04: Sistemas y Tecnología | Confidencial | Abril 2026*
