# Guía Rápida: Datos Intradiarios (Horarios) - CryptoQuant SDK

## Resumen

Este SDK ahora soporta completamente consultas de datos intradiarios (horarios) además de datos diarios. La funcionalidad ha sido optimizada para garantizar que los query parameters funcionen correctamente con datos horarios.

## ¿Qué Cambió?

### Antes (Solo Datos Diarios)
```python
# Solo funcionaba con window='day'
response = client.get_btc_exch_reserve(
    exchange='binance',
    window='day',
    from_='20240101',
    to_='20240131'
)
```

### Ahora (Datos Diarios + Intradiarios)
```python
# Datos horarios con validación automática
response = client.get_btc_exch_reserve(
    exchange='binance',
    window='hour',                # ✓ Soporte para datos horarios
    from_='20240101T000000',     # ✓ Formato con hora validado automáticamente
    to_='20240101T235959',       # ✓ Formato con hora validado automáticamente
    limit=24
)

# Datos diarios siguen funcionando igual
response = client.get_btc_exch_reserve(
    exchange='binance',
    window='day',
    from_='20240101',
    to_='20240131'
)
```

## Requisitos para Consultas Intradiarias

### 1. Parámetro Window
- Usar `window='hour'` para datos horarios
- Usar `window='day'` para datos diarios (como antes)

### 2. Formato de Timestamps
Para `window='hour'`, los timestamps **deben** incluir el componente de hora:
- ✓ Correcto: `'20240101T120000'` (formato: YYYYMMDDTHHMMSS)
- ✗ Incorrecto: `'20240101'` (falta la hora)

Para `window='day'`, ambos formatos son válidos:
- ✓ `'20240101'` (solo fecha)
- ✓ `'20240101T120000'` (fecha con hora)

## Nuevas Funcionalidades

### 1. Validación Automática de Timestamps

El SDK ahora valida automáticamente que los timestamps tengan el formato correcto:

```python
# Esto generará un ValueError con un mensaje claro
response = client.get_btc_exch_reserve(
    exchange='binance',
    window='hour',
    from_='20240101',  # Error: falta componente de hora
    to_='20240101'     # Error: falta componente de hora
)

# Error message:
# "For intraday queries (window='hour'), 'from' timestamp must be in format 
#  YYYYMMDDTHHMMSS. Got: '20240101'. Example: '20240101T120000'"
```

### 2. Métodos de Ayuda para Formateo

#### Validar Timestamps
```python
from cryptoquant.request_handler_class import RequestHandler

# Validar antes de hacer la consulta
is_valid = RequestHandler.validate_timestamp('20240101T120000', 'hour')
print(is_valid)  # True

is_valid = RequestHandler.validate_timestamp('20240101', 'hour')
print(is_valid)  # False
```

#### Formatear Timestamps desde Objetos datetime
```python
from cryptoquant.request_handler_class import RequestHandler
from datetime import datetime

# Crear timestamp desde datetime
dt = datetime(2024, 1, 15, 14, 30, 0)
timestamp = RequestHandler.format_timestamp_for_window(dt, 'hour')
print(timestamp)  # '20240115T143000'

# Usar en consultas
response = client.get_btc_exch_reserve(
    exchange='binance',
    window='hour',
    from_=RequestHandler.format_timestamp_for_window(dt, 'hour'),
    to_=RequestHandler.format_timestamp_for_window(dt + timedelta(hours=12), 'hour')
)
```

## Ejemplos Completos

### Ejemplo 1: Reservas de Exchange por Hora
```python
from cryptoquant import CryptoQuant
import os

api_key = os.environ['CQ_API']
client = CryptoQuant(api_key)

# Obtener reservas horarias de BTC en Binance para un día
response = client.get_btc_exch_reserve(
    exchange='binance',
    window='hour',
    from_='20240101T000000',
    to_='20240101T235959',
    limit=24
)

# Procesar datos
if 'result' in response and 'data' in response['result']:
    for datapoint in response['result']['data']:
        print(f"Timestamp: {datapoint['datetime']}, Reserve: {datapoint['value']}")
```

