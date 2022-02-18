import requests
import dotenv
import os
from random import sample
from instagrapi import Client
from tempfile import NamedTemporaryFile

dotenv.load_dotenv()
p_key = os.getenv('PIXABAY_KEY')
p_cat = os.getenv('PIXABAY_CATEGORIES')
i_user = os.getenv('INSTAGRAM_USERNAME')
i_pass = os.getenv('INSTAGRAM_PASSWORD')

cat = sample(p_cat.split(','), 1)[0]
response = requests.get('https://pixabay.com/api/',
                        params={'key': p_key,
                                'category': cat,
                                'safesearch': 'true'}
                        ).json()
img_url = sample(response['hits'], 1)[0]['largeImageURL']
img_data = requests.get(img_url).content

f = NamedTemporaryFile(suffix='.jpg')
f.write(img_data)

instagram = Client()
instagram.login(i_user, i_pass)
instagram.photo_upload_to_story(f.name)
