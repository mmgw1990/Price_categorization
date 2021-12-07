import matplotlib.pyplot as plt
import numpy as np
from initialize_configuration_file import cfg
import glob
import random
from datetime import datetime

  
# csv files in the path
files = glob.glob(cfg['fake_input_data']['path'] + '*.csv')

csv_load = np.loadtxt(files[0], delimiter=',')
#col_number = random.randint(0, csv_load.shape[1]-1)
col_number = 1
data_to_histogram = np.empty((csv_load.shape[0], 2))
data_to_histogram[:,0] = csv_load[:, col_number]
hist, bin_edges = np.histogram(data_to_histogram[:,0], bins=4, density=True)
price_categories = ['low', 'medium', 'high', 'vip']
#price_categorized = np.empty((data_to_histogram.shape[0], 2))
#price_categorized

for i in range(0, len(bin_edges) - 1, 1):
    if i == len(bin_edges) - 2:
        result = (data_to_histogram[:,0] >= bin_edges[i])\
            & (data_to_histogram[:,0] <= bin_edges[i+1])

    else:
        result = (data_to_histogram[:,0] >= bin_edges[i])\
            & (data_to_histogram[:,0] < bin_edges[i+1])

    indexes_result = np.where(result == True)
    data_to_histogram[indexes_result, 1] = i + 1
    print('checkpoint')

now = datetime.now() # current date and time
date_time = now.strftime("%Y%m%d_%H%M%S")
np.savetxt(cfg['fake_output_data']['path'] + '{}_fake_price_data.csv'.format(date_time), data_to_histogram, delimiter=',')
print("haha")

_ = plt.hist(data_to_histogram[:,0], bins=4)  # arguments are passed to np.histogram
plt.title("Histogram with 4 bins")
plt.show()

