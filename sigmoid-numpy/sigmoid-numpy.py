import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x)

    res = np.asarray(1 / (1 + np.exp(-x)) , dtype = float)

    return res

    