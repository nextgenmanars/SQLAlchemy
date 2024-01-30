from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, session
import shop, product

metadata = MetaData()

shop_category = Table("shop_category", Base.metadata,
                      Column("shop_id", Integer(), ForeignKey("shops.id")),
                      Column("category_id", Integer(), ForeignKey("categories.id"))
                      )


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer(), primary_key=True)
    categories = Column(String(100), nullable=False)
    shop = relationship("Shop", secondary=shop_category, backref="Category")
    products = relationship("Product")


c_1 = Category(categories="clothes")
c_2 = Category(categories="digital")
c_3 = Category(categories="technique")
c_4 = Category(categories="repair")
c_5 = Category(categories="health")

session.add_all([c_1, c_2, c_3, c_4, c_5])
session.commit()