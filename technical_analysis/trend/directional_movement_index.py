from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy
import technical_analysis as ta
import numpy as np

def DMI(high, low, close, limit, moving_average_func=ta.EMA, alpha=1.071421):
    # validate data
    high, original_datatype = convert_to_numpy(high)
    low, _ = convert_to_numpy(low)
    close, _ = convert_to_numpy(close)

    if (False in high > low):
        raise ValueError("Some High values are smaller than Low values")

    # find di
    plus_di = ta.PLUS_DI(high, low, close, limit, moving_average_func, alpha)
    minus_di = ta.MINUS_DI(high, low, close, limit, moving_average_func, alpha)

    # find adx
    adx = ta.ADX(high, low, close, limit, moving_average_func, alpha)

    return np.round(convert_numpy(plus_di, to=original_datatype),2), np.round(convert_numpy(minus_di, to=original_datatype),2), np.round(convert_numpy(adx, to=original_datatype),2)

