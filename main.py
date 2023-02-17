import pyodbc

conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=BanhMiBietBay\SQLEXPRESS;'
    r'DATABASE=Sales_Manager;'
    r'Trusted_Connection=yes;'
)

try:
    DATABASE = pyodbc.connect(conn_str)
    print("Connected successful!")
except:
    print("Connection not found!")