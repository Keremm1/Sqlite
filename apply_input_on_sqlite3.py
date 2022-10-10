import sqlite3,msvcrt,time

table_atributes = {}

def table_list(attributes):

    att_list = []

    for i in attributes:

        if i in att_list:

            continue

        else:

            att_list.append(i)

    print(att_list)

    return att_list


def executee(att_list,table_name):

    pattern2 = "create table if not exists "

    pattern2 = pattern2 + table_name +" ("

    for i in att_list:

        try:

            int(i)

            pattern3= pattern2 + i + " İNT,"

            pattern2 = pattern3

            print(pattern2)

        except:

            pattern4= pattern2 + i + " TEXT,"

            pattern2 = pattern4

            print(pattern2)

    print(pattern2.rstrip(",") + ")")

    return pattern2.rstrip(",") + ")"


def apply_1(which):

    pattern = ""

    for i in which:

        pattern += i +" "

    return pattern


class library():

    con_state = False

    connection = None

    cursor = None

    tables = []

    table_attributes = {}


    def __init__(self,library_name):

        self.library_name = library_name


    def connect(self):

        if self.con_state == False:

            self.con_state = True

            self.connection = sqlite3.connect(self.library_name + ".db")

            self.cursor = self.connection.cursor()

        else:

            return False


    def disconnect(self):

        if self.con_state == True:

            self.con_state = False

            self.connection.close()

        else:

            return False


    def add_table(self,*attributes,table_name):

        if str(type(attributes[0])) =="<class 'tuple'>":

            attributes = attributes[0]

        if table_name in self.tables:

            return False

        else:

            self.tables.append(table_name)

            self.table_attributes[table_name] = attributes

            att_list = table_list(attributes)   

            pattern3 = executee(att_list,table_name)

            self.cursor.execute(pattern3)

            self.connection.commit() #attributes grilmezse zaten hata verecektir  


    def add_book(self,table_name,*attributes1):

        if table_name in self.tables:

            a = self.table_attributes[table_name]

            if len(attributes1) == len(a):

                pattern = "İnsert into "+ table_name + "Values (" + len(a)*"?" + (len(a)-1)*"," + ")"

                self.cursor.execute(pattern,attributes1)

                self.connection.commit()

            else:

                return True

        else:

            return False


    def remove_book(self,table_name,which,which1):

        if table_name in self.tables:

            a = self.table_attributes[table_name]

            if which in a:

                pattern1 = "Delete from " + table_name + " where " + which + " = ?"

                self.cursor.execute(pattern1,(which1,))

                self.connection.commit()

            else:

                return True

        else:

            return False


    def show_book(self,attributes,table_name,quest  = False,ket = None): #sırasıyla 1-alınacak tablo özellikleri(demet veri tipinde alınmalı) 2-veri alınacak tablo adı 3-özel ad ile verialımını aktifleştiren parametre

        if table_name in self.tables:

            if str(type(attributes)) == "<class 'tuple'>":

                a = self.table_attributes[table_name]

                for i in attributes:

                    if not i in a:

                        return True

                if "*" in attributes:

                    pattern1 = "Select * from " + table_name 

                    self.cursor.execute(pattern1)

                    data = self.cursor.fetchall()

                    return data

                elif len(attributes) >= 1 and quest == False and ket == None:

                    pattern2 = "Select " + apply_1(attributes) + "From " + table_name 

                    self.cursor.execute(pattern2)

                    data_1 = self.cursor.fetchall()

                    return data_1

                else:

                    return False

            elif str(type(attributes)) == "<class 'str'>" and quest == True and ket != None:

                pattern3 = "select " + "* From " + table_name + " where " + attributes + " = ?"

                self.cursor.execute(pattern3,(ket,))

                data_2 = self.cursor.fetchall()

                return data_2

            else:

                return False

        else:

            return False


    def update(self,table_name,attribute,changen,changed):

        if table_name in self.tables:

            a = self.table_attributes[table_name]

            if attribute in a:

                pattern_6 = "Update " + table_name + " set " + attribute + " = ? where" + attribute + " = ?"

                self.cursor.execute(pattern_6,(changen,changed))

                self.connection.commit()

            else:

                return True

        else:

            return False


    def __str__(self):

        return self.library_name


    def __del__(self):

        ser = 5

        print("Deleting",end="",flush=True)

        for i in range(0,51):

                time.sleep(0.125)

                if i <=ser-1:

                    print(".",end="",flush=True)

                elif i == ser:

                    print("\b"*5," "*5,"\b"*7,end="",flush=True)

                elif i > ser:

                    print(".",end="",flush=True)

                    ser += 5

        print("Deleting Sucessfulyy.")



