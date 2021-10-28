from technical_analysis._utils.convert_datatype import convert_numpy, convert_to_numpy
import numpy as np

def DM(high, low):
    # validate data
    high, original_datatype = convert_to_numpy(high)
    low, _ = convert_to_numpy(low)

    if False in high > low:
        raise ValueError("low value is greater than high")

    # find up move and down move
    # upMove = (Today's High - Yesterday's High)
    up_move = np.zeros_like(high, dtype='float')
    up_move[0] = np.nan
    up_move[1:] = high[1:]-high[:-1]

    # downMove = (Yesterday's Low - Today's Low)
    down_move = np.zeros_like(low, dtype='float')
    down_move[0] = np.nan
    down_move[1:] = low[:-1]-low[1:]

    # finding positive dm (if UpMove > DownMove and UpMove > 0, then +DM = UpMove, else +DM = 0)
    pos_dm = np.zeros_like(high, dtype='float')
    pos_dm[0] = np.nan

    pos_dm_len = len(pos_dm)
    for index in range(1,pos_dm_len):
        if (up_move[index] > down_move[index] and up_move[index] > 0):
            pos_dm[index] = up_move[index]
        else:
            pos_dm[index] = 0

    # finding negative dm (if DownMove > UpMove and DownMove > 0, then -DM = DownMove, else -DM = 0)
    neg_dm = np.zeros_like(high, dtype='float')
    neg_dm[0] = np.nan

    neg_dm_len = len(neg_dm)
    for index in range(1, neg_dm_len):
        if (up_move[index] < down_move[index] and down_move[index] > 0):
            neg_dm[index] = down_move[index]
        else:
            neg_dm[index] = 0
    
    return convert_numpy(pos_dm, to=original_datatype), convert_numpy(neg_dm, to=original_datatype)