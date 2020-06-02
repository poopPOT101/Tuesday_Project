from glob import glob
from pathlib import Path


path = str(Path('Gui/Images/*'))
Files = glob(path)
for file in Files:
    x, y = file.split('Gui\Images\\')
    without, z = y.split('.')
    print(y)