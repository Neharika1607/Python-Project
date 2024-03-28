import os
import csv
def add_record():
    print("Add a new Record: ")
    print("------------------------")
    f=open('# file name.csv','a')
    s=csv.writer(f)
    coustomer_number=int(input('Enter Coustomer number='))
    name=input('Enter coustomer name=')
    ammount=float(input('Enter Ammount paid='))
    rec=[coustomer_number,name,ammount]
    s.writerow(rec)
    f.close()
    print("Record Saved")
    input("Press key to continue....")

def modify_record():
    print("To Modify the Record")
    print("------------------------")
    f=open("# file name.csv",newline='\r\n')
    f1=open('#temp.csv','w',newline='\r\n')
    f1=open('#temp.csv','a',newline='\r\n')
    r=input('Enter rollno you want to modify: ')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("Coustomer=",rec[0])
            print("Name=",rec[1])
            print("Ammount=",rec[2])
            choice=input("Do you want to modify this record(y/n): ")
            if choice=='y' or choice=='Y':
                coustomer_number=int(input('Enter Coustomer number='))
                name=input('Enter new name=')
                ammount=float(input('Enter ammount='))
                rec[0]=coustomer_number
                rec[1]=name
                rec[2]=ammount
                rec=[coustomer_number,name,ammount]
                s1.writerow(rec)
                print("Record Modified")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()  
    f1.close()
    os.remove("#file name.csv")
    os.rename("#temp.csv","students.csv")
    input("Press key to continue....")

def delete_record():
    print("Delete a Record")
    print("------------------------")
    f=open('#file_name.csv','r','\r\n')
    f1=open('#temp.csv','w','\r\n')
    f1=open('#temp.csv','a','\r\n')
    r=input('Enter record you want to delete: ')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("Coustomer_number=",rec[0])
            print("Name=",rec[1])
            print("Ammount=",rec[2])
            choice=input("Do you want to delete this record(y/n): ")
            if choice=='y' or choice=='Y':
                pass
                print("Record Deleted")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("#file_name.csv")
    os.rename("#temp.csv","students.csv")
    input("Press key to continue..")

def view_all():
    print("List of All Records")
    print("------------------------")
    f=open('#file_name.csv','r',newline='\r\n')  #Remove new line character from output
    s=csv.reader(f)
    i=1
    for rec in s:
        print(rec[0],end="\t\t")
        print(rec[1],end="\t\t")
        print(rec[2])
        i+=1
    f.close()
    input("Press any key to continue..")

def search():
    print("Search a Record")
    print("------------------------")
    f=open('#file_name.csv','r',newline='\r\n')  #Remove new line character from output
    r=input('Enter rollno you want to search')
    s=csv.reader(f)
    for rec in s:
        if rec[0]==r:
            print("Rollno=",rec[0])
            print("Name=",rec[1])
            print("Marks=",rec[2])
    f.close()
    input("Press any key to continue..")

def mainmenu():
    choice=0
    while choice!=6:
        print("\n")
        print("Main Menu")
        print("------------------------")
        print("1. Add a new Record")
        print("2. Modify Existing Record")
        print("3. Delete Existing Record")
        print("4. Search a Record")
        print("5. List all Records")
        print("6.Exit")
        choice=int(input('Enter your choice:'))
        if choice==1:
            add_record()
        elif choice==2:
            modify_record()
        elif choice==3:
            delete_record()
        elif choice==4:
            search()
        elif choice==5:
            view_all()
        elif choice==6:
            print("Software Terminated")
            break

mainmenu()
