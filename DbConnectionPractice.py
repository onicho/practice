
from sqlalchemy import *
from sqlalchemy.engine import reflection

URL = 'mssql+pyodbc://GMT04999:1433/OLYA_TEST?driver=SQL+Server'

engine = create_engine(URL, echo = True)

insp = reflection.Inspector.from_engine(engine)
#print(insp.get_table_names())

conn = engine.connect()

# s = text(
#     "SELECT *"
#     "FROM PART"
# )

# for row in conn.execute(s).fetchall():
#     print(row)


s = text("SELECT SNAME FROM supplier WHERE (supplier.city =:c1) ")


# for row in conn.execute(s,c1 = 'london').fetchall():
#     print(row)


print((conn.execute(s,c1 = 'london').fetchall())[1])
