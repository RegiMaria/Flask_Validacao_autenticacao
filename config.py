import os

class Config:
    SECRET_KEY = '1694f9e94234d4b431ffb2a3747ef6ab'
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost:5432/database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False