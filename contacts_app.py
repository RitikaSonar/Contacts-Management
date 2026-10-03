import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          
        password="your_password",
        database="contacts"
    )

def show_contacts():
    conn = get_connection()
    curs=conn.cursor()
    curs.execute("SELECT * FROM contact")
    rows=curs.fetchall()
    
    print("Sr.No\t MOBILE NO.\t\t NAME")

    for a,(number,name) in enumerate(rows,start=1):
        print(f"  {a}.\t",number,"\t  ----->",name)
    conn.close()

def add_contact(number,name):
    conn = get_connection()
    curs=conn.cursor()
    curs.execute("SELECT * FROM contact WHERE number=%s",(number,))
    if curs.fetchone():
        print("\t\t\tNumber Already Exists...\n\n")
        conn.close()
        return

    curs.execute("SELECT * FROM contact WHERE name=%s",(name,))
    if curs.fetchone():
        print("\t\t\tName already exists... try another name\n\n")
        conn.close()
        return
    
    curs.execute("INSERT INTO contact (number,name) VALUES (%s,%s)",
        (number,name)
    )
    conn.commit()
    print("\t\t\tMOBILE NO. ADDED SUCCESSFULLY...!!\n\n")
    conn.close()

def remove_contact_num(number):
    conn = get_connection()
    curs=conn.cursor()
    curs.execute("SELECT * FROM contact WHERE number=%s",(number,))
    if curs.fetchone():
        curs.execute("DELETE FROM contact WHERE number=%s", (number,))
        curs.commit()
        print("\t\t\tMOBILE NO. REMOVED SUCCESSFULLY...\n")
    else:
        print("Sorry!!.. Number not found\n\n") 
    curs.close()
    conn.close()


def remove_contact_name(name):
    conn = get_connection()
    curs=conn.cursor()
    curs.execute("SELECT * FROM contact WHERE name=%s",(name,))
    if curs.fetchone():
        curs.execute("DELETE FROM contact WHERE name=%s", (name,))
        conn.commit()
        print(f"\t\t\tCONTACT NAMED {name} REMOVED SUCCESSFULLY...\n")
    else:
        print("Sorry!!.. Name not found\n")
    curs.close()
    conn.close()  


def update_contact_name(number,name):
    conn=get_connection()
    curs=conn.cursor()
    curs.execute("SELECT * FROM contact WHERE number=%s",(number,))
    if curs.fetchone():  
        curs.execute("UPDATE contact SET name=%s WHERE number=%s",(name,number))
        conn.commit()
        print("\t\t\tMOBILE NUMBER UPDATED SUCCESSFULLY..!!\n\n")
    else:
        print("OOPS...!!!No such contact to update\n\n")
    curs.close()
    conn.close()

def update_contact_number(name,number):
    conn=get_connection()
    curs=conn.cursor()
    curs.execute("SELECT * FROM contact WHERE name=%s",(name,))
    if curs.fetchone():
        curs.execute("UPDATE contact SET number=%s WHERE name=%s",(number,name))
        conn.commit()
        print("\t\t\tMOBILE NUMBER UPDATED SUCCESSFULLY..!!\n\n")
    else:
        print("OOPS...!!!No such contact to update\n\n")    
    curs.close()
    conn.close()

while True:
    ch=int(input("Press :\n1.Show Contacts\n2.Add Contact\n3.Delete Contact\n4.Update Contact\n5.Exit\t\t :"))
    print()
    match ch:
        case 1:
            show_contacts()
            print()
            print()
        case 2:
            number=input("\nEnter Mobile number to be added:")
            name=input("Enter a name to save this contact:")
            if len(number)==10:
                add_contact(number,name)
            elif len(number)!=10:
                c=input("Invalid Contact Number do you still want to continue ??:\n")
                if c=="Y" or c== "Yes" or c== "yes"  or c== "y" :
                    add_contact(number,name)
                else:
                    print("Contact Discarded...")
                    continue   
                                           
        case 3:
            chh=int(input("1.Delete By Name:\n2.Delete by number:"))
            match chh:
                case 1:
                    name=input("Enter Mobile number holder name to be removed:")
                    remove_contact_name(name)
                case 2:
                    number=input("Enter Mobile number to be removed:")
                    remove_contact_num(number)
        case 4:
            chh=int(input("1.Update Name:\n2.Update number:"))
            match chh:
                case 1:
                    mobno=input("Enter Mobile number whose name to be updated:")
                    name=input("Enter a name to save this contact with:")
                    print()
                    update_contact_name(mobno,name)
                case 2:
                    name=input("Enter name whose number to be updated:")
                    mobno=input("Enter a number to save this name with:")
                    print()
                    update_contact_number(name,mobno)

        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid Choice..Choose again")
            print()
            continue
            





