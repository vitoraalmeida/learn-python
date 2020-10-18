import os
import requests
from download_util import download_file

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

downloaded_img_path = os.path.join(DOWNLOAD_DIR, '1.jpg')
url = "https://external-preview.redd.it/FDllJsaDgH0jL1hiqPI2d68PFBw0bLMFRGYbEW6Gyfc.jpg?auto=webp&s=1328aba4f95d89295b65cb4dbc6cdb7a3e9c88f8"

# para itens razoavelmente pequenos
#r = requests.get(url, stream=True)
#r.raise_for_status() # 200
#with open(downloaded_img_path, 'wb') as f:
#    f.write(r.content)

download_file(url, DOWNLOAD_DIR, "f2.jpg")
