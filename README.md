# 🍬 CandyFlow ERP

<p align="center">
  <img src="https://img.icons8.com/color/200/candy.png" alt="CandyFlow Logo" width="200"/>
</p>

---

## 📱 Descripción

CandyFlow ERP es un sistema integral para **fábricas y distribuidoras de dulces**, construido con **Django + PostgreSQL + Docker** y una interfaz 100% basada en **Bootstrap 5 (sin CSS personalizado)**.

> El sistema cubre el flujo completo: **catálogo → producción → costos de lote → inventario → ventas → utilidad bruta**.

---

## ✨ Características

### Funcionalidades Implementadas ✅

- ✅ Gestión de catálogo de dulces
- ✅ Registro de lotes de producción
- ✅ Costeo por lote (materiales + mano de obra + costos indirectos)
- ✅ Cálculo de costo unitario automático
- ✅ Movimientos de inventario (entradas y salidas)
- ✅ Trazabilidad lote ↔ venta
- ✅ Ventas con costo histórico por ítem
- ✅ Dashboard ejecutivo con KPI clave
- ✅ Seed demo de inicio a fin
- ✅ UI responsive con Bootstrap 5 puro

### Próximamente 🔄

- 🔄 Reportes PDF y Excel
- 🔄 Módulo de compras y proveedores
- 🔄 Multi-sucursal y multi-bodega
- 🔄 API REST para e-commerce / POS
- 🔄 Alertas de stock mínimo por producto

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Versión |
|------------|------------|---------|
| Backend | Django | 5.1.x |
| Base de Datos | PostgreSQL | 16 |
| Contenedores | Docker / Compose | latest |
| Frontend | Bootstrap | 5.3.x |
| Lenguaje | Python | 3.12 |

---

## 📁 Estructura del Proyecto

```bash
candyflow/
├── apps/
│   ├── catalog/
│   ├── production/
│   ├── inventory/
│   ├── sales/
│   └── core/
├── config/
├── templates/
│   ├── base/
│   ├── core/
│   ├── catalog/
│   ├── production/
│   ├── inventory/
│   └── sales/
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── requirements.txt
├── manage.py
└── README.md
```

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Clonar y entrar
```bash
git clone <tu-repo>
cd <tu-repo>/candyflow
```

### 2. Ejecutar con Docker
```bash
docker compose up --build
```

### 3. URL del sistema
```bash
http://localhost:8000
```

### 4. Flujo demo pre-cargado
El contenedor ejecuta automáticamente:
- `python manage.py migrate`
- `python manage.py seed_demo`
- `python manage.py runserver 0.0.0.0:8000`


### 5. Generar ZIP local (entrega)
```bash
chmod +x scripts_make_zip.sh
./scripts_make_zip.sh
```

---

## 🧩 Mapeo End-to-End del negocio

1. **Catálogo**: defines los dulces y precio de venta.
2. **Producción**: registras lote, cantidades y costos.
3. **Costeo**: el sistema calcula costo total y unitario por lote.
4. **Inventario**: entradas por producción y salidas por venta.
5. **Ventas**: cada ítem guarda costo unitario snapshot para margen real.
6. **Dashboard**: resume ingresos, COGS, utilidad y stock.

---

## 📊 Entidades principales

- `Candy`: maestro de productos.
- `ProductionBatch`: lote de fabricación.
- `MaterialUsage`: consumo de insumos por lote.
- `InventoryMovement`: trazabilidad de entradas/salidas.
- `Sale` y `SaleItem`: venta comercial y margen por línea.

---

## 🧪 Comandos útiles

```bash
# Migraciones
python manage.py migrate

# Cargar demo
python manage.py seed_demo

# Ejecutar local (si no usas docker)
python manage.py runserver
```

---

---

## 👨‍💻 Desarrollado por Isaac Esteban Haro Torres

**Ingeniero en Sistemas · Full Stack Developer · Automatización · Data**

### 📞 Contacto

- 📧 **Email:** zackharo1@gmail.com
- 📱 **WhatsApp:** [+593 988055517](https://wa.me/593988055517)
- 💻 **GitHub:** [ieharo1](https://github.com/ieharo1)
- 🌐 **Portafolio:** [ieharo1.github.io](https://ieharo1.github.io/portafolio-isaac.haro/)

---

## 📄 Licencia

© 2026 Isaac Esteban Haro Torres - Todos los derechos reservados.

---

⭐ Si te gustó el proyecto, ¡dame una estrella en GitHub!
