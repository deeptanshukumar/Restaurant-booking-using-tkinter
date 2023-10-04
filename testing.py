from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox
import pymysql

def foodRegister():
    food_id = foodInfo1.get() 
    title = foodInfo2.get() 
    restaurant = foodInfo3.get() 
    status = foodInfo4.get() 
    status = status.lower()

    insertfood = "insert into " + foodtable + " values('" + food_id + "','" + title + "','" + restaurant + "','" + status + "')" 
    try:
        cur.execute(insertfood) 
        con.commit()
        messagebox.showinfo('Success', "dish added successfully") 
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    root.destroy()


def addFood():
    global foodInfo1, foodInfo2, foodInfo3, foodInfo4, Canvas1, con, cur, foodtable, root

    root = Tk() 
    root.title("DEHARTÉ")
    root.minsize(width=400, height=400) 
    root.geometry("600x500")

    con = pymysql.connect(host="localhost", user="root", password='dpsbn', database='deharte')
    cur = con.cursor()
    foodtable = "food items" 
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40") 
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5) 
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5,
relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add food items", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black') 
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8,
relheight=0.4)

    # food ID
    lb1 = Label(labelFrame, text="Food ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    foodInfo1 = Entry(labelFrame) 
    foodInfo1.place(relx=0.3, rely=0.2, relwidth=0.62,
relheight=0.08)

    # title
    lb2 = Label(labelFrame, text="title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4, relheight=0.08)

    foodInfo2 = Entry(labelFrame) 
    foodInfo2.place(relx=0.3, rely=0.4, relwidth=0.62,
relheight=0.08)

    # restaurant
    lb3 = Label(labelFrame, text="restaurant : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.6, relheight=0.08)

    foodInfo3 = Entry(labelFrame) 
    foodInfo3.place(relx=0.3, rely=0.6, relwidth=0.62,
    relheight=0.08)

    # food Status
    lb4 = Label(labelFrame, text="Status(Avail/ordered) : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.8, relheight=0.08)

    foodInfo4 = Entry(labelFrame) 
    foodInfo4.place(relx=0.3, rely=0.8, relwidth=0.62,
    relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=foodRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

ordertable = "foods_ordered" 
foodtable = "Menu"

def deleteFood():
    food_id = foodInfo1.get()

    deleteSql = "delete from " + foodtable + " where food_id = '" + food_id + "'"
    deleteorder = "delete from " + ordertable + " where food_id = '"+ food_id + "'" 
    try:
        cur.execute(deleteSql) 
        con.commit() 
        cur.execute(deleteorder) 
        con.commit()
        messagebox.showinfo('Success', "Food item Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")

def delete():
    global foodInfo1, foodInfo2, foodInfo3, foodInfo4, Canvas1, con, cur, foodtable, root

    root = Tk() 
    root.title("deharte")
    root.minsize(width=400, height=400) 
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#006B38") 
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5) 
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Food", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black') 
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8,relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Food ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    foodInfo1 = Entry(labelFrame) 
    foodInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=deleteFood)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

con = pymysql.connect(host="localhost", user="root", password='dpsbn', database='deharte')
cur = con.cursor()

# List To store all Book IDs allfood_id = []
allfood_id = []


def order():
    global orderBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    food_id = inf1.get() 
    orderto = inf2.get()

    orderBtn.destroy() 
    labelFrame.destroy() 
    lb1.destroy() 
    inf1.destroy() 
    inf2.destroy()

    extractfood_id = "select food_id from " + foodtable 
    try:
        cur.execute(extractfood_id) 
        con.commit()
        for i in cur:
            allfood_id.append(i[0])

        if food_id in allfood_id:
            checkAvail = "select status from " + foodtable + " where food_id = '" + food_id + "'"
            cur.execute(checkAvail) 
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'avail': 
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Food ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Food IDs")

    orderSql = "insert into " + ordertable + " values ('" + food_id + "','" + orderto + "')"
    show = "select * from " + ordertable

    updateStatus = "update " + foodtable + " set status = 'ordered' where food_id = '" + food_id + "'"
    try:
        if food_id in allfood_id and status == True: 
            cur.execute(orderSql) 
            con.commit() 
            cur.execute(updateStatus) 
            con.commit()
            messagebox.showinfo('Success', "Food ordered Successfully")
            root.destroy() 
        else:
            allfood_id.clear()
            messagebox.showinfo('Message', "Food Already ordered") 
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    allfood_id.clear()


def orderFood():
    global orderBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    root = Tk() 
    root.title("deharte")
    root.minsize(width=400, height=400) 
    root.geometry("600x500")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5) 
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="order Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black') 
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8,relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # ordered To Student name
    lb2 = Label(labelFrame, text="ordered To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # order Button
    orderBtn = Button(root, text="order", bg='#d1ccc0', fg='black', command=order)
    orderBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


allfood_id = []

def returnn():
    global SubmitBtn, labelFrame, lb1, foodInfo1, quitBtn, root, Canvas1, status

    food_id = foodInfo1.get()

    extractfood_id = "select food_id from " + ordertable

    try:
        cur.execute(extractfood_id) 
        con.commit()
        for i in cur:
            allfood_id.append(i[0])

        if food_id in allfood_id:
            checkAvail = "select status from " + foodtable + " where food_id = '" + food_id + "'"
            cur.execute(checkAvail) 
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'ordered': 
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    orderSql = "delete from " + ordertable + " where food_id = '" + food_id + "'"
    updateStatus = "update " + foodtable + " set status = 'avail' where food_id = '" + food_id + "'"
    try:
        if food_id in allfood_id and status == True: 
            cur.execute(orderSql) 
            con.commit() 
            cur.execute(updateStatus) 
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            allfood_id.clear()
            messagebox.showinfo('Message', "Please check the bookID")

            root.destroy() 
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

        allfood_id.clear() 
        root.destroy()

def returnFood():
    global foodInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, root, labelFrame, lb1

    root = Tk() 
    root.title("deharte")
    root.minsize(width=400, height=400) 
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#006B38") 
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5) 
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5,    relheight=0.13)

    headingLabel = Label(headingFrame1, text="Cancel order", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black') 
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8,    relheight=0.5)

    # Food ID to Delete
    lb1 = Label(labelFrame, text="Food ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5)

    foodInfo1 = Entry(labelFrame) 
    foodInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="Return", bg='#d1ccc0', fg='black', command=returnn)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

foodtable = "Menu" 
foodtable1= "foods_ordered"


def View():
    root = Tk() 
    root.title("deharte")
    root.minsize(width=400, height=400) 
    root.geometry("600x500")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9") 
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5) 
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5,    relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Menu", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black') 
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8,    relheight=0.5) 
    y = 0.25

    Label(labelFrame, text="%-10s%-40s%-30s%-20s" % ('food_id', 'title', 'restaurant', 'Status'), bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="--------------------------------------------------------------------------", bg='black', fg='white').place(relx=0.05, rely=0.2)
    getFoods = "select * from " + foodtable 
    try:
        cur.execute(getFoods) 
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-30s%-30s%-20s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(relx=0.07, rely=y) 
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop() 


