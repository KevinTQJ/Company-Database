import sqlite3

conn = sqlite3.connect('data.db')

print('connect db successfully')

c = conn.cursor()

#employee
c.execute('''INSERT INTO employee(ID, NAME, PASSWORD, AGE, PHONE_NUMBER, ADDRESS, SALARY, HIRE_DATE, POSITION_TITLE, REPORT_TO)
    VALUES(01, 'Johnny Silverhand', 2021, 34, '2897764638', '2021 Devon Road', 100000.00,'03/18/2015', 'Owner', 'Owner')
;''')

c.execute('''INSERT INTO employee
    VALUES(02, 'Judy Alvarez', 1876, 28, '2893647788', '1876 Watson Road', 16000.00, '09/26/2017', 'Manager', 'Owner')
;''')


c.execute('''INSERT INTO employee
    VALUES(03, 'Logan Bamford', 1156, 41, '3788942237', '1156 Southbay Road', 60000.00, '08/27/2019', 'Cashier', 'Manager')
;''')

c.execute('''INSERT INTO employee
    VALUES(04, 'Goro Takemura', 9098, 59, '4847753874', '9098 Jig Jig Street', 30000.00, '08/30/2018', 'Cashier', 'Manager')
;''')

c.execute('''INSERT INTO employee
    VALUES(05, 'Micah Smith', 1478, 23, '3982331230', '1478 Edinton Road', 45000.00, '04/23/2020', 'Cashier', 'Manager')
;''')

#item
c.execute('''INSERT INTO inventory(ID, NAME, PRICE, AMOUNT, CATEGORY, AUTHOR, PUBLISHER, SERIAL)
    VALUES(01, 'Beholder', 20.00, 60, 'Fiction', 'Warm Lamp', 'Alawar Premium', 'EJ37483')
;''')

c.execute('''INSERT INTO inventory
    VALUES(02,'Beholder 2', 25.00, 80, 'Fiction', 'Warm Lamp', 'Alawar Premium', 'EJ37484')
;''')

c.execute('''INSERT INTO inventory
    VALUES(03,'Dyson Sphere Program', 15.00, 120, 'Science Fiction', 'Youthcat', 'gamera', 'AK83269')
;''')

c.execute('''INSERT INTO inventory
    VALUES(04,'Celeste', 14.25, 20, 'Science Fiction', 'Matt', 'MattMakesG', 'EJ95854')
;''')

c.execute('''INSERT INTO inventory
    VALUES(05,'Battlefield', 13.26, 80, 'History', 'DICE', 'Electronic Arts', 'RT87688')
;''')

c.execute('''INSERT INTO inventory
    VALUES(06,'Devil May Cry', 60.00, 35, 'Fiction', 'Capcom', 'CapcomCo.', 'IO39482')
;''')

c.execute('''INSERT INTO inventory
    VALUES(07,'Return Human', 13.44, 5, 'Humanities', 'Derek Zhou', 'TeenWorld', 'UG94753')
;''')

c.execute('''INSERT INTO inventory
    VALUES(08,'Hades', 24.45, 200, 'Fiction', 'Supergiant', 'SupergiantGM', 'RH39284')
;''')

c.execute('''INSERT INTO inventory
    VALUES(09,'Paranormal HK', 15.20, 140, 'Horror', 'Ghostpie', 'Ghostpie studio','IY48375')
;''')

c.execute('''INSERT INTO inventory
    VALUES(10,'Why I am gay.', 20.00, 100, 'Non-Fiction', 'Ethan Tang', 'LGBTQ', 'GA28492')
;''')

#sales History
c.execute('''INSERT INTO sales(ID, PRODUCT, AMOUNT, DATE, TIME, CASHIER, SERIAL)
    VALUES(01,'Celeste', 1, '02/02/2021', '08:34:06', 'Logan Bamford', 'EJ95854')
;''')

c.execute('''INSERT INTO sales
    VALUES(02, 'Celeste', 1, '02/03/2021', '09:46:36', 'Mica Smith', 'EJ95854')
;''')

c.execute('''INSERT INTO sales
    VALUES(03,'Celeste', 1, '02/14/2021', '18:54:18', 'Logan Bamford', 'EJ95854')
;''')

c.execute('''INSERT INTO sales
    VALUES(04, 'Paranormal HK', 1, '02/15/2021', '22:10:42', 'Logan Bamford', 'IY48375')
;''')

c.execute('''INSERT INTO sales
    VALUES(05,'Why I am gay.', 1, '02/16/2021', '10:32:30', 'Johnny Silverhand', 'GA28492')
;''')

