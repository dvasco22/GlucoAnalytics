"""
=========================================================
GlucoAnalytics v2.0
dataset.py

Contenedor de datos compartido entre módulos.

Autor: Diego Vasco
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List

import pandas as pd


@dataclass
class Dataset:
    """
    Contenedor principal de datos de GlucoAnalytics.

    Todos los módulos trabajarán con esta clase.
    """

    # -----------------------------------------
    # Datos
    # -----------------------------------------

    df: pd.DataFrame

    # -----------------------------------------
    # Información del origen
    # -----------------------------------------

    source_file: str

    sheet_name: str

    loaded_at: datetime = field(default_factory=datetime.now)

    # -----------------------------------------
    # Validaciones
    # -----------------------------------------

    errors: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)

    # -----------------------------------------
    # Métodos
    # -----------------------------------------

    @property
    def rows(self) -> int:
        """Número de registros."""

        return len(self.df)

    @property
    def columns(self) -> int:
        """Número de columnas."""

        return len(self.df.columns)

    @property
    def is_valid(self) -> bool:
        """Indica si existen errores."""

        return len(self.errors) == 0

    def add_error(self, message: str) -> None:
        """Añade un error."""

        self.errors.append(message)

    def add_warning(self, message: str) -> None:
        """Añade una advertencia."""

        self.warnings.append(message)

    def summary(self) -> str:
        """
        Devuelve un resumen de la carga.
        """

        return (
            f"Archivo      : {self.source_file}\n"
            f"Hoja         : {self.sheet_name}\n"
            f"Registros    : {self.rows}\n"
            f"Columnas     : {self.columns}\n"
            f"Errores      : {len(self.errors)}\n"
            f"Advertencias : {len(self.warnings)}"
        )

    def __str__(self) -> str:
        return self.summary()