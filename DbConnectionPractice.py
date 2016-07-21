import pyodbc
from sqlalchemy import *
from sqlalchemy.engine import reflection

URL = 'mssql+pyodbc://GMT04999:1433/OLYA_TEST?driver=SQL+Server'

engine = create_engine(URL, echo = True)

insp = reflection.Inspector.from_engine(engine)
print(insp.get_table_names())

conn = engine.connect()

s = text(
    "SELECT *"
    "FROM PART"
)

for row in conn.execute(s).fetchall():
    print(row)

