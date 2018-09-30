import os
import numpy as np
from PIL import Image

from download import prepare_images
from path import *

# Download images
# prepare_images()


images_dir = os.path.join(os.getcwd(), DOWNLOAD_DIR)
filepath = os.path.join(images_dir, '01.png')
im = Image.open(filepath).convert('RGB')
im_array = np.asarray(im)

# (w, h) should be (550, 478)
print(im_array)
