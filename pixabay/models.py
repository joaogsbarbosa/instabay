import requests
import dotenv
import os
from random import sample


class Categoria:
    def __init__(self):
        self.__categorias = os.getenv('PIXABAY_CATEGORIES')

    def obter_categoria(self):
        lista = self.__categorias.split(',')
        return sample(lista, 1)[0]


class Pixabay:
    def __init__(self):
        dotenv.load_dotenv()
        self.__key = os.getenv('PIXABAY_KEY')
        self.__categories = os.getenv('PIXABAY_CATEGORIES')

    def obter_imagem(self):
        response = requests.get('https://pixabay.com/api/',
                                params={'key': self.__key,
                                        'category': Categoria().obter_categoria(),
                                        'safesearch': 'true'}
                                ).json()
        imagem_url = sample(response['hits'], 1)[0]['largeImageURL']
        return imagem_url
