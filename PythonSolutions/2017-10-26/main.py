from PIL import Image
import numpy as np


def is_grey(_pixel):
    if _pixel[0] == _pixel[1] and _pixel[1] == _pixel[2]:
        return True
    return False


def roll_row(_row):
    for _i, _pixel in enumerate(_row):
        offset = _i
        if not is_grey(_pixel):
            if _i < 2:
                for _j in range(-2, 0):
                    if not is_grey(_row[_j]):
                        offset = _j
                        break
            return np.roll(_row, - offset - 3, axis=0)


def red_green_sort(_data):
    return _data[:, -1, 0]

file_name = 'input5.png'
im = Image.open(file_name)

pixels = np.array(list(im.getdata()))
image = np.reshape(pixels, (400, 400, 4))

result_data = np.ndarray((400, 400, 4), dtype=np.uint8)

for row_index, row in enumerate(image):
    rolled_row = roll_row(row)
    result_data[row_index] = rolled_row

# Needs to be stable sort
order = np.argsort(a=red_green_sort(result_data), kind='mergesort')
print(len(set(order)))

result_image = Image.fromarray(result_data[order])
result_image.show()
