from db_setup import engine, Base
from models import trades

Base.metadata.create_all(bind=engine)