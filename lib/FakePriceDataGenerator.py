import numpy as np
import random
from datetime import datetime
from initialize_configuration_file import cfg

class FakePriceDataGenerator:

    def __init__(self):
        pass

    def generate_data(self, rows, cols):

        random_numpy = np.zeros((rows, cols))
        for i in range(0, random_numpy.shape[1], 1):
            # current status of for loop
            print('for loop interation: {}'.format(i))

            # factor random_f, standard_f for multiplication of 10^i to one of random_numpy column
            # limitation if columns numbers, i.e i goes above 10 - to avoid numbers beyond allowed integer/float range
            if cols <= 10:
                standard_f = 10**i
                random_f = 10**random.randint(0, random_numpy.shape[1] - 1)
                random_numpy[:, i] = np.random.rand(random_numpy.shape[0]) * standard_f
            else:
                standard_f = random.randint(0, 100)
                random_f = 10**random.randint(0, 3)
                random_numpy[:, i] = np.random.rand(random_numpy.shape[0]) * standard_f

            # random rows of column i multiplied by factor f
            f_row = random.randint(0, random_numpy.shape[0] - 1)
            if f_row < (random_numpy.shape[0]):
                g_row = random.randint(f_row, random_numpy.shape[0] - 1)
                random_numpy[f_row:g_row, i] = random_numpy[f_row:g_row, i] * random_f

            # random rows of column i casted to integers
            a_row = random.randint(0, random_numpy.shape[0] - 1)
            if a_row < (random_numpy.shape[0]) and i > 0:
                b_row = random.randint(a_row, random_numpy.shape[0] - 1)
                if (random_numpy[a_row:b_row, i] > 1).all():
                    random_numpy[a_row:b_row, i] = random_numpy[a_row:b_row, i].astype(int)

            
        now = datetime.now() # current date and time
        date_time = now.strftime("%Y%m%d_%H%M%S")
        np.savetxt(cfg['data']['path'] + '{}_fake_price_data.csv'.format(date_time), random_numpy, delimiter=',')
        print("Data generation completed!\n**** CSV can be found in: {}{}_fake_price_data.csv ****".format(cfg['data']['path'], date_time))
        return random_numpy