"""
=========================================================
GlucoAnalytics v2.0
exceptions.py

Excepciones propias del proyecto.

Autor: Diego Vasco
=========================================================
"""


class GlucoAnalyticsError(Exception):
    """Excepción base del proyecto."""
    pass


class InvalidFileError(GlucoAnalyticsError):
    """El archivo no existe o no puede abrirse."""
    pass


class InvalidExcelFormatError(GlucoAnalyticsError):
    """El archivo no es un Excel válido."""
    pass


class MissingSheetError(GlucoAnalyticsError):
    """No existe la hoja solicitada."""
    pass


class MissingColumnError(GlucoAnalyticsError):
    """Falta una columna obligatoria."""
    pass


class DuplicateRecordError(GlucoAnalyticsError):
    """Se han detectado registros duplicados."""
    pass


class InvalidDataError(GlucoAnalyticsError):
    """Los datos contienen valores no válidos."""
    pass

class InvalidColumnsError(GlucoAnalyticsError):
    """Las columnas del Excel no son válidas."""
    pass