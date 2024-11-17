from pathlib import Path
from typing import Union
import pandas_gbq
import pandas as pd
from jinja2 import Environment, FileSystemLoader


def get_bq(query_path: Union[Path, str],
           params: dict) -> pd.DataFrame:
    
    env = Environment(loader = FileSystemLoader(''))
    template = env.get_template(query_path)
    query = template.render(params=params)
    df = pandas_gbq.read_gbq(query,
                             project_id='coki-scratch-space')
    return df
