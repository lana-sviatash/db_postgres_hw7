import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

user_name = config.get('DB', 'USER')
password = config.get('DB', 'PASSWORD')
db_name = config.get('DB', 'DB_NAME')
domain = config.get('DB', 'DOMAIN')
port = config.get('DB', 'PORT')

url = f'postgresql://{user_name}:{password}@{domain}:{port}/{db_name}'

engine = create_engine(url, echo=False, pool_size=5)
DBsession = sessionmaker(bind=engine)
session = DBsession()
