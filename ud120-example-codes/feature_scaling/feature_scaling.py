""" quiz materials for feature scaling clustering """


### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
import numpy as np

def featureScaling(arr):
    arr = np.array(arr, dtype=float)
    max_value = max(arr)
    min_value = min(arr)
    if max_value != min_value:
        arr = (arr - min_value) / (max_value - min_value)
    return arr


# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
