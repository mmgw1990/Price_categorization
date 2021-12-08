import glob
from initialize_configuration_file import cfg
import numpy as np
from lib import HistogramPriceCategorization, ZScore
import random
from scipy import stats
from datetime import datetime

score = ZScore.ZScore()

# HistogramPriceCategorization object initialization
histogram_categorization = HistogramPriceCategorization.HistogramPriceCategorization()

# getting all csv files with fake input price data
files = glob.glob(cfg['fake_input_data']['path'] + '*.csv')
# loading first found csv into workspace to variable csv_load
csv_load = np.loadtxt(files[0], delimiter=',')
# drawing random column number from fake price data from csv_load variable
if len(csv_load.shape) == 2:
    col_number = random.randint(0, csv_load.shape[1]-1)
    # chosing one column/vector of prices from csv_load
    raw_price_vector = csv_load[:, col_number]
else:
    col_number = 0
    raw_price_vector = csv_load
#standardize data with zscore
zscored_price_vector = stats.zscore(raw_price_vector, nan_policy='omit')
# Categorizing fake input price data using histogram's bin edges, and saving output into /data/pricecategorizeddata
zscored_output = histogram_categorization.categorize_prices_with_hist(zscored_price_vector, ZSCORE = True)
zscored_output[:,0] = raw_price_vector

now = datetime.now() # current date and time
date_time = now.strftime("%Y%m%d_%H%M%S")
np.savetxt(cfg['fake_output_data']['path'] + '{}_fake_price_data.csv'.format(date_time), zscored_output, delimiter=',')
