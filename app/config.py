class Config:
    """"""
    BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    SEARCH_URL = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'

class ProdConfig(Config):
    """"""

class DevConfig(Config):
    """"""
    DEBUG = True
