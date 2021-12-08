from datetime import datetime
import numpy as np
from initialize_configuration_file import cfg

class SaveOutputCsv:

    def __init__(self):
        pass

    def save_csv(self, data):

        now = datetime.now() # current date and time
        date_time = now.strftime("%Y%m%d_%H%M%S")
        np.savetxt(cfg['fake_output_data']['path'] + '{}_fake_price_data.csv'.format(date_time), data, delimiter=',')