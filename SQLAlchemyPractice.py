__author__ = 'ONicholls'

from sqlalchemy import *

engine = create_engine('sqlite:///:memory:', echo=True)
metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name',String),
              Column('fullname', String),
              )

addresses = Table('addresses', metadata,
                  Column('id',Integer, primary_key=True),
                  Column('user_id', None,ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
                  )

metadata.create_all(engine)
#ins = users.insert()
#print(str(ins))

ins = users.insert().values(name = 'jack', fullname = 'Jack Jones')
print(str(ins))
print(ins.compile().params)

conn = engine.connect()
result = conn.execute(ins)
ins.bind = engine
print(result.inserted_primary_key)

ins = users.insert()
conn.execute(ins, id=2,name = 'wendy',fullname = 'Wendy Williams')

conn.execute(addresses.insert(),[
 {'user_id' : 1, 'email_address' : 'jack@yahoo.com'},
 {'user_id' : 1, 'email_address' : 'jack@msn.com'},
 {'user_id' : 2, 'email_address' : 'www@www.com'},
 {'user_id' : 2, 'email_address' : 'wendy@aol.com'},
 ])


s = select([(users.c.fullname + ", " + addresses.c.email_address).label('title ')]).\
    where(
        and_(
            users.c.id == addresses.c.user_id,
            users.c.name.between('m', 'z'),
            or_(
                addresses.c.email_address.like('%@aol.com'),
                addresses.c.email_address.like('%@msn.com')
            )
        )

)


conn.execute(s).fetchall()
