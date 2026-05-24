# Preguntas de entrevista para explicar este proyecto

## Que problema resuelve

Ayuda a una empresa a analizar clientes, pedidos y ventas para saber quien compro, quien no ha comprado y que ciudades generan mas ventas.

## Que es una clave primaria

Es un identificador unico para cada registro. Por ejemplo, cliente.id identifica a cada cliente.

## Que es una clave foranea

Es un campo que conecta una tabla con otra. Por ejemplo, pedido.id_cliente conecta cada pedido con un cliente.

## Para que usaste INNER JOIN

Para mostrar solo clientes que si tienen pedidos relacionados.

## Para que usaste LEFT JOIN

Para mostrar todos los clientes, incluso los que no tienen pedidos.

## Como encontraste clientes sin pedidos

Usando LEFT JOIN y filtrando con IS NULL.

## Para que sirve COALESCE

Para reemplazar valores vacios. En este proyecto sirve para mostrar 0 cuando un cliente no tiene compras.
