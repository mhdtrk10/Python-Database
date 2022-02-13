
# We read our file and place the data we get from the read file in the appropriate places of our database.
import sqlite3


class _file:            
    def __init__(self): # We are reading file here.
        
        with open("EmployeeInformation.txt","r",encoding="UTF-8") as file:
            file_content=file.read()
            words=file_content.split()
            self.just_words=list()

            for i in words:         # here we are clearing words from structures such as commas and line breaks.
                i=i.strip(" ")
                i=i.strip("\n")

                self.just_words.append(i)


    def add_db(self):       # and here we create the database and transfer the data from the file we read to the database.
        con=sqlite3.connect("EmployeeInfo.db")
        cursor=con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS EmployeeInfo (name TEXT,surname TEXT,salary INT)")
        con.commit()

        for i in range(0,len(self.just_words)):
            if(i%3==0):
                cursor.execute("INSERT INTO EmployeeInfo VALUES(?,?,?)",(self.just_words[i],self.just_words[i+1],self.just_words[i+2]))
                con.commit()
            
            

file_read=_file()

file_read.add_db()

