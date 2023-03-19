class Config:
    DB_NAME: str = 'name'
    DB_USER: str = 'user'
    DB_PASSWORD: str = 'password'
    DB_HOST: str = 'myapp'
    DB_PORT: int = 5432
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'