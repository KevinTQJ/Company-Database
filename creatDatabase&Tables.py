import sqlite3

conn = sqlite3.connect('data.db')

print('connect db successfully')

c = conn.cursor()

c.execute('''CREATE TABLE employee(
    ID INT PRIMARY KEY  NOT NULL,
    NAME            TEXT    NOT NULL,
    PASSWORD        INT     NOT NULL,
    AGE             INT     NOT NULL,
    PHONE_NUMBER    INT    NOT NULL,
    ADDRESS         CHAR(50),
    SALARY          REAL,
    HIRE_DATE       TEXT    NOT NULL,
    POSITION_TITLE  TEXT    NOT NULL,
    REPORT_TO       TEXT    NOT NULL
);''')

print('creat table employee successfully')



c.execute('''CREATE TABLE inventory(
    ID INT PRIMARY KEY  NOT NULL,
    NAME            TEXT    NOT NULL,
    PRICE           REAL,
    AMOUNT          INT,
    CATEGORY        TEXT    NOT NULL,
    AUTHOR          TEXT    NOT NULL,
    PUBLISHER       TEXT    NOT NULL,
    SERIAL          TEXT    NOT NULL
);''')

print('creat table inventory successfully')



c.execute('''CREATE TABLE sales(
    ID INT PRIMARY KEY  NOT NULL,
    PRODUCT         TEXT    NOT NULL,
    AMOUNT          INT     NOT NULL,
    DATE            TEXT    NOT NULL,
    TIME            TEXT    NOT NULL,
    CASHIER         TEXT    NOT NULL,
    SERIAL          TEXT    NOT NULL
);''')

print('creat table sales successfully')