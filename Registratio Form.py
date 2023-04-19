from tkinter import *
import sqlite3
root= Tk()
root.title("Registration Form")
root.geometry("600x500")


#DATABASE
conn=sqlite3.connect('address_book.db')

#create cursor
c=conn.cursor()

# Create table

'''c.execute("""CREATE TABLE addresses(
nameentry text,
emailentry text,
phoneentry integer,
genderentry text,
dobentry text,
paymentmoodentry text
)""")
'''


def submit():

    #DATABASE
    conn=sqlite3.connect('address_book.db')
    #create cursor
    c=conn.cursor()

    #Insert into table
    c.execute("INSERT INTO addresses VALUES(:name, :email, :phone, :gender, :dob, :paymentmood)",
              {
                  'name':nameentry.get(),
                  'email':emailentry.get(),
                  'phone':phoneentry.get(),
                  'gender':genderentry.get(),
                  'dob':dobentry.get(),
                  'paymentmood':paymentmoodentry.get()
              }
              )

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()

    
    #print("Accepted")
    nameentry.delete(0,END)
    emailentry.delete(0,END)
    phoneentry.delete(0,END)
    genderentry.delete(0,END)
    dobentry.delete(0,END)
    paymentmoodentry.delete(0,END)

#Create query function
def query():
    #DATABASE
    conn=sqlite3.connect('address_book.db')
    #create cursor
    c=conn.cursor()

    c.execute("SELECT *,oid FROM addresses")
    records=c.fetchall()
    #print(records)

    
    #Loop thru results
    print_records=''
    for record in records:
        print_records += str(record) +"\n"
    query_label = Label(root,text=print_records).grid(row=10,column=3)

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()


# Heading
Label(root, text="Python Rgistration Form", font="ar 15 bold").grid(row=0, column=3)

#Fild Name
name= Label(root, text="Name")
email=Label(root, text="EMail")
phone=Label(root, text="Phone")
gender=Label(root, text="Gender")
dob=Label(root, text="D.O.B")
paymentmood=Label(root, text="Payment Mood")


# Packing Fields
name.grid(row=1,column=2)
email.grid(row=2,column=2)
phone.grid(row=3,column=2)
gender.grid(row=4,column=2)
dob.grid(row=5,column=2)
paymentmood.grid(row=6,column=2)


# Variable for storing Data
namevalue =StringVar
emailvalue= StringVar
phonevalue =StringVar
gendervalue =StringVar
dobvalue =StringVar
paymentmoodvalue =StringVar

checkvalue =IntVar

# Creating Entry Field
nameentry =Entry(root, textvariable=namevalue)
emailentry =Entry(root, textvariable=emailvalue)
phoneentry =Entry(root, textvariable=phonevalue)
genderentry =Entry(root, textvariable=gendervalue)
dobentry =Entry(root, textvariable=dobvalue)
paymentmoodentry =Entry(root, textvariable=paymentmoodvalue)


#packing entry fields
nameentry.grid(row=1,column=3)
emailentry.grid(row=2,column=3)
phoneentry.grid(row=3,column=3)
genderentry.grid(row=4,column=3)
dobentry.grid(row=5,column=3)
paymentmoodentry.grid(row=6,column=3)


#Creating Checkbox
checkbtn =Checkbutton(text="remember me?", variable=checkvalue)
checkbtn.grid(row=7,column=3)


#Submit button
submitbtn=Button(root,text="submit",command=submit).grid(row=8,column=3)

#Create a query button
querybtn=Button(root,text="show records",command=query).grid(row=9,column=3)

#Commit changes
conn.commit()

#Close connection
conn.close()


root.mainloop()
