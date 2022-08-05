##

"""

    """

##

from pathlib import Path
from pathlib import PurePath

import pandas as pd
from mir_tse import save_as_prq_wo_index as sprq

wdpn = Path('wds.xlsx')  # all tse working days
prpn = Path('prices.prq')  # actual adjusted prices dataset
opn = Path('ffilled.prq')  # output

jdc = 'JDate'
tic = 'Ticker'
adc = 'AdjClose'

def main() :

  pass

  ##
  wdf = pd.read_excel(wdpn)
  wdf = wdf[jdc]

  ##
  prdf = pd.read_parquet(prpn)
  ticks = prdf[tic].drop_duplicates()

  ##
  df = pd.merge(wdf , ticks , how = 'cross')

  ##
  cdf = prdf[[jdc , tic , adc]]

  ##
  df = df.merge(cdf , how = 'outer')

  ##
  df = df.sort_values(jdc)

  ##
  gpo = df.groupby(tic)
  df1 = df.copy()
  df1[adc] = gpo[adc].ffill()

  ##
  df1 = df1.dropna()

  ##
  sprq(df1 , opn)

##


if __name__ == "__main__" :
  main()
  print(f'{PurePath(__file__).name} Done.')