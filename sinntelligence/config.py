import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    WD = "sqlite:////" + os.path.dirname(os.path.abspath(__file__))

    SQLALCHEMY_DATABASE_URI = os.path.join(WD, DB_NAME + ".db")

    IMAGES_SAVE_DIRECTORY = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "static/images"
    )


class ProductionConfig(Config):
    DEBUG = False

    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    SQLALCHEMY_DATABASE_URI = os.path.join(Config.WD, DB_NAME + ".db")


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    SQLALCHEMY_DATABASE_URI = os.path.join(Config.WD, DB_NAME + ".db")
