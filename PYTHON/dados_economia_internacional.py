import pandas as pd
import datetime as dt
# pip install pandasdmx
import pandasdmx as pdmx
# pip install seaborn
import seaborn as sns
from matplotlib import pyplot as pl

# Conecta com a base da OECD stats através do pdmx
oecd = pdmx.Request("OECD")

# Realiza o Request baseado no API disponibilizado pela OECD Statistics
## PIB
data_gdp = oecd.data(
    resource_id = "QNA",
    key = "AUS+CHL+JPN+MEX+USA+EA19+CHN+IND+RUS+SAU.B1_GE.GYSA+GPSA.Q",
    ).to_pandas()
# Transforma em data frame
gdp_raw = pd.DataFrame(data_gdp).reset_index()

# Faz o tratamento e limpeza de dados
gdp =  (
    gdp_raw[(gdp_raw.FREQUENCY == 'Q')]
    .drop(["SUBJECT", "FREQUENCY"], axis = 1)
    .rename({'LOCATION' : 'location',
             'TIME_PERIOD' : 'date',
             'MEASURE' : 'measure'}, axis = 'columns')
    .assign(date = lambda x: pd.to_datetime(x['date']),
            measure = lambda x: x['measure'].replace({'GPSA' : '% change from same quarter of previous year',
                                                      'GYSA' : '% change from previous quarter'}))
    )






