class Config:
    DB_NAME: str = 'db_name'
    DB_USER: str = 'db_user'
    DB_PASSWORD: str = 'db_password'
    DB_HOST: str = 'db'
    DB_PORT: int = 5432
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'