import matplotlib.pyplot as plt
from initialize_configuration_file import cfg
from datetime import datetime
import time

class PlotHistogram:

    def __init__(self):
        self.out_path = cfg['output_plots']['path']
        self.bins_number = cfg['price_category']['number']
    
    def plot_histogram(self, input_vector):
        now = datetime.now() # current date and time
        date_time = now.strftime("%Y%m%d_%H%M%S")
        plt.figure()
        n, bins, patches = plt.hist(input_vector, bins=self.bins_number, density=False)
        plt.xticks(bins) 
        plt.grid(color='white', lw=0.5, axis='x')
        plt.title("Number of prices within one of 4 price categories")
        plt.savefig(self.out_path + "{}_histogram.png".format(date_time))
        plt.close()
        time.sleep(1) # sleep time to avoid overwriting png files

