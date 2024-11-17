import string
import random
from pathlib import Path
from typing import Union, Literal

import numpy as np
import pandas as pd

from data.sql.sql_utils import get_bq

RERUN = False
salt = ''.join(random.choices(population=string.ascii_uppercase,
                              k=5))
bqsql_path = 'data/sql/get_era.bqsql'
df_outpath = 'data/downloads/era.csv'

if Path(df_outpath).is_file() and RERUN is False:
    pass
else:
    df = get_bq(bqsql_path, params= {"salt": salt})
    bins = [0, 0.4, 0.8, 1.2, 1.6, np.inf]
    names = ['1', '2', '3', '4', '5']
    df['era_standard'] = pd.cut(df['rci_world'], bins, labels=names)
    df.to_csv(df_outpath)
