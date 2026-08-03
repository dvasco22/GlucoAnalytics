"""
=========================================================
GlucoAnalytics v2.0

Módulo:
    loader.py

Responsabilidad:
    Cargar y validar un archivo Excel.

Autor:
    Diego Vasco

Versión:
    1.0.0
=========================================================
"""
from modules.exceptions import InvalidColumnsError
from importlib.resources import path
from os import path
from pathlib import Path
import logging

import pandas as pd

from modules.constants import EXPECTED_COLUMNS
from modules.dataset import Dataset
from modules.exceptions import (
    InvalidFileError,
    InvalidExcelFormatError,
    MissingSheetError,
)

logger = logging.getLogger(__name__)


class Loader:
    """
    Responsable de cargar un archivo Excel.
    """
    def __init__(self) -> None:
        logger.info("Loader inicializado")

    def load(self, file_path: str) -> Dataset:
        """
        Punto de entrada principal.
        """

        path = Path(file_path)
        
        logger.info("Iniicio de carga del archivo...")
        
        self._check_file(path)
        self._validate_sheet(path)
        df = self._read_excel(path) 
        self._validate_columns(df)
        df = self._clean_dataframe(df)

        print(df.head())

        raise NotImplementedError(
            "Siguiente paso: reemplazar valores vacíos"
        )


    def _check_file(self, path: Path) -> None:
       """
       Comprueba que el archivo existe y que tiene
       una extensión compatible.
       """

       logger.info("Comprobando archivo: %s", path)

       if not path.exists():
          raise InvalidFileError(
              f"El archivo '{path}' no existe."
        )

       if not path.is_file():
          raise InvalidFileError(
              f"'{path}' no es un archivo."
        )

       if path.suffix.lower() != ".xlsx":
           raise InvalidExcelFormatError(
              f"Formato no soportado: '{path.suffix}'. "
              "Actualmente solo se admiten archivos .xlsx."
        )

       logger.info("Archivo validado correctamente.")

    def _validate_sheet(self, path: Path) -> None:
        """
        Comprueba que exista una hoja con el mismo nombre
        que el archivo (sin la extensión).
        """

        logger.info("Validando hoja del Excel...")

        try:
            excel = pd.ExcelFile(path, engine="openpyxl")

        except Exception as e:
            raise InvalidExcelFormatError(
                f"No se pudo abrir el archivo '{path.name}'."
            ) from e

        expected_sheet = path.stem

        if expected_sheet not in excel.sheet_names:
            raise MissingSheetError(
                f"No existe la hoja '{expected_sheet}'. "
                f"Hojas disponibles: {excel.sheet_names}"
            )

        logger.info(f"Hoja '{expected_sheet}' validada correctamente.")

    def _read_excel(self, path: Path) -> pd.DataFrame:
        """
        Lee el archivo Excel y devuelve un DataFrame.
        """

        logger.info("Leyendo archivo Excel...")

        try:
            df = pd.read_excel(
                path,
                sheet_name=path.stem,
                engine="openpyxl"
            )

            logger.info("Excel leído correctamente")

            return df

        except Exception as e:
            raise InvalidExcelFormatError(
                f"No se pudo leer el archivo '{path.name}'."
            ) from e

    def _validate_columns(self, df: pd.DataFrame) -> None:
        """
        Valida que el DataFrame contenga todas las columnas obligatorias.
        """

        logger.info("Validando columnas...")

        found_columns = set(df.columns)

        missing_columns = EXPECTED_COLUMNS - found_columns
        extra_columns = found_columns - EXPECTED_COLUMNS


        errors = []

        if missing_columns:
           errors.append(
               f"Faltan columnas: {sorted(missing_columns)}"
        )

        if extra_columns:
             logger.warning(
             "Columnas desconocidas: %s",
             sorted(extra_columns)
        )

        if errors:
           raise InvalidColumnsError("\n".join(errors))

        logger.info("Columnas validadas correctamente.")

    def _trim_strings(self, df: pd.DataFrame) -> pd.DataFrame:
       """
       Elimina espacios al principio y al final de todas las cadenas
       del DataFrame.
       """

       logger.info("Eliminando espacios en blanco...")

       df = df.copy()

       object_columns = df.select_dtypes(include="object").columns

       for column in object_columns:
           df[column] = df[column].str.strip()

       return df

    def _clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:

       logger.info("Limpiando DataFrame...")
       
       df = self._trim_strings(df)
       df = self._replace_empty_values(df)

       return df

    def _replace_empty_values(self, df: pd.DataFrame) -> pd.DataFrame:
            """
            Reemplaza cadenas vacías o formadas únicamente por espacios
            por valores nulos (pd.NA).
            """

            logger.info("Reemplazando valores vacíos...")

            df = df.copy()

            object_columns = df.select_dtypes(include="object").columns

            for column in object_columns:

                 df[column] = (
                 df[column]
                 .replace(r"^\s*$", pd.NA, regex=True)
               )

            return df

