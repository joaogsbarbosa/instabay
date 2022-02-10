import os
import models
import requests
from instagrapi import Client

imagem_url = models.Pixabay().obter_imagem()
imagem_dados = requests.get(imagem_url).content
with open('imagem.jpg', 'wb') as arq:
    arq.write(imagem_dados)
cl = Client()
cl.login(os.getenv('INSTAGRAM_USERNAME'), os.getenv('INSTAGRAM_PASSWORD'))
cl.photo_upload_to_story('imagem.jpg')
