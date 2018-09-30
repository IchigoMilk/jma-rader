import os
import numpy as np
from PIL import Image

from download import prepare_images
from path import *


OVER_80MM = 255


# Just joke
def necessity_of_umbrella(rainfall):
  nec_s = 'C'

  if rainfall <= 1:
    nec_s = '-'
  elif rainfall <= 5:
    nec_s = 'B'
  else:
    nec_s = 'A'

  return nec_s

# Bresenham's line algorithm
def acquire_rainfall(im_array, x0, x1, y0, y1):
  necessity_list = []

  dx = x1 - x0
  dy = y1 - y0
  err = 0.0
  derr = abs(dy / dx)

  y = y0
  for x in range(x0, x1, 1):
    color = tuple(im_array[x][y])
    # print(x, y, color)

    necessity = necessity_of_umbrella(rainfall_by_color(color))
    necessity_list.append(necessity)
    # print(rainfall)

    err = err + derr
    if (err > 0.5):
      y = y + 1
      err = err - 1.0
  
  return necessity_list


def rainfall_by_color(rgb):
  max_rainfall = 0

  if rgb == (180, 0, 104):
    max_rainfall = OVER_80MM
  elif rgb == (255, 40, 0):
    max_rainfall = 80
  elif rgb == (255, 153, 0):
    max_rainfall = 50
  elif rgb == (250, 245, 0):
    max_rainfall = 30
  elif rgb == (0, 65, 255):
    max_rainfall = 20
  elif rgb == (33, 140, 255):
    max_rainfall = 10
  elif rgb == (160, 210, 255):
    max_rainfall = 5
  elif rgb == (242, 242, 255):
    max_rainfall = 1
  else:
    max_rainfall = 0

  return max_rainfall


# Download images
prepare_images()

images_dir = os.path.join(os.getcwd(), DOWNLOAD_DIR)
x0, y0 = 230, 247
x1, y1 = 235, 252
# (w, h) should be (550, 478)

print('< 1[mm/h]: \' \' 傘いらん')
print('< 5[mm/h]: \'B\' 傘いるかも')
print('>=5[mm/h]: \'A\' 傘必須')
print('\t自宅......................労場')

for i in range(1, NOWCAST_NUM, 1):
  filepath = os.path.join(images_dir, '{0:02d}.png'.format(i + 1))
  im = Image.open(filepath).convert('RGB')
  im_array = np.asarray(im)

  minutes_later = i * 5
  necessity_list = acquire_rainfall(im_array, x0, x1, y0, y1)
  s = ' '.join(necessity_list)
  print('{0:02d} 分後\t{1}'.format(minutes_later, s))
