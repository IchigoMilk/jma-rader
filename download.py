# coding: utf-8

import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone

from path import *

# Generate JST timezone
JST = timezone(timedelta(hours=+9), 'JST')


# Download images 01.png, 02.png,..., 12.png
def download(uri_list):
  download_dir = os.path.join(os.getcwd(), DOWNLOAD_DIR)

  for uri in uri_list:
    print(uri)
    
    filename = uri[-6:]
    filepath = os.path.join(download_dir, filename)

    res = requests.get(uri, stream=True)
    if res.status_code == 200:
      with open(filepath, 'wb') as file:
        file.write(res.content)


# List of URI
# ex. http://www.jma.go.jp/jp/radnowc/imgs/nowcast/211/201809301615-01.png
def get_nowcast_uri_list():
  # The nowcast image comes about 5 minutes later
  now = (datetime.now(JST) - timedelta(minutes=5)).strftime('%Y%m%d%H%M')
  
  if (int(now[-1]) < 5):
    now = now[:11] + '0'
  else:
    now = now[:11] + '5'

  now_uri = URI_BASE + now
  
  # Nowcast images are available up to 60 minutes from now
  nowcast_uri_list = []
  for i in range(NOWCAST_NUM):
    nowcast_uri_list.append(now_uri + '-{0:02d}.png'.format(i + 1))

  return nowcast_uri_list


def prepare_images():
  download(get_nowcast_uri_list())