libraries = []

def create_library(name_of_library,quest = False):

    if quest == False:

        k = "library_" + str(len(libraries))

        exec("k = library(" + name_of_library + ")")

        print("Creating succesfuly -->" + input_1,flush=True)

        return k

    if quest == True:

        index = libraries.index(name_of_library) + 1

        exec("z =library_" + index)

        return z



process2 = False

while True:

    if len(libraries) == 0:

        input_1 = input("Please enter new library's name:")

        libraries.append(input_1)

        libex1 = create_library(input_1)

        continue


    else:

        while True:

            keys = input("Yeni kütüphane oluşturmak için 1'e basın, mevcut kütüphane üzerinde işlem yapmak için 2'ye basın!")

            data = msvcrt.getch()

            if data == b'1':

                input_2 = input("Please enter new library's name:")

                libraries.append(input_2)

                libex2 = create_library(input_2)

            elif data == b'2':

                while True:

                    data3 = input("İlk önce kütüphane ismini doğru bir şekilde giriniz!") 

                    if data3 in libraries:

                        libex3 = create_library(data3,quest=True)
                        
                        while True:
                        
                            print("""kütüphane üzerinde hangi işlemleri yapmak istediğiniz tuş atamaları ile belirtniz:
                            1: Tablo Ekleme
                            2: Tablodan kitap silme          
                            3: Tabloya kitap ekleme
                            4: Kütüphaneyi silme
                            """)
                        
                            data5 = msvcrt.getch()
                        
                            if data5 == b'1':
                        
                                while True:
                        
                                    input3 = input("Eklemek istediğiniz tablo ismini giriniz:")
                        
                                    input6 = input("Eklemek istediğiniz attributesları giriniz:\n1:")
                        
                                    libex3.add_table(input6,input3)
                        
                            elif data5==b'2':
                        
                                input4= input("Hangi  tablodan hangi kitabı silmek istediğinizi yazınız:")
                        
                                if input4 in libex3.table_attributes.keys():
                        
                                    pass
                        
                                else:
                        
                                    print("Please enter valid number command.")
                        
                                    continue
                        
                            elif data5 == b'3':
                        
                                input5 = input("Tabloya kitap ekleme:")
                        
                                if input5 in libex3.table_attributes.keys():
                        
                                        pass
                        
                                else:
                        
                                    print("Please enter valid number command.")
                        
                                    continue
                        
                            else:
                        
                                print("Please enter a valid number command!")
                        
                                continue
                    
                    else:

                        while True:

                            print("""Kütüphaneniz veri tabanından bulunmamaktadır. 
                            Kütüphane ismini tekrar girmek için 9'a basınız.
                            Eğer kütüphane ismini unuttuysanız tüm kütüphaneleri görmek için 6'ya tıklayınız!""")

                            data4 = msvcrt.getch()

                            if data4 == b'6':

                                process2 = True

                                break

                            elif data4 == b'9':

                                process2 = True

                                break

                            else:

                                print("Doğru tuş komutunu giriniz!")

                                continue

                        if process2 == True:

                            process2 = False

                            continue
                            

            else:
                print("Lütfen doğru tuş komut karakteri girin!")
                continue