def View_order():
    root = Tk()
    root.title("deharte") 
    root.minsize(width=400, height=400) 
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9") 
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5) 
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5,    relheight=0.13)

    headingLabel = Label(headingFrame1, text="View ordered Food", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black') 
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8,    relheight=0.5) 
    y = 0.25

    Label(labelFrame, text="%-10s%-20s" % ('food_id','ordered_to'), bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text=" 	", bg='black', fg='white').place(relx=0.05, rely=0.2)
    getFoods = "select * from " + foodtable1 
    try:
        cur.execute(getFoods) 
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-20s" % (i[0], i[1]), bg='black', fg='white').place(relx=0.07, rely=y) 
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

root = Tk() 
root.title("deharte")
root.minsize(width=700, height=500) 
root.geometry("800x600")

same = True 
n = 0.6

# Adding a background image 
background_image = Image.open("C:/Users/dines/Downloads/the-best-top-10-indian-dishes.png")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth * n) 
if same:
    newImageSizeHeight = int(imageSizeHeight * n) 
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight))
img = ImageTk.PhotoImage(background_image) 
Canvas1 = Canvas(root)
Canvas1.create_image(450, 300, image=img) 
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight) 
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#FFBB00", bd=5) 
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n The Deharté Food ordering app \n by: Deeptanshu,Harshit,Tejas", bg='black', fg='white',font=('Courier', 15)) 
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Food Details", bg='black', fg='white', command=addFood)
btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Food", bg='black', fg='white', command=delete)
btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Food List", bg='black', fg='white', command=View)
btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="order Food", bg='black', fg='white', command=orderFood)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Cancel order", bg='black', fg='white', command=returnFood)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

btn6 = Button(root, text="View orders", bg='black', fg='white', command=View_order)
btn6.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1) 

root.mainloop()
