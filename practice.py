__author__ = 'ONicholls'


# import pandas as pd
# import numpy as np
#
# s = pd.Series([1,2,3,np.nan,6,8])
#
# print(s)

# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:', echo=True)
#
#
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
#
#
# from sqlalchemy import Column, Integer, String
#
# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     password = Column(String)
#
#     def __repr__(self):
#         return "<User(name = '%s', fullname = '%s', password = '%s')>" % (
#             self.name, self.fullname,self.password)

import sqlalchemy

print(sqlalchemy.__version__)


