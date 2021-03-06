import numpy as np
import pandas as pd

def convert_to_numpy(data):
    if (str(type(data)) != "<class 'numpy.ndarray'>"):
        data = np.array(data, dtype='float')
        return data, str(type(data))

    return data.astype('float64'), str(type(data))

def convert_numpy(data, to):
    if (to == "<class 'pandas.core.series.Series'>"):
        return pd.Series(data)
    elif (to == "<class 'list'>"):
        return list(data)

    return data