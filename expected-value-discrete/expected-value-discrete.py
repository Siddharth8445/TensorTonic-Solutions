import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    x_arr = np.array(x, dtype = float)
    p_arr = np.array(p, dtype = float)
    
    ans = np.sum(x_arr*p_arr) 

    return float(ans)