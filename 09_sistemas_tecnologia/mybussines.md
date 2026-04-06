# ANÁLISIS TÉCNICO: MyBusiness POS
## Software Administrativo y Punto de Venta — Evaluación para NVC

---

| Campo              | Detalle                                          |
|--------------------|--------------------------------------------------|
| **Documento**      | Análisis de Software — MyBusiness POS           |
| **Versión**        | v2.0                                             |
| **Fecha**          | 5 de abril de 2026                               |
| **Elaboró**        | Consultor Externo                                |
| **Propósito**      | Evaluar las capacidades reales del sistema que usa NVC y determinar si debe quedarse, complementarse o migrar |

---

## ÍNDICE

1. [¿Qué es MyBusiness POS?](#1-qué-es-mybusiness-pos)
2. [Versiones disponibles y precios](#2-versiones-disponibles-y-precios)
3. [Funcionalidades principales](#3-funcionalidades-principales)
4. [Manejo de usuarios y permisos](#4-manejo-de-usuarios-y-permisos)
5. [Trabajo en red y multi-sucursal](#5-trabajo-en-red-y-multi-sucursal)
6. [Capacidad, rendimiento y requisitos](#6-capacidad-rendimiento-y-requisitos)
7. [Integración e interoperabilidad](#7-integración-e-interoperabilidad)
8. [Opiniones de usuarios](#8-opiniones-de-usuarios)
9. [Errores comunes y problemas conocidos](#9-errores-comunes-y-problemas-conocidos)
10. [Actualizaciones y soporte](#10-actualizaciones-y-soporte)
11. [Competidores directos en México](#11-competidores-directos-en-méxico)
12. [Limitaciones — lo que NO hace o hace mal](#12-limitaciones--lo-que-no-hace-o-hace-mal)
13. [Evaluación específica para NVC](#13-evaluación-específica-para-nvc)
14. [Propuesta de mejora y complemento](#14-propuesta-de-mejora-y-complemento)

---

## 1. ¿QUÉ ES MYBUSINESS POS?

**MyBusiness POS** es un software de administración comercial y punto de venta (POS) desarrollado por una empresa **100% mexicana** con más de 25 años en el mercado.

| Dato | Información |
|------|-------------|
| **Empresa desarrolladora** | MyBusiness POS Desarrollos, S.A. de C.V. (antes Dintelsis, S.A. de C.V.) |
| **Sede** | Toluca, Estado de México |
| **Fundación** | 1990 (software desde 1999) |
| **Empleados** | 11–50 personas |
| **Licencias instaladas** | +127,000 en México y sur de EE.UU. |
| **Giros compatibles** | +550 tipos de negocio |
| **Sitio oficial** | mybusinesspos.com |
| **Soporte** | soporte.mybusinesspos.net |
| **Distribuidor certificado** | mbpservicios.com.mx |

**Propuesta de valor central:** Software poderoso para punto de venta y control administrativo de PYMEs mexicanas, a precio accesible, sin sacrificar funcionalidad.

**Posicionamiento:** Se presenta como el POS más vendido en México. Su enfoque principal es el ciclo comercial: ventas, inventarios, compras y facturación CFDI. No es un ERP completo.

---

## 2. VERSIONES DISPONIBLES Y PRECIOS

### Historial de versiones

| Versión | Año | Precio aprox. (MXN) | Estatus |
|---------|-----|---------------------|---------|
| MyBusiness 2011 | 2011 | $3,790 | Aún se vende, obsoleta |
| MyBusiness 2012 | 2012 | $3,790 | Aún se vende, obsoleta |
| **MyBusiness 2017** | **2017** | **$3,790** | **✅ VERSIÓN INSTALADA EN NVC** (confirmado entrevista 05/04/2026) |
| MyBusiness POS v20 | 2020 | $3,790 | Vigente pero anterior |
| **MyBusiness POS v24** | **2024** | **$3,790** | **Versión actual recomendada** |

> **⚠️ CONFIRMADO PARA NVC (05/04/2026):** NVC utiliza **MyBusiness 2017** con personalizaciones propias (notas/módulos adicionales desarrollados en el ambiente BVisual). La versión 2017 **no soporta CFDI 4.0 de forma nativa** y carece de funcionalidades críticas de v24 (venta en ruta, envío de comprobantes por WhatsApp, modo desconectado). La migración a v24 es urgente.

### Tipos de licencia actuales (v24)

| Tipo | Precio | ¿Para quién? |
|------|--------|-------------|
| **Estándar (MYB24)** | ~$3,790 MXN/equipo (licencia perpetua) | Una terminal/caja. Funciones principales de POS + inventario + facturación |
| **PRO (VPro)** | ~$5,999–$10,000 MXN/equipo | Automatización avanzada: carga masiva desde Excel, sugerido de traspasos, acceso en la nube incluido |
| **Corporativos** | Por contrato de servicio anual | Cadenas con 10+ sucursales. Incluye BI, integraciones con SAP/Oracle, e-commerce |

### Servicios adicionales (costos recurrentes)

| Servicio | Costo (MXN) |
|----------|-------------|
| Paquete 100 timbres CFDI | $465 |
| Paquete 1,000 timbres CFDI | ~$2,300 |
| Paquete 100,000 timbres CFDI | $128,760 |
| Servicios en la nube (respaldo + acceso remoto) | $1,799/año |
| Certificación operativa de usuario | $200 |
| Certificación de programador | $300 |

> **Modelo de negocio:** Licencia perpetua por equipo (sin mensualidad obligatoria). Los únicos costos recurrentes son los timbres CFDI y, opcionalmente, los servicios en la nube. Esto lo hace **más económico en el tiempo** que sistemas SaaS de renta mensual.

---

## 3. FUNCIONALIDADES PRINCIPALES

### 3.1 Punto de Venta (POS)

| Funcionalidad | ¿Disponible? | Notas |
|--------------|-------------|-------|
| Pantalla de cobro configurable | ✅ | Rediseñada en v24 |
| Impresora de tickets | ✅ | Compatible con impresoras térmicas estándar |
| Lector de código de barras | ✅ | |
| Cajón de dinero | ✅ | |
| Múltiples métodos de pago | ✅ | Efectivo, tarjeta, transferencia, PayPal, PayU |
| Corte de caja parcial (X) | ✅ | |
| Corte de caja total (Z) | ✅ | |
| Devoluciones y cancelaciones | ✅ | |
| Cotizaciones | ✅ | |
| Notas de venta / remisiones | ✅ | |
| **Modo desconectado** (sin red) | ✅ | **Nuevo en v24** — caja sigue operando si cae la red |
| Pantalla touchscreen | ✅ | |
| Autenticación biométrica (huella) | ✅ | Con hardware compatible |

### 3.2 Facturación Electrónica (MyCFDI)

| Funcionalidad | ¿Disponible? |
|--------------|-------------|
| CFDI 4.0 | ✅ |
| Complemento de pagos (REP) | ✅ |
| Autofacturación en línea para clientes | ✅ |
| Portal para ver/cancelar/descargar facturas | ✅ |
| **Carta Porte** (transporte de mercancías) | ⚠️ **No documentado claramente — verificar con proveedor** |

> **Alerta para NVC:** El complemento **Carta Porte** es obligatorio para distribuidoras que transportan mercancía propia en sus camionetas. Si NVC no lo tiene activo, está expuesto a multas del SAT. **Verificar urgente.**

### 3.3 Inventarios

| Funcionalidad | ¿Disponible? |
|--------------|-------------|
| Control de existencias por almacén | ✅ |
| Multi-almacén | ✅ |
| Entradas, salidas y traspasos entre sucursales | ✅ |
| Inventario físico (con o sin lector de datos) | ✅ |
| Control por número de serie, lote y caducidad | ✅ |
| Ensambles (productos compuestos) | ✅ |
| Actualización masiva de precios | ✅ |
| Sugerido automático de traspasos | ✅ (versión PRO) |
| Impresión de etiquetas con código de barras | ✅ |
| App móvil StockApp (Android) | ✅ |

### 3.4 Compras

| Funcionalidad | ¿Disponible? |
|--------------|-------------|
| Órdenes de compra / pedidos a proveedor | ✅ |
| Requisiciones | ✅ |
| Recepción de mercancías | ✅ |
| Compras por XML del proveedor (escanear XML en caja) | ✅ (nuevo en v24) |

### 3.5 Ventas y Cobranza

| Funcionalidad | ¿Disponible? |
|--------------|-------------|
| Ventas a crédito | ✅ |
| Precios diferenciados por cliente | ✅ |
| Múltiples listas de precios | ✅ |
| Cuentas por cobrar con seguimiento | ✅ |
| Reportes de cobranza | ✅ |
| Módulo de Promociones avanzado | ✅ (nuevo en v24: cupón QR, paquetes, temporadas) |
| WhatsApp para cobranza | ✅ (nuevo en v24) |

### 3.6 Contabilidad (módulo interno)

| Funcionalidad | ¿Disponible? | Calidad |
|--------------|-------------|---------|
| Catálogo de cuentas (código agrupador SAT) | ✅ | Básico |
| Pólizas contables automáticas | ✅ | Básico |
| Balanza de comprobación | ✅ | Básico |
| DIOT | ✅ | Básico |
| **Contabilidad Electrónica Anexo 24 completa** | ⚠️ | **No documentada — requiere verificación** |
| Conciliación bancaria automática | ❌ | **No disponible** |

> **Conclusión:** El módulo contable de MyBusiness **no reemplaza a CONTPAQi COI ni a Aspel COI** para el cumplimiento fiscal formal. Para declaraciones y contabilidad completa, NVC debe seguir usando un sistema contable dedicado (o el contador externo con su propio software).

### 3.7 Nómina

| Funcionalidad | Disponible |
|--------------|-----------|
| Timbrado de recibos de nómina (CFDI) | ✅ (limitado) |
| **Cálculo de nómina** (ISR, IMSS, INFONAVIT, prestaciones) | ❌ **NO disponible de forma nativa** |

> **Para NVC:** Si se va a regularizar el IMSS de todo el personal (como se recomienda en el plan), necesitarán un sistema de nómina separado o contratar el cálculo con el contador externo.

### 3.8 Apps móviles del ecosistema

| App | Plataforma | Función |
|-----|-----------|---------|
| **POS Tools** | Android (gratuita) | Venta en ruta, pedidos offline/online, facturación móvil, cobros con tarjeta |
| **StockApp** | Android | Gestión de inventarios desde celular |
| **CashApp** | Android | Gestión de catálogos y acceso de usuarios |
| **LoyaltyApp** | Android | Programa de lealtad con puntos, cupones QR, promociones |
| **ReporteBiew** | Android | Dashboard de indicadores en tiempo real |

> **Oportunidad para NVC:** **POS Tools** es especialmente relevante — permitiría a Pepe (San Simón) y Julio (Nueva Italia) levantar pedidos en campo desde el celular, sincronizarlos con el sistema y generar facturas sin ir a la computadora. Esto resuelve un problema operativo real identificado en el diagnóstico.

### 3.9 Otros módulos

| Módulo | Descripción |
|--------|-------------|
| Tiempo Aire | Venta de recargas telefónicas integradas (no aplica para NVC) |
| Business Intelligence | Integración con Power BI (vía distribuidor) |
| Mensajería WhatsApp entre sucursales | Nuevo en v24 — útil para reemplazar el grupo de WhatsApp informal |
| Ambiente de programación BVisual | Permite crear módulos personalizados sin costo adicional de licencia |

---

## 4. MANEJO DE USUARIOS Y PERMISOS

### Modelo de licenciamiento

> El modelo de MyBusiness es **licencia por equipo (terminal)**, no por usuario. Cada computadora necesita su propia licencia. No hay límite de usuarios nominados dentro de una instalación.

### Niveles de acceso

| Nivel | Acceso |
|-------|--------|
| **Supervisor** | Acceso total: configuración, usuarios, todos los reportes, funciones especiales en caja |
| **Operador / Cajero** | Acceso configurado por el supervisor: solo las funciones asignadas |
| **Permisos granulares** | Por carpeta dentro del Business Manager: Nuevo / Modificar / Eliminar |
| **Autenticación biométrica** | Compatible con lectores de huella digital |

### Cómo crear y gestionar usuarios

1. Ingresar como Supervisor (password "SUP SUP" por defecto — **cambiar inmediatamente**)
2. Business Manager → Configuración → Usuarios
3. Capturar: nombre de usuario, nombre completo, contraseña
4. Asignar permisos por módulo y acción

### Recomendación para NVC

| Puesto | Perfil sugerido en MyBusiness |
|--------|-------------------------------|
| Rossy (caja) | Cajero: solo POS, corte X, sin acceso a configuración |
| Vianey | Supervisor con acceso a compras, facturación, reportes, conciliación |
| Encargados (Paola, Briseida) | Cajero + inventario de su sucursal |
| DG | Supervisor total (solo para consulta, no operativo diario) |

---

## 5. TRABAJO EN RED Y MULTI-SUCURSAL

### Arquitectura técnica

```
[Servidor con SQL Server]
        │
    Red LAN (Ethernet / Wi-Fi)
        │
[Terminal 1]  [Terminal 2]  [Terminal N]
(caja/venta)  (admin)       (inventario)
```

**Motor de base de datos:** Microsoft SQL Server (Express gratuito o Standard/Enterprise de pago)
**Conexión:** TCP/IP, puerto 1433
**Driver requerido en clientes:** SQL Native Client (`sqlncli.msi`)

### Red local (LAN) — dentro de una sucursal

- Funciona en LAN sin internet
- Todas las terminales ven inventario, ventas y clientes en tiempo real
- Configuración técnica: requiere abrir puerto 1433 en el firewall del servidor
- **Sin conocimientos técnicos, la configuración en red es el principal punto de falla**

### Multi-sucursal — entre sucursales remotas

| Método | Descripción | Costo |
|--------|-------------|-------|
| **VPN** | Une las redes de cada sucursal vía internet | Requiere infraestructura de red (router con VPN) |
| **Servicios en la nube MyBusiness** | Las sucursales suben datos a servidores de MyBusiness; la matriz los consolida | $1,799 MXN/año |
| **Concentrador** | Módulo de MyBusiness para sincronizar cajas autónomas multi-sucursal | Código abierto, incluido |

> **Situación actual en NVC identificada en el Diagnóstico 01:**
> - Nueva Italia: 2 computadoras (servidor + punto de venta). El servidor hace traspasos y respaldo. ✅ Configuración correcta
> - San Simón: 1 computadora. ⚠️ Sin servidor dedicado — posible riesgo de pérdida de datos
> - Apatzingán: 3 computadoras. ✅ Configuración adecuada

**Capacidad máxima documentada:** Hasta **50 sucursales** simultáneas con el módulo Concentrador.

### Modo desconectado (v24)

Cada terminal puede seguir vendiendo aunque el servidor no sea alcanzable. Sincroniza automáticamente cuando se restaura la conexión. **Crítico para NVC:** si el internet de San Simón falla, la caja no debe pararse.

---

## 6. CAPACIDAD, RENDIMIENTO Y REQUISITOS

### Requisitos mínimos de hardware (v24)

| Componente | Mínimo | Recomendado |
|-----------|--------|-------------|
| SO | Windows 10 | Windows 11 |
| Procesador | Intel Dual Core | 3.2 GHz o superior |
| RAM | 4 GB | 8 GB (servidor) |
| Disco duro | 10 GB libres | 500 GB (servidor) |
| No-break | — | **Recomendado para servidor** |

### Límites críticos de la base de datos

| Motor SQL | Límite de base de datos | Costo |
|-----------|------------------------|-------|
| **SQL Server Express** (instalación gratuita por defecto) | **10 GB por base de datos** | Gratuito |
| **SQL Server Standard** | 524 PB | ~$18,000–$35,000 MXN |
| **SQL Server Enterprise** | Ilimitado | Muy alto |

> **⚠️ Alerta para NVC:** Si llevan varios años de operación en MyBusiness y nunca han revisado el tamaño de la base de datos, pueden estar cerca del límite de 10 GB de SQL Server Express. Esto causaría errores al intentar guardar nuevas transacciones. **Verificar urgente el tamaño actual de la base de datos.**

---

## 7. INTEGRACIÓN E INTEROPERABILIDAD

### Con el SAT

| Integración | Estado |
|-------------|--------|
| CFDI 4.0 | ✅ Nativo |
| Complemento de pagos (REP) | ✅ Nativo |
| DIOT | ✅ Básico |
| Contabilidad Electrónica Anexo 24 | ⚠️ No documentado claramente |
| **Carta Porte** | ⚠️ **Verificar — crítico para NVC** |

### Con otros sistemas

| Sistema | Integración | Tipo |
|---------|-------------|------|
| CONTPAQi / CONTPAQ | ⚠️ No nativa | Requiere desarrollo de conector o exportación manual |
| Aspel | ❌ No documentada | — |
| SAP B1 / Oracle | ✅ (versión Corporativa) | Vía desarrollo de distribuidor certificado |
| WooCommerce (e-commerce) | ✅ API directa (v24) | Para catálogo y pedidos online |
| Power BI | ✅ (vía distribuidor) | Para dashboard avanzado |
| Bancos (conciliación) | ❌ No disponible | — |
| WhatsApp Business | ✅ (v24, mensajería) | Notificaciones y cobranza |

### Personalización y desarrollo

- **Ambiente BVisual** (HTML + AngelDB): Permite a distribuidores certificados crear módulos personalizados, reportes adicionales e integraciones
- **Concentrador:** Código abierto — personalizable
- **API REST / SQL directo:** Los distribuidores pueden conectar MyBusiness a sistemas externos vía consultas SQL al servidor

---

## 8. OPINIONES DE USUARIOS

### Lo que dicen positivamente

- "Permite medir ventas del día, flujo monetario y control de inventario desde cualquier sucursal"
- "Fácil de aprender para el usuario final"
- "No necesitamos largas capacitaciones; los videotutoriales son suficientes"
- "La relación precio-valor es muy competitiva frente a Aspel o CONTPAQi"
- "El ambiente de programación nos permite adaptarlo exactamente a nuestro giro"
- "Funciona muy bien para abarrotes, ferreterías y distribuidoras"

### Críticas frecuentes

| Queja | Frecuencia |
|-------|-----------|
| Errores de conexión SQL (Código Duro 58 / Error 5) | 🔴 Muy alta |
| Dificultad en la instalación inicial en red | 🔴 Alta |
| Soporte técnico directo del fabricante lento | 🟡 Media |
| Costo de soporte con distribuidores certificados | 🟡 Media |
| Módulo contable insuficiente para contabilidad fiscal | 🟡 Media |
| Migración entre versiones compleja | 🟡 Media |
| Conflictos con antivirus (Avast) | 🟡 Media |

### Calificación en plataformas

| Plataforma | Calificación | Reseñas |
|-----------|-------------|---------|
| Capterra MX | Listado disponible | ~8 reseñas verificadas (muestra pequeña) |
| G2 / Trustpilot | Sin página específica encontrada | — |

> **Conclusión:** MyBusiness tiene una base de usuarios leal en el segmento PYME mexicano, pero el soporte técnico y la contabilidad formal son sus puntos más débiles.

---

## 9. ERRORES COMUNES Y PROBLEMAS CONOCIDOS

### Errores técnicos documentados

| Error | Causa | Solución |
|-------|-------|---------|
| **Código Duro 58** | SQL Server no corriendo, puerto bloqueado, credenciales incorrectas | Iniciar servicio SQL Server, abrir puerto 1433 en firewall, verificar credenciales |
| **Código Duro 5** | Permisos denegados sobre archivos de base de datos | Ejecutar como administrador, ajustar permisos en `C:\MyBusinessDatabase` |
| **Error 2147467259** | SQL Server no permite crear base de datos | Ajustar permisos de Windows/SQL Server |
| **Error TCP Provider** | Cliente no alcanza al servidor | Verificar red, IP del servidor, puerto, estado del servicio SQL |
| **Conflicto con antivirus** | Avast u otros bloquean el ejecutable | Agregar excepción en antivirus para MyBusiness POS |
| **Problemas de CFDI 4.0** | Configuración de timbres o certificados incorrecta | Verificar configuración de MyCFDI y vigencia del CSD |
| **Base de datos llena (10 GB)** | SQL Server Express al límite | Migrar a SQL Server Standard o hacer limpieza de históricos |

### Problemas operativos habituales en PYMEs

| Problema | Impacto para NVC |
|---------|-----------------|
| Usuarios comparten contraseña del supervisor | Riesgo de modificaciones no autorizadas e imposibilidad de auditoría |
| Inventario desactualizado por no registrar todas las entradas | Diferencias físico vs sistema (problema ya identificado en NVC) |
| Tickets no registrados en el sistema (ventas fuera del POS) | Pérdida de trazabilidad y potencial evasión fiscal |
| Sin respaldo automático de la base de datos | Riesgo de pérdida total de datos ante falla del servidor |
| Versión desactualizada sin CFDI 4.0 | Multas del SAT y cancelación de facturación |

---

## 10. ACTUALIZACIONES Y SOPORTE

### Frecuencia de versiones mayores

- **Cada 3–4 años** (2011, 2012, 2017, 2020, 2024)
- Parches y actualizaciones menores: disponibles en el sitio oficial para descarga

### Canales de soporte (de mejor a peor acceso)

| Canal | Costo | Calidad |
|-------|-------|---------|
| **Distribuidor certificado** (MBP Servicios y similares) | Pago (hora o contrato anual) | Alta — soporte especializado |
| **Videotutoriales oficiales** (mybusinesspos.com) | Gratis | Media — solo problemas comunes |
| **Blog no oficial helpmybusinesspos.info** | Gratis | Media-Alta — errores técnicos |
| **Soporte.mybusinesspos.net** (foro) | Gratis | Baja — poca actividad |
| **Soporte directo del fabricante** | Variable | Variable — sin SLA documentado |

> **Recomendación para NVC:** Contratar a un **distribuidor certificado local** con contrato de servicio anual. El costo es predecible y garantiza respuesta ante cualquier falla técnica, especialmente el temido Error 58.

---

## 11. COMPETIDORES DIRECTOS EN MÉXICO

### Tabla comparativa — enfocada en distribuidoras como NVC

| Criterio | **MyBusiness POS** | **Bind ERP** | **Microsip** | **CONTPAQi Comercial** | **Aspel SAE+CAJA** |
|----------|-------------------|--------------|--------------|----------------------|-------------------|
| **Modelo de pago** | Licencia perpetua ~$3,790/equipo | SaaS mensual | Modular permanente/suscripción | Licencia + anualidad | Mensual o permanente |
| **POS / Caja rápida** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Inventarios** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Contabilidad** | ⭐⭐ (básica) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Nómina nativa** | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Multi-sucursal** | ✅ Hasta 50 | ✅ | ✅ | ✅ | ✅ |
| **100% en la nube** | ❌ (parcial) | ✅ | ❌ | ❌ | ❌ |
| **Personalización** | ⭐⭐⭐⭐⭐ (BVisual) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **App móvil de campo** | ✅ POS Tools | ✅ | ✅ CEO Móvil | ❌ | ❌ |
| **CFDI 4.0** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Carta Porte** | ⚠️ Verificar | ✅ | ✅ | ✅ | ✅ |
| **E-commerce** | ✅ (WooCommerce) | ✅ | ✅ | ✅ | ✅ |
| **Precio entrada total** | **Bajo** | Medio | Medio-alto | Alto | Medio |
| **Costo mensual recurrente** | Muy bajo (solo timbres) | Alto | Bajo-medio | Medio | Medio |

---

## 12. LIMITACIONES — LO QUE NO HACE O HACE MAL

| # | Limitación | Impacto para NVC | Urgencia |
|---|-----------|-----------------|---------|
| L1 | **Sin cálculo de nómina nativo** — solo timbra recibos calculados externamente | Alto — NVC debe regularizar IMSS de todo el personal | 🔴 Alta |
| L2 | **Contabilidad formal incompleta** — no reemplaza CONTPAQi COI para Anexo 24 y declaraciones | Alto — el contador externo necesita un sistema contable dedicado | 🔴 Alta |
| L3 | **Sin Carta Porte documentada** — crítico para distribuidoras que entregan con camionetas propias | Muy alto — riesgo de multas del SAT en cada entrega | 🔴 Alta |
| L4 | **Límite de 10 GB en SQL Server Express** — puede saturarse con años de historial | Alto — riesgo de bloqueo del sistema | 🟡 Media |
| L5 | **Sin conciliación bancaria automática** — reconciliar manualmente es lento y propenso a error | Medio — Vianey lo hace manualmente | 🟡 Media |
| L6 | **Sin CRM nativo** — solo catálogo de clientes + historial de compras | Medio — no hay seguimiento de oportunidades ni pipeline | 🟡 Media |
| L7 | **No es 100% en la nube** — requiere infraestructura local con servidor | Bajo — NVC ya tiene servidores en sucursales | 🟢 Baja |
| L8 | **Integración con CONTPAQi no nativa** — requiere exportación manual o conector de tercero | Medio — Vianey hace conciliación manualmente entre ambos sistemas | 🟡 Media |
| L9 | **Sin módulo de manufactura/producción** — no aplica a la línea de tilapia de NVC | Medio — la producción de tilapia no está sistematizada | 🟡 Media |
| L10 | **Sin multi-empresa nativa** — para manejar varias razones sociales necesitaría varias bases de datos | Bajo — NVC opera bajo una sola entidad (hoy) | 🟢 Baja |
| L11 | **Soporte técnico sin SLA garantizado** — no hay tiempo de respuesta documentado | Medio — falla el sistema = sucursal parada | 🟡 Media |
| L12 | **Configuración en red compleja para usuarios no técnicos** — el Error 58 es el más frecuente | Alto — NVC no tiene personal de TI interno | 🟡 Media |

---

## 13. EVALUACIÓN ESPECÍFICA PARA NVC

### ¿MyBusiness les sirve hoy?

**Sí, con condiciones.** Para las necesidades actuales de NVC — punto de venta, inventarios, facturación CFDI y control de cobranza — MyBusiness POS es adecuado. Pero tiene **brechas críticas que deben resolverse.**

### Brechas críticas que resolver YA

| Brecha | Estado confirmado (05/04/2026) | Acción inmediata |
|--------|-------------------------------|------------------|
| Versión instalada | ⚠️ **MyBusiness 2017** — pendiente actualización | Evaluar actualización a v24 (CFDI 4.0, venta en ruta, WhatsApp) |
| Carta Porte activa | ❓ Sin confirmar | Verificar con Vianey y distribuidor — multas SAT en cada entrega |
| Respaldos | ⚠️ Se realizan pero **no están en la nube** — son locales | Activar Servicios en la Nube MyBusiness ($1,799/año) |
| Acceso remoto | Se conectan vía **AnyDesk** — solo una persona autorizada para movimientos | Documentar el protocolo; considera acceso en la nube nativo (v24) |
| Tamaño de base de datos | ❓ Sin verificar | Revisar que no supere 8 GB en SQL Express |
| Usuarios configurados | ❓ Sin confirmar | Verificar perfiles individuales vs. contraseña compartida |
| San Simón sin servidor | ⚠️ Confirmado en Dx01 | Evaluar agregar segundo equipo |

### Lo que MyBusiness SÍ resuelve para NVC

- ✅ Control de inventario multi-almacén (Apatzingán, San Simón, Nueva Italia)
- ✅ Punto de venta rápido en mostrador
- ✅ Facturación CFDI 4.0
- ✅ Traspasos de mercancía entre sucursales
- ✅ Corte de caja diario con reporte
- ✅ POS Tools para venta en campo (Pepe y Julio con celular)
- ✅ Reportes de ventas por sucursal y producto (base para el dashboard)
- ✅ Historial de ventas exportable (base del análisis de inventarios/ventas)
- ✅ Modo desconectado (v24) — sucursal opera aunque caiga el internet

### Lo que MyBusiness NO resuelve para NVC (y necesita complemento)

- ❌ Cálculo de nómina para regularización IMSS
- ❌ Contabilidad formal completa (ya tiene CONTPAQ con el contador)
- ❌ Dashboard gerencial visual y consolidado (usar Power BI o Excel por encima de MyBusiness)
- ❌ CRM para seguimiento de clientes (complementar con Excel o herramienta ligera)
- ❌ Control de producción de tilapia

---

## 14. PROPUESTA DE MEJORA — 3 CAMINOS DISTINTOS

Hay **tres caminos posibles**, no uno. No se deben mezclar. Cada uno tiene su propio costo, plazo y condición de aplicación. La respuesta a "¿qué hacer con MyBusiness?" depende del momento y del presupuesto.

---

### ÁRBOL DE DECISIÓN

```
¿MyBusiness cubre las necesidades operativas actuales de NVC?
│
├─► SÍ, cubre lo esencial (ventas, inventario, CFDI)
│   │
│   ├─► ¿Tiene brechas menores (respaldo, usuarios, Carta Porte)?
│   │   └─► CAMINO A — Optimizar lo que ya tienes (Hoy, costo mínimo)
│   │
│   └─► ¿Necesitas más automatización o módulos extra?
│       └─► CAMINO B — Ampliar MyBusiness (Meses 2–6, inversión moderada)
│
└─► NO cubre en 18–24 meses (10 suc., nómina, contabilidad, nube)
    └─► CAMINO C — Migrar a otro sistema (Futuro, inversión mayor)
```

---

### CAMINO A — OPTIMIZAR LO QUE YA TIENES
**"Sacarle el máximo a MyBusiness sin gastar más"**
**Plazo: Semanas 1–4 | Costo: $0 a $5,000 MXN**

> Este es el camino inmediato para NVC. No requiere cambiar nada del sistema, solo activar lo que ya está disponible y corregir errores de configuración.

#### A1 — Acciones sin costo (esta semana)

| Acción | Por qué es urgente |
|--------|-------------------|
| Crear usuario individual por persona (no compartir "SUP SUP") | Sin usuarios nominados no hay auditoría posible ni control real |
| Verificar qué versión está instalada — actualizar a v24 si no la tienen | CFDI 4.0 es obligatorio; versiones viejas generan errores con el SAT |
| Revisar el tamaño de la base de datos SQL Server | Si supera 8 GB en Express, el sistema puede bloquearse sin aviso |
| Estandarizar catálogo de productos (eliminar duplicados, asignar códigos) | Sin catálogo limpio, los reportes de ventas son inútiles para el análisis |
| Exportar historial de ventas de los últimos 12–24 meses | Es la línea base del proyecto — sin esto no se puede medir nada |

#### A2 — Acciones de bajo costo ($1,800–$3,000 MXN)

| Acción | Costo | Qué resuelve |
|--------|-------|-------------|
| Activar **Servicios en la Nube** de MyBusiness | $1,799 MXN/año | Respaldo automático diario + acceso remoto del DG desde cualquier lugar |
| Activar **POS Tools** en celular de Pepe y Julio | Gratis (app) + configuración ~$1,000 MXN con distribuidor | Levantamiento de pedidos en campo desde el celular, sincronizado al sistema |
| Verificar y activar **Carta Porte** | $0–$2,000 MXN con distribuidor | Evitar multas del SAT en cada entrega con camioneta propia |
| Activar **WhatsApp de cobranza** (v24) | $0 (incluido en v24) | Envío automático de recordatorios de pago a clientes con saldo vencido |

#### A3 — Sistemas complementarios gratuitos o de bajo costo (no son MyBusiness, se usan al lado)

> MyBusiness hace bien su trabajo de POS e inventario, pero no hace todo. Estos complementos **no reemplazan a MyBusiness** — lo acompañan.

| Complemento | Herramienta sugerida | Costo | Qué cubre |
|-------------|---------------------|-------|-----------|
| **Dashboard gerencial** (KPIs visuales) | Google Looker Studio o Power BI Desktop | Gratis | Conecta con los exports de MyBusiness y genera gráficas para el DG |
| **CRM básico** (seguimiento de clientes) | Excel estructurado (inmediato) → HubSpot CRM gratuito (mes 2) | Gratis | Registro de clientes, seguimiento de ventas, clientes inactivos |
| **Nómina** (cálculo de IMSS, ISR, etc.) | Aspel NOI o CONTPAQi Nóminas | ~$800–$1,500 MXN/mes | Cálculo correcto de nómina para regularización del IMSS |
| **Contabilidad formal** | Ya tienen CONTPAQ con el contador externo | Ya pagado | Declaraciones, Anexo 24, DIOT — el contador lo usa, NVC no necesita otro |
| **Comunicación interna** | WhatsApp Business (oficial por sucursal) | Gratis | Reemplaza el grupo informal de WhatsApp por canales institucionales |
| **Correo institucional** | Google Workspace (~$120 MXN/usuario/mes) | Bajo | Correos @nvc.mx por sucursal y encargado |

**→ Resultado del Camino A:** MyBusiness queda bien configurado, sin brechas críticas, con herramientas gratuitas que cubren lo que le falta, y sin cambiar el sistema central. **Es lo que se recomienda hacer HOY.**

---

### CAMINO B — AMPLIAR MYBUSINESS CON DESARROLLO A MEDIDA
**"Agregar módulos y automatizaciones encima del sistema existente"**
**Plazo: Meses 2–6 | Costo: $15,000–$60,000 MXN (inversión única)**

> Este camino aplica si el Camino A ya está hecho y NVC quiere más automatización sin cambiar de sistema. Se hace con un **distribuidor certificado de MyBusiness** que programa en BVisual (el ambiente de desarrollo nativo del software).

**No es un sistema nuevo. No es desarrollo propio. Es contratar a un programador certificado de MyBusiness para agregar funciones específicas.**

| Módulo a desarrollar | Qué automatiza | Costo aprox. |
|---------------------|---------------|-------------|
| **Conector MyBusiness ↔ CONTPAQi** | Elimina la doble captura — las ventas pasan automáticamente al sistema del contador | $5,000–$15,000 MXN (una vez) |
| **Dashboard en Power BI** conectado directo al SQL Server de MyBusiness | El DG ve ventas, inventario y cartera en tiempo real desde su celular o laptop, sin exportar archivos | $3,000–$8,000 MXN implementación + Power BI Desktop gratis |
| **Módulo de seguimiento de clientes** (mini-CRM dentro de MyBusiness) | Registro de visitas, llamadas, historial de contacto, alertas de clientes sin compra en 30+ días | $5,000–$12,000 MXN |
| **Módulo de control de rutas/entregas** | Asignación de pedidos a camionetas, seguimiento de entrega, firma digital del cliente | $8,000–$20,000 MXN |
| **Tienda en línea integrada** | Catálogo de productos en web, pedidos online sincronizados al inventario de MyBusiness (vía API WooCommerce nativa en v24) | $10,000–$25,000 MXN (desarrollo del sitio web aparte) |
| **Actualización a SQL Server Standard** | Elimina el límite de 10 GB, base de datos crece sin problema hasta las 10 sucursales | $18,000–$35,000 MXN (licencia Microsoft) + instalación |

**¿Cuándo elegir el Camino B sobre el C?**
- Cuando el equipo ya conoce MyBusiness y cambiar generaría mucha resistencia
- Cuando el presupuesto no alcanza para una migración completa
- Cuando las brechas son específicas y puntuales (no todo el sistema está mal)
- Cuando NVC tiene entre 5 y 8 sucursales y el sistema actual aún aguanta

**→ Resultado del Camino B:** MyBusiness ampliado con automatizaciones específicas, sin migrar, sin reentrenar a todo el equipo desde cero. Es la evolución natural del Camino A para cuando NVC esté más organizado y tenga presupuesto.

---

### CAMINO C — MIGRAR A OTRO SISTEMA
**"Reemplazar MyBusiness por un ERP más completo"**
**Plazo: 18–24 meses desde hoy (NO antes) | Costo: $30,000–$150,000 MXN**

> **Este camino NO se recomienda ahora.** Migrar mientras la empresa está en proceso de reorganización sería sumar caos sobre caos. Primero hay que ordenar la operación (Caminos A y B), y solo entonces evaluar si el sistema es el verdadero cuello de botella.

**¿Cuándo evaluar migrar?** Solo si se cumple al menos uno de estos triggers:

| Trigger | Señal concreta |
|---------|---------------|
| La empresa llega a 8–10 sucursales y el Concentrador de MyBusiness se vuelve difícil de administrar | El DG o Vianey pasan más de 2 horas/semana resolviendo problemas de sincronización entre sucursales |
| Se necesita nómina + contabilidad + inventario + POS en un solo sistema (sin sistemas separados) | El contador externo termina el contrato o NVC contrata un equipo contable interno |
| La base de datos supera los 10 GB y SQL Server Standard resulta demasiado caro | Más económico pagar una suscripción de nube que una licencia de Microsoft Enterprise |
| NVC quiere vender en línea con inventario unificado en tiempo real | El e-commerce con MyBusiness requiere demasiado desarrollo a medida |
| La dirección decide profesionalizar a nivel de ERP formal (con financiero, proyectos, producción de tilapia) | El DG quiere un sistema de gestión empresarial, no solo un POS |

#### Opciones de migración evaluadas para NVC

| Sistema | Tipo | Lo que gana NVC | Costo aprox. |
|---------|------|----------------|-------------|
| **Bind ERP** | SaaS (100% nube) | Todo integrado: ventas, inventario, compras, contabilidad, nómina, e-commerce. Sin servidor local. Multi-sucursal nativo. Especializado en distribuidoras. | $3,000–$8,000 MXN/mes |
| **Microsip ERP** | On-premise modular | Nómina + contabilidad + ventas + inventario integrados. Venta en ruta (CEO Móvil). Licencia permanente. | $40,000–$80,000 MXN inversión inicial |
| **CONTPAQi Comercial Pro + COI + Nóminas** | On-premise modular | Integración total con la contabilidad que ya lleva el contador. El estándar fiscal más sólido en México. | $50,000–$100,000 MXN por ecosistema completo |
| **Odoo Community + localización MX** | Open source + implementación | ERP completo internacional, muy personalizable, CFDI 4.0 y Carta Porte disponibles. Sin costo de licencia, sí de implementación. | $30,000–$100,000 MXN implementación |

> **Recomendación si llega el momento de migrar:** Evaluar primero **Bind ERP** por su especialización en distribuidoras, su modelo en la nube (sin servidores propios) y su integración nativa con CONTPAQi para no perder al contador externo.

**→ Resultado del Camino C:** Sistema único que integra todo, pero con el costo de la migración, la curva de aprendizaje de todo el equipo y el tiempo fuera de operación normal. Solo vale la pena cuando el negocio ya está maduro y ordenado.

---

### RESUMEN DE LOS 3 CAMINOS

| | Camino A | Camino B | Camino C |
|---|----------|----------|----------|
| **¿Qué es?** | Optimizar MyBusiness actual | Ampliar MyBusiness con desarrollo | Reemplazar MyBusiness por ERP |
| **¿Cuándo?** | HOY | Meses 2–6 | Meses 18–24 |
| **¿Quién lo hace?** | NVC + distribuidor básico | Distribuidor certificado MyBusiness | Consultor de implementación ERP |
| **Costo** | $0–$5,000 MXN | $15,000–$60,000 MXN | $30,000–$150,000 MXN |
| **Riesgo operativo** | Muy bajo | Bajo | Alto |
| **¿Cambia el sistema?** | No | No | Sí |
| **¿Requiere reentrenamiento?** | Mínimo | Parcial (módulos nuevos) | Total |
| **Recomendación** | ✅ Hacer ya | ✅ Planear para mes 3 | ⏳ Evaluar en 18 meses |

---

## RESUMEN EJECUTIVO

| Aspecto | Calificación | Nota |
|---------|-------------|------|
| POS y ventas en mostrador | ⭐⭐⭐⭐⭐ | Excelente para el core del negocio NVC |
| Control de inventarios | ⭐⭐⭐⭐ | Bueno, pero requiere disciplina operativa |
| Facturación CFDI 4.0 | ⭐⭐⭐⭐ | Bien, pero verificar Carta Porte urgente |
| Multi-sucursal | ⭐⭐⭐⭐ | Funcional, mejorar con Servicios en la Nube |
| Contabilidad | ⭐⭐ | No reemplaza sistema contable formal |
| Nómina | ⭐ | Prácticamente no disponible |
| Reportes y BI | ⭐⭐⭐ | Suficiente para base, necesita Power BI encima |
| Soporte técnico | ⭐⭐⭐ | Requiere distribuidor certificado |
| Costo total de propiedad | ⭐⭐⭐⭐⭐ | Muy competitivo para el nivel de funcionalidad |
| **Calificación global para NVC** | **⭐⭐⭐½** | **Adecuado HOY. Camino A inmediato → Camino B en mes 3 → Camino C en 18–24 meses si se cumplen triggers** |

---

## FUENTES

| Fuente | URL |
|--------|-----|
| Sitio oficial MyBusiness POS | mybusinesspos.com |
| Catálogo y precios | mybusinesspos.com/collections/all |
| FAQ oficial | mybusinesspos.com/pages/preguntas-frecuentes |
| Multi-sucursal / Corporativos | mybusinesspos.com/pages/corporativos |
| App POS Tools (venta en ruta) | mybusinesspos.com/pages/venta-en-ruta-para-android |
| Servicios en la nube | mybusinesspos.com/pages/servicios-en-la-nube |
| Novedades v24 | boletin.mx (julio 2024) |
| Análisis de canal v24 | infochannel.info |
| Errores técnicos y configuración en red | helpmybusinesspos.info |
| Gestión de usuarios | helpmybusinesspos.info/usuario |
| Distribuidor certificado MBP Servicios | mbpservicios.com.mx |
| Versión PRO con precios | solucionespos.mx |
| Historia de la empresa | lohechoenmexico.mx |
| Reseñas Capterra MX | capterra.mx/software/212061/mybusiness-pos |
| Bind ERP (alternativa) | bind.com.mx |
| Microsip (alternativa) | microsip.com |
| CONTPAQi (alternativa) | contpaqi.com |

---

## 15. USO REAL EN NVC — HALLAZGOS DE ENTREVISTA (05/04/2026)

> Esta sección documenta cómo NVC **realmente usa** MyBusiness 2017, basado en entrevista directa con el área administrativa. Es complemento al análisis técnico general de las secciones anteriores.

### 15.1 Módulos activos confirmados

| Módulo | Estado en NVC |
|--------|---------------|
| Punto de Venta (POS) | ✅ Activo |
| Facturación CFDI | ✅ Activo |
| Cuentas por Pagar | ✅ Activo (Apatzingán) |
| Cuentas por Cobrar | ✅ Activo (Nueva Italia) |
| Inventarios por almacén | ✅ Activo — cada tienda tiene Almacén 1 |
| Multi-sucursal / Concentrador | ✅ Activo vía MyNube/PosTools |
| Traspasos entre sucursales | ✅ Activo pero **se realizan de forma manual** |
| Módulo de gastos adicionales | ⚠️ Existe en el sistema pero **no se usa** — se lleva en Excel |
| Corte Z (corte total de caja) | ✅ Activo — cada tienda tiene su propio corte |

### 15.2 Arquitectura real multi-sucursal

```
Arquitectura confirmada en NVC:

[Apatzingán - BD Local]  [San Simón - BD Local]  [Nueva Italia - BD Local]
         │                       │                        │
         └───────────────────────┴────────────────────────┘
                                 │
                    MyNube / POS Tools (internet)
                    Concentrador de información
                    (dashboard de cortes consolidado)
```

**Puntos clave:**
- Cada sucursal tiene su **propia base de datos local** e **inventario independiente** (Almacén 1 por tienda)
- Las tiendas funcionan de forma autónoma — si cae el internet, la operación no se detiene
- La sincronización/concentración se hace a través de **MyNube/POS Tools** (servicio en la nube de MyBusiness)
- La conexión NO es en red local directa entre sucursales — es vía internet a través del concentrador

### 15.3 Traspasos entre sucursales — proceso manual

> **Problema identificado:** Los traspasos no se realizan de forma automatizada. El proceso actual es:

1. Se genera una **salida** en la tienda de origen (mercancía sale del inventario local)
2. Alguien da de alta manualmente una **entrada** en la tienda destino
3. No existe validación automática ni alerta de discrepancias
4. **Se realizan mal algunos traspasos o no se registran adecuadamente en MyBusiness** — error operativo frecuente

**Impacto:** Diferencias de inventario entre tiendas, pérdida de trazabilidad, inconsistencias en reportes.

**Antes:** Se usaban estándares de traspaso (un traspaso para una tienda o para todas) para saber cuánto se pasa de una tienda a otra.

### 15.4 Manejo de producto a granel (kileado)

Se identificó un proceso específico de conversión de presentaciones:
- Un producto tiene **dos registros**: el bulto y el kileado
- Se registra **salida por bultos** y **entrada por kilos**
- Esto generó problemas de inventario porque la venta se realiza mayoritariamente por bulto
- El seguimiento por kilos **no funcionó correctamente** — se abandonó parcialmente

### 15.5 Cobranza — problema crítico

> **Uno de los temas más complejos del uso de MyBusiness en NVC.**

| Síntoma | Detalle |
|---------|--------|
| Depósitos no capturados | Se recibe el pago físico pero no se registra en sistema — hay clientes que en papel no deben pero sí aparecen con saldo |
| Certeza limitada | El sistema sabe lo que se vendió, **pero no lo que se recuperó** |
| Registros paralelos | Existe reporte de ventas, pero la recuperación de cartera se lleva fuera del sistema |

**Consecuencia:** No hay certeza real del estado de la cartera. La cobranza se confirma "en físico" pero no se concilia sistemáticamente con MyBusiness.

### 15.6 Flujos de dinero — tres registros paralelos

NVC opera con **tres flujos de dinero diferenciados** que no están unificados en MyBusiness:

| Flujo | Descripción | Dónde se registra |
|-------|-------------|-------------------|
| **Flujo fiscal** | Ventas con CFDI, facturas formales | MyBusiness |
| **Flujo no fiscal** | Ventas sin factura, operaciones informales | Registro paralelo (fuera del sistema) |
| **Flujo de efectivo** | Movimientos de caja, pagos en efectivo, egresos no tipificados | Parcialmente en MyBusiness + Excel + registros manuales |

> **Hallazgo crítico:** Los egresos no siempre se capturan en el sistema. Cuando alguien "se lleva dinero" (para gastos, fletes, cargadores, uso personal del DG), esto no necesariamente queda registrado. El **módulo de gastos adicionales** de MyBusiness existe pero no se utiliza.

### 15.7 Concentrado de cortes (Dashboard informal)

Actualmente existe un "concentrado de cortes" que funciona como dashboard informal:
- Qué se vendió
- Qué se cobró
- Qué salió de egresos
- Cómo fue el flujo de dinero

Este concentrado **no está en MyBusiness** — se construye manualmente y se reporta por WhatsApp.

### 15.8 Soporte técnico y acceso remoto

- El acceso remoto para soporte técnico se realiza vía **AnyDesk**
- Solo **una persona autorizada** puede hacer movimientos remotos
- El modelo es pago único por el sistema + pago por soporte cuando se requiere, o por actualizaciones, o por los servicios de nube
- Los **respaldos se realizan** pero son **locales, no en la nube**
- MyBusiness 2017 vs. v24: la versión actual (2024) incluye envío de comprobantes por WhatsApp y venta en rutas — funcionalidades que NVC no tiene disponibles

### 15.9 Personalización y ambiente de desarrollo

MyBusiness tiene un **ambiente de desarrollo propio** que permite modificar y extender el sistema:
- Históricamente se desarrolló en **Visual Basic**
- Actualmente la plataforma usa **Visual Studio**
- El propio MyBusiness cuenta con su **ambiente de desarrollo nativo (BVisual)**
- NVC tiene algunas **notas/módulos adicionales** desarrollados sobre la versión 2017
- Es **open source** en su capa de personalización — con las claves de superadministrador se puede modificar
- Los **reportes también se pueden personalizar** dentro del sistema

> **Punto de fondo:** El problema no es únicamente técnico. La administración de la información y la disciplina de captura son tan importantes como las funcionalidades del sistema: *"Que los procesos sean y se cumplan como se debe hacer — rígido y flexible, que la gente haga lo que tiene que hacer para que funcione."*

### 15.10 Hallazgo: gastos diarios fuera del sistema

> **Ver también: Diagnóstico 01 — Hallazgos / Hallazgos complementarios**

Los **gastos operativos diarios menores** (basura, mandados, comida, cargadores, fletes menores, etc.) **NO se registran en MyBusiness**. En su lugar:
- Se lleva un **registro en Excel**
- Se reporta al contador de forma **mensual**
- No hay tipificación de categorías de gastos
- El módulo de gastos adicionales de MyBusiness existe pero no se usa

**Impacto:** La utilidad real del negocio al cierre de mes no se puede calcular directamente desde MyBusiness sin integrar este Excel. El flujo de efectivo real es siempre mayor al reflejado en el sistema.

---

### Historial de versiones

| Versión | Fecha | Cambios | Elaboró |
|---------|-------|---------|---------|
| 1.0 | 19/02/2026 | Versión inicial — análisis general de MyBusiness POS | Consultor externo |
| 2.0 | 05/04/2026 | Confirmación de versión 2017 instalada en NVC. Nueva sección 15 con hallazgos de uso real: arquitectura BD local por sucursal, concentrador MyNube/PosTools, traspasos manuales con errores, cobranza sin certeza, tres flujos de dinero, gastos fuera del sistema, acceso AnyDesk, respaldos locales, personalización BVisual | Consultor externo |

---

*NVC — Análisis MyBusiness POS v2.0 | Consultoría Externa | Confidencial*
