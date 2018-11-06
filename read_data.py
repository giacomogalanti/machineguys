import json
import numpy as np


def load_data(filepath, ):
    with open('./shipsnet.json') as data_file:
        dataset = json.load(data_file)

    x = np.array(dataset['data']).astype('uint8')
    y = np.array(dataset['labels']).astype('uint8')

    data_file.close()
    return x, y


