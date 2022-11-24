from datetime import datetime 
from pathlib import Path
from typing import List, Union

import pandas as pd
from tqdm import tqdm


def parse_meta_file(file: Union[str, Path]) -> pd.DataFrame:
    if isinstance(file, Path):
        assert file.exists(), "The path does not exist!"
        file = str(file)
    return pd.read_csv(file, sep="\t")


def parse_text_file(file: Union[str, Path]) -> pd.DataFrame:
    if isinstance(file, Path):
        assert file.exists(), "The path does not exist!"
        file = str(file)
    with open(file, "r") as f:
        contents = f.readlines()
    IDs = [i.split()[0] for i in contents]
    texts = [" ".join(i.split()[1:]) for i in contents]

    return pd.DataFrame(data={
        "ID": IDs,
        "Text": texts
    })