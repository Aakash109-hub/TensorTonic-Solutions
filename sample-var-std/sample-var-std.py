import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    n = len(x)
    mean = np.mean(x)

    var = np.sum((x - mean)**2)/ (n-1)

    sd = np.sqrt(var)

    return var, sd

