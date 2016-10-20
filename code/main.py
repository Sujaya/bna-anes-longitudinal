import pandas as pd
import numpy as np

if __name__ == '__main__':
	df = pd.read_stata('../data/anes_timeseries_cdf.dta')
	
	df.info()
	