
class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI= 'sqlite:///project.db'


class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI=''


config_options = {
    "dev": DevelopmentConfig,
    "prd": DevelopmentConfig
}