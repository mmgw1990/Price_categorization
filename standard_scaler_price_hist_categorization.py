import glob
from initialize_configuration_file import cfg
import numpy as np
from lib import HistogramPriceCategorization, ZScore, SaveOutputCsv, PlotHistogram
import random
from scipy import stats
from datetime import datetime
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

saveCSV = SaveOutputCsv.SaveOutputCsv()
scaler = StandardScaler()
plotting = PlotHistogram.PlotHistogram()



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

# standardize data with StandardScaler
standardscaler_price_vector = scaler.fit_transform(raw_price_vector.reshape(-1,1))
# Categorizing fake input price data using histogram's bin edges, and saving output into /data/pricecategorizeddata
standardscaler_output = histogram_categorization.categorize_prices_with_hist(standardscaler_price_vector.reshape(-1), ZSCORE = True)
# plotting standardized data
plotting.plot_histogram(standardscaler_output[:,0])
# plotting raw/unstandardized data
standardscaler_output[:,0] = raw_price_vector
plotting.plot_histogram(standardscaler_output[:,0])
#saving to file categorized, raw/unstandardized data
saveCSV.save_csv(standardscaler_output)
