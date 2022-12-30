import pymysql
from pymysql.constants import CLIENT

db_connection = pymysql.connect(
  user = "root",
  port = 3306,
  password = "dusick305",
  host = "localhost",
  db = "aitrading_db",
  charset="utf8",
  client_flag=CLIENT.MULTI_STATEMENTS,
)
