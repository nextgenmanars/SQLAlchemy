from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, session

metadata = MetaData()

shop_category = Table("shop_category", Base.metadata,
    Column("shop_id", Integer(), ForeignKey("shops.id")),
    Column("category_id", Integer(), ForeignKey("categories.id"))
)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer(), primary_key=True)
    clothes = Column(String(100), nullable=False)
    games = Column(String(100), nullable=False)
    meat = Column(String(100), nullable=False)
    shop = relationship("Shop", secondary=shop_category, backref="Category")