# Fechas, horas y zonas horarias en Python
En Python puedes usar la clase `datetime` del módulo `datetime` para manejar fechas y horas.

Para las zonas horarias usa la clase `timezone` del módulo `datetime`. Esta clase `timezone` tiene un atributo de clase `timezone.utc` que devuelve la zona horaria UTC.

Para crear un objeto con la fecha y hora actual usa `datetime.now()`. ¡PERO OJO!, esta fecha/hora no tiene información de la zona horaria es un *naive datetime*.

Si quieres hacer lo mismo añadiendo la información de la zona horaria en UTC usa `datetime.now(timezone.utc)`. Ahora sí, tenemos un *aware datetime* y podrás usarlo para convertir la hora a la zona horaria de Madrid o de cualquier otro lugar.

## Zona horaria
Puedes crear una zona horaria con la clase `ZoneInfo` del módulo `zoneinfo`.

Por ejemplo:

```python
from zoneinfo import ZoneInfo


madrid_tz: ZoneInfo = ZoneInfo("Europe/Madrid")
```

Este código crear un objeto con la información de la zona horaria de Madrid.

Puedes convertir una hora en UTC, por ejemplo, a la hora en Madrid:

```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


madrid_tz: ZoneInfo = ZoneInfo("Europe/Madrid")

dt_now_in_utc: datetime = datetime.now(timezone.utc)

dt_now_in_madrid: datetime = dt_now_in_utc.astimezone(madrid_tz)
```

## De datetime a str (ISO-8601)
Puedes convertir un objeto `datetime` a un `str` en formato ISO-8601 así:

```python
from datetime import datetime, timezone


dt_object: datetime = datetime.now(timezone.utc)

dt_str_iso8601: str = dt_object.isoformat()
```

## De str (ISO-8601) a dateime
Al revés también puedes. Es decir, de `str` en formato ISO-8601 a un objeto `datetime`:

```python
from datetime import datetime


dt_str_iso8601: str = "2020-10-10T10:10:10+00:00"

dt_object: datetime = datetime.fromisoformat(dt_str_iso8601)
```