c.execute('''INSERT INTO sales
    VALUES(06, 'Battlefield', 1, '02/16/2021', '19:35:06', 'Logan Bamford', 'RT87688')
;''')

c.execute('''INSERT INTO sales
    VALUES(07, 'Return Human', 1, '02/17/2021', '15:34:39', 'Johnny Silverhand', 'UG94753')
;''')

c.execute('''INSERT INTO sales
    VALUES(08, 'Beholder 2', 1, '02/18/2021', '15:57:03', 'Goro Takemura', 'EJ37484')
;''')

c.execute('''INSERT INTO sales
    VALUES(09, 'Devil May Cry', 1, '02/19/2021', '17:22:38', 'Judy Alvarez', 'IO39482')
;''')

c.execute('''INSERT INTO sales
    VALUES(10, 'Dyson Sphere Program', 1, '02/20/2021', '08:52:30', 'Logan Bamford', 'AK83269')
;''')

c.execute('''INSERT INTO sales
    VALUES(11, 'Beholder', 1, '02/20/2021', '10:37:16', 'Mica Smith', 'EJ37483')
;''')

c.execute('''INSERT INTO sales
    VALUES(12, 'Return Human', 1, '02/20/2021', '11:32:34', 'Goro Takemura', 'UG94753')
;''')

c.execute('''INSERT INTO sales
    VALUES(13,'Beholder 2', 1, '02/20/2021', '15:46:10', 'Logan Bamford', 'EJ37484')
;''')

c.execute('''INSERT INTO sales
    VALUES(14,'Beholder 2', 1, '02/20/2021', '18:32:30', 'Goro Takemura', 'EJ37484')
;''')

c.execute('''INSERT INTO sales
    VALUES(15,'Return Human', 1, '02/22/2021', '13:25:36', 'Logan Bamford', 'UG94753')
;''')

c.execute('''INSERT INTO sales
    VALUES(16,'Devil May Cry', 1, '02/22/2021', '19:55:49', 'Mica Smith', 'IO39482')
;''')

c.execute('''INSERT INTO sales
    VALUES(17,'Battlefield', 1, '02/23/2021', '08:01:36', 'Mica Smith', 'RT87688')
;''')

c.execute('''INSERT INTO sales
    VALUES(18,'Return Human', 1, '02/23/2021', '10:16:09', 'Goro Takemura', 'UG94753')
;''')

c.execute('''INSERT INTO sales
    VALUES(19,'Hades', 1, '02/23/2021', '17:29:00', 'Logan Bamford', 'RH39284')
;''')

c.execute('''INSERT INTO sales
    VALUES(20,'Why I am gay.', 1, '02/25/2021', '10:05:59', 'Goro Takemura', 'GA28492')
;''')

c.execute('''INSERT INTO sales
    VALUES(21,'Devil May Cry', 1, '02/25/2021', '11:55:16', 'Mica Smith', 'IO39482')
;''')

c.execute('''INSERT INTO sales
    VALUES(22,'Battlefield', 1, '02/25/2021', '15:19:33', 'Mica Smith', 'RT87688')
;''')

c.execute('''INSERT INTO sales
    VALUES(23,'Hades', 1, '02/26/2021', '08:00:36', 'Judy Alvarez', 'RH39284')
;''')

c.execute('''INSERT INTO sales
    VALUES(24,'Return Human', 1, '03/07/2021', '10:32:30', 'Mica Smith', 'UG94753')
;''')

c.execute('''INSERT INTO sales
    VALUES(25,'Beholder 2', 1, '03/09/2021', '13:54:07', 'Mica Smith', 'EJ37484')
;''')

c.execute('''INSERT INTO sales
    VALUES(26, 'Dyson Sphere Program', 1, '03/10/2021', '17:04:54', 'Judy Alvarez', 'AK83269')
;''')

c.execute('''INSERT INTO sales
    VALUES(27,'Battlefield', 1, '03/11/2021', '13:04:43', 'Logan Bamford', 'RT87688')
;''')

c.execute('''INSERT INTO sales
    VALUES(28,'Beholder 2', 1, '03/12/2021', '10:44:00', 'Johnny Silverhand', 'EJ37484')
;''')

c.execute('''INSERT INTO sales
    VALUES(29, 'Battlefield', 1, '03/14/2021', '13:49:50', 'Johnny Silverhand', 'RT87688')
;''')

c.execute('''INSERT INTO sales
    VALUES(30,'Devil May Cry', 1, '03/17/2021', '09:43:07', 'Mica Smith', 'IO39482')
;''')
conn.commit()

print('INSERT VALUES successfully')

conn.close()



