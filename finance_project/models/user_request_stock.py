"""class for stocks model."""

from finance_project.database.database import Base
from sqlalchemy import Column, Integer, Datatime, String, Numeric
from sqlalchemy.sql import func
class UserRequestStock(Base):
   __tablename__ = 'user_request_stock'

   id Column(Integer, primary_key=True, index=True)
   date = Column(Datetime, defaut=func.now())
   name = Column(String(100))
   symbol = Column(String(20))
   open = Column(Numeric(6, 2))
   hight = Column(Numeric(6, 2))
   low = Column(Numeric(6, 2))
   close = Column(Numeric(6, 2))


   