### Ejemplo 2: Flujos Netos Horarios (Netflows)
```python
from cryptoquant import CryptoQuant
from datetime import datetime, timedelta
from cryptoquant.request_handler_class import RequestHandler

api_key = os.environ['CQ_API']
client = CryptoQuant(api_key)

# Definir rango de tiempo usando objetos datetime
start_time = datetime(2024, 1, 15, 0, 0, 0)
end_time = start_time + timedelta(hours=12)

# Formatear timestamps
from_ts = RequestHandler.format_timestamp_for_window(start_time, 'hour')
to_ts = RequestHandler.format_timestamp_for_window(end_time, 'hour')

# Consultar netflows horarios
response = client.get_btc_exch_netflow(
    exchange='kraken',
    window='hour',
    from_=from_ts,
    to_=to_ts,
    limit=12
)
```

### Ejemplo 3: Múltiples Métricas con Granularidad Horaria
```python
from cryptoquant import CryptoQuant
import os

api_key = os.environ['CQ_API']
client = CryptoQuant(api_key)

# Parámetros comunes
params = {
    'exchange': 'binance',
    'window': 'hour',
    'from_': '20240115T000000',
    'to_': '20240115T120000',
    'limit': 12
}

# Obtener múltiples métricas horarias
reserves = client.get_btc_exch_reserve(**params)
inflows = client.get_btc_exch_inflow(**params)
outflows = client.get_btc_exch_outflow(**params)
netflows = client.get_btc_exch_netflow(**params)

print(f"Reserves data points: {len(reserves['result']['data'])}")
print(f"Inflows data points: {len(inflows['result']['data'])}")
print(f"Outflows data points: {len(outflows['result']['data'])}")
print(f"Netflows data points: {len(netflows['result']['data'])}")
```

### Ejemplo 4: Formato CSV para Datos Horarios
```python
from cryptoquant import CryptoQuant
import os

api_key = os.environ['CQ_API']
client = CryptoQuant(api_key)

# Obtener datos en formato CSV
response = client.get_btc_exch_reserve(
    exchange='coinbase',
    window='hour',
    from_='20240101T000000',
    to_='20240101T060000',
    limit=6,
    format_='csv'  # Formato CSV
)

# response será un string CSV
print(response)
# datetime,value
# 2024-01-01T00:00:00,123456.78
# 2024-01-01T01:00:00,123450.45
# ...
```

## Compatibilidad hacia Atrás

Todas las consultas existentes de datos diarios continúan funcionando sin cambios:

```python
# Este código sigue funcionando exactamente igual
response = client.get_btc_exch_reserve(
    exchange='binance',
    window='day',
    from_='20240101',
    to_='20240131',
    limit=31
)
```

## Endpoints que Soportan Datos Horarios

Todos los endpoints que aceptan el parámetro `window` ahora soportan `window='hour'`:

### Bitcoin
- Exchange flows (reserves, inflows, outflows, netflows)
- Miner flows
- Network indicators
- Flow indicators
- Market indicators

### Ethereum
- Exchange flows
- Network data
- Market data

### Otros Assets
- Stablecoins
- ERC-20 tokens
- XRP
- TRX
- Altcoins

## Solución de Problemas

### Error: Timestamp formato incorrecto
**Problema:**
```python
ValueError: For intraday queries (window='hour'), 'from' timestamp must be in format 
YYYYMMDDTHHMMSS. Got: '20240101'. Example: '20240101T120000'
```

**Solución:**
- Cambiar `from_='20240101'` a `from_='20240101T000000'`
- O usar el helper: `RequestHandler.format_timestamp_for_window(datetime_obj, 'hour')`

### Error: API devuelve datos vacíos
**Causas posibles:**
1. El exchange no tiene datos para ese rango de tiempo
2. El rango de tiempo está fuera del período disponible
3. El límite es demasiado pequeño

**Solución:**
- Verificar disponibilidad de datos en la documentación de CryptoQuant
- Ajustar el rango de fechas
- Aumentar el parámetro `limit`

## Recursos Adicionales

- **Documentación completa:** Ver README.md
- **Ejemplos detallados:** Ver `examples/intraday_data_example.py`
- **Demo rápida:** Ejecutar `python examples/demo_intraday.py`
- **Tests:** Ver `tests/test_intraday_support.py`

## Resumen de Mejoras

1. ✅ **Validación automática** de timestamps para consultas horarias
2. ✅ **Mensajes de error claros** cuando hay problemas con timestamps
3. ✅ **Métodos de ayuda** para formatear y validar timestamps
4. ✅ **Compatibilidad hacia atrás** con consultas diarias existentes
5. ✅ **Documentación completa** con ejemplos
6. ✅ **Suite de tests** con 18 pruebas automatizadas

---

**Fecha de actualización:** 2024
**Versión:** Compatible con CryptoQuant API v1
