from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / 'data'

st.set_page_config(page_title='Dashboard Clientes y Pedidos', page_icon='📊', layout='wide')
st.title('Dashboard de Clientes y Pedidos')
st.write('Proyecto de portafolio con SQL, Python y análisis de datos.')

clientes = pd.read_csv(DATA_DIR / 'clientes.csv')
pedidos = pd.read_csv(DATA_DIR / 'pedidos.csv')
reporte = clientes.merge(pedidos, how='left', left_on='id', right_on='id_cliente')

col1, col2, col3, col4 = st.columns(4)
col1.metric('Clientes', clientes['id'].nunique())
col2.metric('Pedidos', pedidos['id_pedido'].nunique())
col3.metric('Ventas', f"${pedidos['valor'].sum():,.0f}")
col4.metric('Clientes sin pedidos', reporte[reporte['id_pedido'].isna()]['id'].nunique())

st.subheader('Datos combinados')
st.dataframe(reporte, use_container_width=True)

ventas_ciudad = reporte.dropna(subset=['id_pedido']).groupby('ciudad', as_index=False)['valor'].sum()
fig = px.bar(ventas_ciudad, x='ciudad', y='valor', text='valor', title='Ventas por ciudad')
st.plotly_chart(fig, use_container_width=True)

st.subheader('Clientes sin pedidos')
st.dataframe(reporte[reporte['id_pedido'].isna()][['id', 'nombre', 'ciudad', 'telefono', 'edad']], use_container_width=True)
