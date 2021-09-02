import sqlite3

class Database():

    def __init__(self,):  
        self.conn = sqlite3.connect('dsc.db')
        print("Opened database successfully")
    
    def createMemeberTable(self):
        self.conn.execute('''CREATE TABLE MEMBER
                (ID VARCHAR(30) PRIMARY KEY     NOT NULL,
                HOUSE           TEXT    NOT NULL
                );''')
        print("Table created successfully")
    
    def close(self):
        self.conn.close()
    
    def addMemeber(self,id,house):
        self.conn.execute("INSERT INTO MEMBER(ID,HOUSE) VALUES(?,?);",(id,house,))
        self.conn.commit()  
    
    def getHouseOfMember(self,id):
        cursor = self.conn.execute("SELECT HOUSE from MEMBER WHERE ID=?;",(id,))
        member = cursor.fetchone()
        return member[0]

    def isMemberHadHouse(self,id):
        cursor = self.conn.execute("SELECT HOUSE from MEMBER WHERE ID=?",(id,))
        return len(cursor.fetchall()) != 0
    
    def updateMeberHouse(self,id,house):
        self.conn.execute("UPDATE MEMBER SET HOUSE=? WHERE ID=?;",(house,id,))
        self.conn.commit()

