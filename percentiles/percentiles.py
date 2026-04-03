import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.sort(np.array(x))
    q = np.sort(np.array(q))

    res = np.percentile(x, q, method = 'linear')

    return res