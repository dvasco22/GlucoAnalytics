"""
=========================================================
GlucoAnalytics v2.0
constants.py

Constantes utilizadas por todos los módulos.

Autor: Diego Vasco
=========================================================
"""

from pathlib import Path

#MEJORA EN FUTURO
#YES_VALUE = "SI"
#NO_VALUE = "NO"
#DATE_FORMAT = "%Y-%m-%d"


# -------------------------------------------------------
# Versión
# -------------------------------------------------------

APP_NAME = "GlucoAnalytics"
APP_VERSION = "2.0.0"

# -------------------------------------------------------
# Directorios
# -------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

REPORTS_DIR = BASE_DIR / "reports"

TESTS_DIR = BASE_DIR / "tests"

# -------------------------------------------------------
# Formato de fechas
# -------------------------------------------------------

DATE_FORMAT = "%d/%m/%Y"

TIME_FORMAT = "%H:%M"

# -------------------------------------------------------
# Columnas del Excel
# -------------------------------------------------------

EXPECTED_COLUMNS = {
    "Fecha",
    "Hora",
    "Ingesta",
    "Momento",
    "Glucosa",
    "Ejercicio",
    "Insulina",
}

# -------------------------------------------------------
# Valores permitidos
# -------------------------------------------------------

VALID_INGESTAS = (
    "Desayuno",
    "Comida",
    "Cena",
)

VALID_MOMENTOS = (
    "Antes",
    "Después",
)

VALID_BOOLEAN = (
    "SI",
    "NO",
    "",
)

# -------------------------------------------------------
# Extensiones permitidas
# -------------------------------------------------------

VALID_EXTENSIONS = (
    ".xlsx",
)

SUPPORTED_EXTENSIONS = (
    ".xlsx",
    ".csv",
)

# -------------------------------------------------------
# Configuración
# -------------------------------------------------------

ENGINE = "openpyxl"