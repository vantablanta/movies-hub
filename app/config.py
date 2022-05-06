class Config:
    """"""
    BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    """"""

class DevConfig(Config):
    """"""
    DEBUG = True
