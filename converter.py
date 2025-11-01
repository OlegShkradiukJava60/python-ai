

from typing import Iterable
import pandas as pd


def enumerator(values: Iterable[str]) -> dict[str, int]:
    return {s: i for i, s in enumerate(values)}


def columnsMapper(columnsStr: list[str], df: pd.DataFrame) -> dict[str, dict[str, int]]:
    res: dict[str, dict[str, int]] = {}
    for column in columnsStr:
        uniques = list(df[column].unique())
        res[column] = enumerator(uniques)
    return res


def convertX(df: pd.DataFrame, mapper: dict[str, dict[str, int]]) -> pd.DataFrame:
    resDict: dict[str, list] = {}
    for column in df.columns:
        if column in mapper:
            col_map = mapper[column]
            resDict[column] = [col_map[v] for v in df[column]]
        else:
            resDict[column] = df[column].tolist()
    return pd.DataFrame(resDict)
