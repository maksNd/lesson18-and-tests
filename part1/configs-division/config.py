class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # TODO cохраните данные настройки
    SQLALCHEMY_TRACK_MODIFICATIONS = False         # в классе Сonfig файла config.py
    API_URL = 'https://api.npoint.io/6c40daa11556af60fe4f'