import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A = np.array(A)
    n = A.shape[0]

    if A.ndim != 2 and A.shape[0] != A.shape[1]:
        return None
    
    if np.linalg.det(A) == 0:
        return None

    
    A_inv = np.linalg.inv(A)

    I = np.eye(n)

    eq_norm = np.linalg.norm((A @ A_inv) - I)

    if eq_norm < 1e-7:
        return A_inv
    

    return None


