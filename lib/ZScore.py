import numpy as np
from scipy.stats.stats import zscore


class ZScore:
    
    def __init__(self):
        pass

    def calculate_zscore(self, input_numpy_vector):
        z_score = (input_numpy_vector - np.mean(input_numpy_vector))/np.std(input_numpy_vector)
        return z_score