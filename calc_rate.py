import pandas as pd
import numpy as np
import pprint

def result_conv_val(result):
    result_point = {
        "SSS": 2.0,
        "SS+": 1.5,
        "SS": 1.0,
        "S": 0.0,
        "AA": -3.0,
        "A": -5.0,
    }

    try:
        return result_point[result]
    except KeyError as e:
        raise ValueError('Invalid printer: {}'.format(result))

def sort_rate(path):
    df = pd.read_csv(path, header=None)
    array = np.asarray(df)
    col_num = 1
    array = array[np.argsort(array[:, col_num])]
    np.savetxt(path, array, fmt="%s", delimiter=',')

def calc_rate(path):
    df = pd.read_csv(path, header=None)
    array = np.asarray(df)

    sum = 0.0
    incomplete_list = []
    complete_tracks = 0
    incomplete_tracks = 0
    for row in array:
        name, level, result, complete = row[:]
        sum += level + result_conv_val(result)
        if complete == "F":
            incomplete_list.append([name, level, result])
            incomplete_tracks += 1
        else:
            complete_tracks += 1

    print("\nRating is {:.5g}".format(sum/len(array)))
    print("\nComplete   : {0}/{1}".format(complete_tracks, format(len(array))))
    print("Incomplete : {0}/{1}\n".format(incomplete_tracks, format(len(array))))

    pprint.pprint(incomplete_list, indent=1)

if __name__ == "__main__":
    path = 'chunithm_rate.csv'
    sort_rate(path)
    calc_rate(path)