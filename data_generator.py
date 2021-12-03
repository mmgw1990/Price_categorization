import numpy as np
import random
from datetime import datetime
import os
from initialize_configuration_file import cfg

def generate_data(rows, cols):
    #cols = 10
    #rows = 1000
    random_numpy = np.zeros((rows, cols))
    for i in range(0, random_numpy.shape[1], 1):
        random_column = random.randint(0,9)

        # factor for multiplication of 10^i to one of random_numpy column
        #f = 10**i
        f = 10**random.randint(0, random_numpy.shape[1] - 1)
        random_numpy[:, i] = np.random.rand(random_numpy.shape[0])

        # random rows of column i multiplied by factor f
        f_row = random.randint(0, random_numpy.shape[0] - 1)
        if f_row < (random_numpy.shape[0] - 1):
            g_row = random.randint(f_row, random_numpy.shape[0] - 1)
            random_numpy[f_row:g_row, i] = random_numpy[f_row:g_row, i] * f

        # random rows of column i casted to integers
        a_row = random.randint(0, random_numpy.shape[0] - 1)
        if a_row < (random_numpy.shape[0] - 1) and i > 0:
            b_row = random.randint(a_row, random_numpy.shape[0] - 1)
            if (random_numpy[a_row:b_row, i] > 1).all():
                random_numpy[a_row:b_row, i] = random_numpy[a_row:b_row, i].astype(int)

        print('for loop interation: {}'.format(i))
    now = datetime.now() # current date and time
    date_time = now.strftime("%Y%m%d_%H%M%S")
    np.savetxt(cfg['data']['path'] + '{}_fake_price_data.csv'.format(date_time), random_numpy, delimiter=',')
    print('koniec')

generate_data(30, 4)

