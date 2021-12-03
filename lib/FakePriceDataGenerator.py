import numpy as np
import random
from datetime import datetime

random_numpy = np.zeros((1000, 10))
for i in range(0, random_numpy.shape[1], 1):
    random_column = random.randint(0,9)


    f = 10**i # factorial for multiplication of 10^i to one of random_numpy column
    random_numpy[:, i] = np.random.rand(random_numpy.shape[0]) * f
    a_row = random.randint(0, random_numpy.shape[0] - 1)
    if a_row < (random_numpy.shape[0] - 1) and i > 0:
        b_row = random.randint(a_row, random_numpy.shape[0] - 1)
        random_numpy[a_row:b_row, i] = random_numpy[a_row:b_row, i].astype(int)
    print('for loop interation: {}'.format(i))
now = datetime.now() # current date and time
date_time = now.strftime("%Y%m%d_%H%M%S")
np.savetxt('{}_fake_price_data.csv'.format(date_time), random_numpy, delimiter=',')
print('koniec')