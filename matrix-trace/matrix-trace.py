import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code 
    A = np.array(A)
    d = [] 
    if A.shape[0] == A.shape[1]:
        for i in range(len(A[0])):
            d.append(A[i, i])

    return sum(d)
            

