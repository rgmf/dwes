from datetime import datetime, date, time, timedelta, timezone
from zoneinfo import ZoneInfo


###############################################################################
# Fechas y horas
###############################################################################

# Objetos que solo contienen la fecha.
d1: date = date(year=2020, month=10, day=1)

# Objetos que solo contienen la hora.
t1: time = time(hour=10, minute=30, second=15, microsecond=950)
t2: time = time(hour=10)
t3: time = time(minute=25)
t4: time = time(second=3)


###############################################################################
# Datetimes
###############################################################################

# Creamos un objeto datetime pasando todos los atributos posibles.
#
# 1 de octubre de 2020, a las 10:30:10.950 UTC (aware datetime).
dt1: datetime = datetime(
    year=2020,
    month=10,
    day=1,
    hour=10,
    minute=30,
    second=10,
    microsecond=950,
    tzinfo=timezone.utc
)

# Los únicos atributos obligatorios son: year, month y day.
#
# 1 de octubre de 2020, a las 00:00:00.000 sin información de zona horaria.
dt2: datetime = datetime(year=2020, month=10, day=1)

# Si imprimes por pantalla los datetime, verás una representación de la hora
# (en str):
print(dt1)  # Imprime: "2020-10-01 10:30:10.000950+00:00"
print(dt2)  # Imprime: "2020-10-01 00:00:00"


###############################################################################
# Timedeltas
###############################################################################

# A las fechas le podemos sumar/restar días, horas, minutos y/o segundos con
# timedelta. Esta clase permite indicar desviaciones horarias. Por ejemplo,
# la siguiente fecha es igual que "dt2" pero sumándole una semana.
dt2_one_week_ahead: datetime = dt2 + timedelta(days=7)


###############################################################################
# Datetimes con manejo de zonas horarias
###############################################################################

# Puedo obtener la hora de ahora (en el sistema local, sin información de
# timezone).
dt_now: datetime = datetime.now()

# Lo mismo de arriba con información horaria (UTC).
dt_now_tz: datetime = datetime.now(timezone.utc)

# Los mismo de arriba usando el huso UTC+2. Con un timedelta ponemos el +2 en
# la zona horaria.
tz_utc_2: timezone = timezone(timedelta(hours=2))
dt_now_tz_2: datetime = datetime.now(tz_utc_2)

# Los mismo de arriba usando el huso UTC-2. Ahora le quitamos 2 horas al
# timezone.
tz_utc_minus_2: timezone = timezone(timedelta(hours=-2))
dt_now_tz_minus_2: datetime = datetime.now(tz_utc_minus_2)

# Puedes usar el módulo zoneinfo para indicar la zona horaria usando los
# nombres definidos por la IANA (zonas horarias).
#
# Por ejemplo, la zona horaria de Madrid.
zone_info_madrid: ZoneInfo = ZoneInfo("Europe/Madrid")
dt_madrid: datetime = datetime.now(zone_info_madrid)


###############################################################################
# De fecha a str: formateo de datetime/date/time
###############################################################################

# Se usa el método strftime(<format>) para crear un str que represente la
# fecha/hora bajo un control de una cadena de caracteres de formato explícito.
#
# Se usan directivas o códigos de formato que puedes ver aquí:
# https://docs.python.org/es/3/library/datetime.html#strftime-and-strptime-format-codes

dt1_str: str = dt1.strftime("Fecha: %d/%m/%Y. Hora: %H:%M:%S")

# Usamos formato ISO-8601 para una fecha con zona horaria UTC.
dt_now_tz_iso8600: str = dt_now_tz.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

# ISO-8600 para la fecha/hora de Madrid.
dt_madrid_iso8600: str = dt_madrid.strftime("%Y%m%dT%H:%M:%S.%f%z")

# Más fácil: si quieres la hora en ISO-8600, usa isoformat().
dt_madrid_iso8600: str = dt_madrid.isoformat()


###############################################################################
# De str a datetime: crear objetos datetime a partir de cadenas o str
###############################################################################

# Tienes que usar el método strptime de la clase datetime y conocer el formato
# de la fecha: si te equivocas obtendrás un ValueError.
dt1_str: str = "2020-10-01"
dt1_dt: datetime = datetime.strptime(dt1_str, "%Y-%m-%d")

# Si tienes una fecha en formato ISO-8601, no te compliques: usa el método
# fromisoformat()
dt2_str: str = "2020-10-01T10:30:25+02:00"
dt2_dt: datetime = datetime.fromisoformat(dt2_str)


###############################################################################
# Timestamps: fechas representadas por medio de un número de segundos
# transcurridos desde la medianoche del día 01/01/1970
###############################################################################

# Puedes obtener este timestamp de un datetime usando el método timestamp()
dt1_timestamp: float = dt1.timestamp()

# Día y hora de hoy en formato timestamp
now_timestamp: float = datetime.now(timezone.utc).timestamp()

# Puedes convertir un timestamp a objeto datetime
now_in_dt: datetime = datetime.fromtimestamp(now_timestamp)
