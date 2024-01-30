from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

metadata = MetaData()

user_shop = Table("user_shop", Base.metadata,
    Column("user_id", Integer(), ForeignKey("users.id")),
    Column("shop_id", Integer(), ForeignKey("shops.id"))
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    date_of_birth = Column(String(20), nullable=False)
    favorites = Column(String(100))
    shop = relationship("Shop", secondary=user_shop, backref="User")


