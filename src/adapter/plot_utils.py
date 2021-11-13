from typing import List, Optional
from matplotlib import pyplot as plt


class GraphicProperties:
    BLUE_CIRCLE_MARKS = 'bo'
    GREEN_CIRCLE_MARKS = 'go'
    RED_CIRCLE_MARKS = 'ro'

    BLUE_SOLID_LINE = '-b'
    GREEN_SOLID_LINE = '-g'
    RED_SOLID_LINE = '-r'

    BLUE_DASHED_LINE = '--b'
    GREEN_DASHED_LINE = '--g'
    RED_DASHED_LINE = '--r'

    TEXT = ''


def plot(array_x1: Optional[List[float]] = None,
         array_y1: Optional[List[float]] = None,
         type_line1: Optional[str] = '',
         label_text1: Optional[str] = '',
         ):

    if array_x1 and array_y1:
        fig, ax = plt.subplots()
        ax.plot(array_x1, array_y1, type_line1, label=label_text1)
        ax.axis('equal')
        plt.show()
        return
