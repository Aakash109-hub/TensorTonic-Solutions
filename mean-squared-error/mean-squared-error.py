import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    n = len(y_pred)

    E = []

    for i in range(n):
        E.append((y_true[i] - y_pred[i])**2)

    E = np.array(E)

    mse = np.mean(E)

    return mse

    
