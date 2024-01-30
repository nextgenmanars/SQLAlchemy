from sqlalchemy import Column, Integer, String
from database import Base, session
from models import user

class Shop(Base):
    __tablename__ = "shops"
    id = Column(Integer(), primary_key=True)
    shop_name = Column(String(100), nullable=False)

s1 = Shop(shop_name = "Star")
s2 = Shop(shop_name = "Moon")
s3 = Shop(shop_name = "Sun")
s4 = Shop(shop_name = "Bandana")
s5 = Shop(shop_name = "Cool")
s6 = Shop(shop_name = "Cola")
s7 = Shop(shop_name = "Muka")
s8 = Shop(shop_name = "Skazka")
s9 = Shop(shop_name = "Monik")
s10 = Shop(shop_name = "Kolos")