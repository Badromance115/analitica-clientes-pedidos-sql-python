# Análisis de Clientes y Pedidos con SQL + Python

Proyecto de portafolio para prácticas en **Análisis y Desarrollo de Software**, **Analítica de Datos** e **Innovación Tecnológica**.

## Demo en línea

Aplicación publicada en Streamlit:

https://5tmhlpnpr8pgljhviwroe6.streamlit.app

## Objetivo

Simular un caso real de empresa donde se analizan clientes, pedidos y ventas usando SQL, MySQL, Python, Pandas y Streamlit.

## Problema de negocio

Una empresa necesita responder:

- ¿Cuántos clientes tiene?
- ¿Qué clientes han comprado?
- ¿Qué clientes no tienen pedidos?
- ¿Cuánto compró cada cliente?
- ¿Qué ciudad genera más ventas?
- ¿Qué clientes están activos o inactivos?

## Tecnologías

- MySQL
- SQL
- Python
- Pandas
- Streamlit
- Plotly

## Funcionalidades del dashboard

- Métricas principales de clientes, pedidos, ventas y clientes sin pedidos.
- Tabla combinada de clientes y pedidos.
- Filtro por ciudad.
- Visualización de ventas por ciudad.
- Identificación de clientes sin pedidos.

## Estructura

```text
analitica-clientes-pedidos-sql-python/
├── README.md
├── requirements.txt
├── runtime.txt
├── .gitignore
├── database/
│   ├── schema_mysql.sql
│   └── seed_mysql.sql
├── data/
│   ├── clientes.csv
│   └── pedidos.csv
├── src/
│   └── analisis_clientes_pedidos.py
├── app/
│   └── dashboard_streamlit.py
└── docs/
    └── preguntas_entrevista.md
```

## Ejecutar análisis

```bash
pip install -r requirements.txt
python src/analisis_clientes_pedidos.py
```

## Ejecutar dashboard

```bash
streamlit run app/dashboard_streamlit.py
```

## Consultas clave

### Clientes sin pedidos

```sql
SELECT c.id, c.nombre, c.ciudad
FROM cliente AS c
LEFT JOIN pedido AS p
ON c.id = p.id_cliente
WHERE p.id_pedido IS NULL;
```

### Total comprado por cliente

```sql
SELECT c.nombre, COALESCE(SUM(p.valor), 0) AS total_compras
FROM cliente AS c
LEFT JOIN pedido AS p
ON c.id = p.id_cliente
GROUP BY c.nombre;
```

### Ventas por ciudad

```sql
SELECT c.ciudad, SUM(p.valor) AS total_ventas
FROM cliente AS c
INNER JOIN pedido AS p
ON c.id = p.id_cliente
GROUP BY c.ciudad
ORDER BY total_ventas DESC;
```

## Qué demuestra

- Creación de tablas relacionales.
- Uso de claves primarias y foráneas.
- Consultas con SELECT, WHERE, GROUP BY, HAVING, JOIN, LEFT JOIN, CASE y COALESCE.
- Análisis con Python y Pandas.
- Creación de dashboard con Streamlit.
- Publicación de una aplicación web de datos.
- Documentación profesional de un proyecto técnico.
