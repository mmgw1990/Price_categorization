from initialize_configuration_file import cfg
import numpy as np
from datetime import datetime
from lib import SaveOutputCsv

class HistogramPriceCategorization:

    def __init__(self):
        self.savecsv = SaveOutputCsv.SaveOutputCsv()

    def categorize_prices_with_hist(self, raw_price_vector, **kwargs):
        data_to_histogram = np.empty((raw_price_vector.shape[0], 2))
        data_to_histogram[:,0] = raw_price_vector
        hist, bin_edges = np.histogram(data_to_histogram[:,0], bins=cfg['price_category']['number'], density=True)

        for i in range(0, len(bin_edges) - 1, 1):
            """
            Check if price is within any bin range, if so, assign coresponding price category.
            Price category is numerical, 1,2,3 or 4 which then can be mapped into low, medium, high, vip, respectively
            """
            # When i == len(bin_edges) - 2 close the right side of numerical range of the last histogram's bin
            if i == len(bin_edges) - 2:
                result = (data_to_histogram[:,0] >= bin_edges[i])\
                    & (data_to_histogram[:,0] <= bin_edges[i+1])
            # otherwise, leave right side of numerical range of histogram's bin opened
            else:
                result = (data_to_histogram[:,0] >= bin_edges[i])\
                    & (data_to_histogram[:,0] < bin_edges[i+1])

            # getting indexes of matched condition and assigning proper price category
            # in 2nd column of numpy data_to_histogram array
            indexes_result = np.where(result == True)
            data_to_histogram[indexes_result, 1] = i + 1
        
        # saving to csv data_to_histogram including raw prices in first column and categorization in 2nd column

        if cfg['histogram_optional_keys']['zscore'] not in kwargs:
            self.savecsv.save_csv(data_to_histogram)

        return data_to_histogram