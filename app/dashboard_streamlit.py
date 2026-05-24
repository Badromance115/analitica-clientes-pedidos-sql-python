from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

# Configuración de rutas de archivos
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / 'data'

# Configuración de la página de Streamlit
st.set_page_config(page_title='Dashboard Clientes y Pedidos', page_icon='📊', layout='wide')
st.title('Dashboard Clientes y Pedidos')
st.write('Proyecto de portafolio con SQL, Python y análisis de datos.')

# Carga y combinación de los datos (Equivalente al LEFT JOIN de SQL)
clientes = pd.read_csv(DATA_DIR / 'clientes.csv', dtype={'telefono': str})
pedidos = pd.read_csv(DATA_DIR / 'pedidos.csv')
reporte = clientes.merge(pedidos, how='left', left_on='id', right_on='id_cliente')

# --- NUEVO: BARRA LATERAL CON FILTROS ---
st.sidebar.header("Filtros Disponibles")

# Crear una lista única de ciudades y añadir la opción "Todas"
lista_ciudades = ['Todas'] + sorted(reporte['ciudad'].unique().tolist())
ciudad_seleccionada = st.sidebar.selectbox('Selecciona una Ciudad:', lista_ciudades)

# Filtrar el DataFrame original según la selección
if ciudad_seleccionada != 'Todas':
    reporte_filtrado = reporte[reporte['ciudad'] == ciudad_seleccionada]
    clientes_filtrados = clientes[clientes['ciudad'] == ciudad_seleccionada]
    # Para los pedidos, filtramos solo los que pertenecen a los clientes de esa ciudad
    pedidos_filtrados = pedidos[pedidos['id_cliente'].isin(clientes_filtrados['id'])]
else:
    reporte_filtrado = reporte
    clientes_filtrados = clientes
    pedidos_filtrados = pedidos
# ----------------------------------------

# Sección de Tarjetas de Métricas (KPIs basados en el filtro)
col1, col2, col3, col4 = st.columns(4)
col1.metric('Clientes', clientes_filtrados['id'].nunique())
col2.metric('Pedidos', pedidos_filtrados['id_pedido'].nunique())
col3.metric('Ventas', f"${pedidos_filtrados['valor'].sum():,.0f}")
col4.metric('Clientes sin pedidos', reporte_filtrado[reporte_filtrado['id_pedido'].isna()]['id'].nunique())

# Sección de Tabla General (Filtrada)
st.subheader('Datos combinados')
st.dataframe(reporte_filtrado, use_container_width=True)

# Sección de Gráfico de Barras
ventas_ciudad = reporte_filtrado.groupby('ciudad', as_index=False)['valor'].sum()
fig = px.bar(ventas_ciudad, x='ciudad', y='valor', text='valor', title='Ventas por ciudad')
fig.update_traces(texttemplate='$%{text}:,.0f', textposition='outside')
st.plotly_chart(fig, use_container_width=True)

# Sección de Clientes sin Pedidos (Filtrada)
st.subheader('Clientes sin pedidos')
clientes_sin_pedido = reporte_filtrado[reporte_filtrado['id_pedido'].isna()][['id', 'nombre', 'ciudad', 'telefono', 'edad']]
st.dataframe(clientes_sin_pedido, use_container_width=True)