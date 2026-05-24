from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / 'data'
REPORTS_DIR = BASE_DIR / 'reports'
REPORTS_DIR.mkdir(exist_ok=True)

clientes = pd.read_csv(DATA_DIR / 'clientes.csv')
pedidos = pd.read_csv(DATA_DIR / 'pedidos.csv')

reporte = clientes.merge(pedidos, how='left', left_on='id', right_on='id_cliente')

clientes_sin_pedidos = reporte[reporte['id_pedido'].isna()][['id', 'nombre', 'ciudad']]
ventas_por_ciudad = reporte.dropna(subset=['id_pedido']).groupby('ciudad', as_index=False)['valor'].sum()
total_por_cliente = reporte.groupby(['id', 'nombre'], as_index=False)['valor'].sum()
total_por_cliente['valor'] = total_por_cliente['valor'].fillna(0)

reporte.to_csv(REPORTS_DIR / 'clientes_pedidos.csv', index=False)
clientes_sin_pedidos.to_csv(REPORTS_DIR / 'clientes_sin_pedidos.csv', index=False)
ventas_por_ciudad.to_csv(REPORTS_DIR / 'ventas_por_ciudad.csv', index=False)
total_por_cliente.to_csv(REPORTS_DIR / 'total_por_cliente.csv', index=False)

print('Reportes generados correctamente')
print(clientes_sin_pedidos)
