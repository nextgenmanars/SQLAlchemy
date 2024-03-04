from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, session
import category


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer(), primary_key=True)
    product_name = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))


p1 = Product(product_name="cap_nike")
p2 = Product(product_name="jeans_levis")
p3 = Product(product_name="subscription_google")
p4 = Product(product_name="subscription_netflix")
p5 = Product(product_name="laptop_apple")
p6 = Product(product_name="phone_samsung")
p7 = Product(product_name="tile_red")
p8 = Product(product_name="wallpaper_blue")
p9 = Product(product_name="painkiller")
p10 = Product(product_name="patch")

# session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
# session.commit()
