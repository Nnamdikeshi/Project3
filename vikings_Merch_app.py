from tkinter import *
from tkinter import ttk
from tkinter import messageboximport sqlite3import timeimport datetime
# Establish connection to our dbconn = sqlite3.connect('vikingsdatabase.db', isolation_level=None)c = conn.cursor()class Welcome():#This is the class defining the first welcoming window.    def __init__(self,master):
            #This is the GUI for the starting Menu area. Features five buttons for navigating towards the Buying Merch for week 1, and displaying the item list for each week (Updates) EXIT#          self.master=master          self.master.geometry('250x200+200+170')          self.master.title('VMA.1.1')          self.bar = Scrollbar(self.master)          self.label1=Label(self.master,text='Welcome to the Vikings Merch Store!',fg='purple').grid(row=0,column=1)          self.button1=Button(self.master,text="Buy Week 1 SuperBowl VII",fg='green',bg='purple',command=self.gotomerchandisebuyer).grid(row=1,column=1)          self.button2=Button(self.master,text="Week One Merch List",fg='yellow',bg='purple',command=self.gotoweekOneMerch).grid(row=2,column=1)
          self.button3=Button(self.master,text="Week Two Merch List",fg='yellow',bg='purple',command=self.gotoweekThreeMerch).grid(row=3,column=1)
          self.button4=Button(self.master,text="Week Three Merch List",fg='yellow',bg='purple',command=self.gotoweekThreeMerch).grid(row=4,column=1)          self.button5=Button(self.master,text="Exit",fg='red',bg='black',command=self.exit).grid(row=5,column=1)    def exit(self):        #Exit protocol for the exit button. This part is completely done.#          self.master.destroy()    def gotomerchandisebuyer(self):        #This is the Merchandise Buyer GUI#              root2=Toplevel(self.master)          myGUI=merchandisebuyer(root2)
              def gotoweekOneMerch(self):        #This is where the weekOneMerch is kept          root2=Toplevel(self.master)          mygui=weekOneMerch(root2)
          
    def gotoweekThreeMerch(self):
        #This is where the weekTwoMerch is kept
          root2=Toplevel(self.master)
          mygui=weekThreeMerch(root2)
              def gotoweekThreeMerch(self):
        #This is where weekThreeMerch is kept
          root2=Toplevel(self.master)
          mygui=weekThreeMerch(root2)
          class merchandisebuyer():     #class created for the Merch buyer GUI and processing the numbers (pain in the ass to make)#    def __init__(self,master):          #c.execute('CREATE TABLE IF NOT EXISTS week1_sold_merch(timestamp TEXT)           self.idnum=StringVar()          self.buyname=StringVar()
          self.colorname=StringVar()
          self.merchquantity=StringVar()          self.box_value = StringVar()
          self.box1_value = StringVar()
          self.deletename=StringVar()
                    self.master=master          self.master.geometry('900x450+100+200')          self.master.title('*Buy Merch*')
                    self.label2=Label(self.master,text='Welcome to the Vikings Offseason SuperBowl Sale!!',fg='red').grid(row=0,column=0)          self.label2=Label(self.master,text='Please enter Item #',fg='black').grid(row=3,column=0)          self.label2=Label(self.master,text='Please enter your name',fg='black').grid(row=4,column=0)
          self.label2=Label(self.master,text='Please select color',fg='black').grid(row=5,column=0)
          self.label2=Label(self.master,text='Please select a location',fg='black').grid(row=6,column=0)
          self.label2=Label(self.master,text='Please enter buy quantity',fg='black').grid(row=7,column=0)
          self.label3=Label(self.master,text='****Total Sold for Week 1****',fg='purple').grid(row=8,column=1)
                    self.idLabel = Label(self.master, text="ID", width=10)
          self.idLabel.grid(row=9, column=0)
          self.idFindLabel = Label(self.master, text="Item Name", width=10)
          self.idFindLabel.grid(row=9, column=1) 
          self.colorLabel = Label(self.master, text="Color",width=10)
          self.colorLabel.grid(row=9, column=2)
          self.buyernameLabel = Label(self.master, text="BuyerName", width=10)
          self.buyernameLabel.grid(row=9, column=3)
          self.locationLabel = Label(self.master, text="Location", width=10)
          self.locationLabel.grid(row=9, column=4)
          self.quantityLabel = Label(self.master, text="Quantity", width=10)
          self.quantityLabel.grid(row=9, column=5)
          self.dateLabel = Label(self.master, text="Date", width=10)
          self.dateLabel.grid(row=9, column=6)           
          self.hatLabel = Label(self.master, text="*Hat W/Logo*\nItem#: '1' '2' or '3'")
          self.hatLabel.grid(row=5, column=2) 
          self.shirtLabel = Label(self.master, text="*Shirt with viking Logo*\nItem#: '4' '5' or '6'")
          self.shirtLabel.grid(row=6, column=2) 
          self.shortsLabel = Label(self.master, text="*Shorts with Viking Logo*\nItem#: '7' '8' '9'")
          self.shortsLabel.grid(row=7, column=2) 
                    self.merchname=Entry(self.master,textvariable=self.idnum).grid(row=3,column=1)          self.myname=Entry(self.master,textvariable=self.buyname).grid(row=4,column=1)
          self.garbname=Entry(self.master,textvariable=self.deletename).grid(row=4,column=2)
          # Color Options
          self.color = ttk.Combobox(self.master, textvariable=self.box_value)
          self.color['values'] = ('Yellow', 'Purple', 'Black')
          self.color.current(1)
          self.color.grid(column=1, row=5)
          # Location options
          self.loc = ttk.Combobox(self.master, textvariable=self.box1_value)
          self.loc['values'] = ('Minneapolis', 'St. Paul')
          self.loc.current(0)
          self.loc.grid(column=1, row=6)
          
          
          self.merchQuan=Entry(self.master,textvariable=self.merchquantity).grid(row=7,column=1)  
                    self.button6=Button(self.master,text="Buy",fg='red',command=self.merchbuyer).grid(row=3,column=2)          self.button7=Button(self.master,text="Exit",fg='red',bg='black',command=self.exit).grid(row=3,column=3)
          self.button8=Button(self.master,text="DELETE",fg='red',bg='black',command=self.deleteRecords).grid(row=4,column=3)
          
          
          self.connection = sqlite3.connect('vikingsdatabase.db')
          self.cur = self.connection.cursor()
          self.showallweekOneMerch()
    # Show our table from vikingsdatabase
    def readfromdatabase(self):
         self.cur.execute('SELECT * FROM sold')
         return self.cur.fetchall()
     
    def showallweekOneMerch(self):
          
         data = self.readfromdatabase()
          
         for index, dat in enumerate(data):
             Label(self.master, text=dat[0]).grid(row=index+10, column=0)
             Label(self.master, text=dat[1]).grid(row=index+10, column=1)
             Label(self.master, text=dat[2]).grid(row=index+10, column=2)
             Label(self.master, text=dat[3]).grid(row=index+10, column=3)
             Label(self.master, text=dat[4]).grid(row=index+10, column=4)
             Label(self.master, text=dat[5]).grid(row=index+10, column=5)             Label(self.master, text=dat[6]).grid(row=index+10, column=6)
                 def merchbuyer(self):                     
          # Brings us back to merch buyer frame          self.master.update()
          self.master.deiconify()
          self.dynamic_data_entry()
              def dynamic_data_entry(self):          #this is what adds the data to the database.
          """ Logic could be a little cleaner but it works """          try:
         
             idFind=int(self.idnum.get())
             amount=int(self.merchquantity.get())
             print (amount)
             if idFind == 1: 
                # Unsupported type dilemma conquered ^_^
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 1",(amount,amount))
                conn.commit()
                idFind = "Hat w/Logo" 
                print (idFind)
                
             elif idFind == 2:                
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 2",(amount,amount))
                conn.commit()
                idFind = "Hat w/Logo"                              
                print (idFind)
                
             elif idFind == 3:                
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 3",(amount,amount))               
                conn.commit()
                idFind = "Hat w/Logo"
                print (idFind)
                
             elif idFind == 4:                
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 4",(amount,amount))
                conn.commit()
                idFind = "Shirt w/Logo"
                print (idFind)
                
             elif idFind == 5:                
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 5",(amount,amount))
                conn.commit()
                idFind = "Shirt w/Logo"
                print (idFind)
                
             elif idFind == 6:                
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 6",(amount,amount))
                conn.commit()
                idFind = "Shirt w/Logo"
                print (idFind)
             
             elif idFind == 7:
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 7",(amount,amount))
                idFind = "Shorts w/Logo"
                print (idFind)
             elif idFind == 8:
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 8",(amount,amount))
                idFind = "Shorts w/Logo"
                print (idFind)
             elif idFind == 9:
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 9",(amount,amount))
                idFind = "Shorts w/Logo"
                print (idFind) 
                 
             else:
                #message box display
                messagebox.showerror("Error", "The ID # you entered doesn't exist in our system... \nClick 'OK'  & Try another purchase")
                self.merchname.delete(0, END)
                return 
               

             custname=str(self.buyname.get())
             print (custname)          
             colorname=str(self.color.get())
             print (colorname)
             locationname=str(self.loc.get())
             print (locationname)
             timestamp = str(datetime.datetime.now().date())
              # SQL query INSERT our details             c.execute("INSERT INTO sold (MerchName, Color, BuyerName, Location, Quantity, Date ) VALUES (?, ?, ?, ?, ?, ?)",(idFind, colorname, custname, locationname, amount, timestamp))             conn.commit()
             self.showallweekOneMerch()
             # If it got this far... Success!
             self.label1=Label(self.master,text='Your Purchase was successfull ' + custname,fg='green').grid(row=8,column=0)
                       except ValueError:
             # Error message for ValueError
             messagebox.showerror('Error','Please enter numbers ie: "1", "2", or "3" in their corosponding boxes!')
             #self.merchname.selection_clear()
             #self.merchname.focus()
             self.label1=Label(self.master,text='Your Purchase was unsuccessfull. Sorry ' + custname,fg='red').grid(row=8,column=0)
             return      # Delete function with sql DELETE statement and UPDATE merch stock
    def deleteRecords(self):
          id = self.deletename.get()
          c.execute("DELETE FROM sold WHERE ID=?", id)
          conn.commit()
          c.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='sold'")
          conn.commit()
          self.showallweekOneMerch()
          return
              def exit(self):          #Exit protocol for the exit button. This part is completely done.#          self.master.destroy()
     class weekOneMerch():     #class created to see weekOneMerch that have been previously inputted#    def __init__(self,master):         self.master=master         self.master.geometry('600x210+100+200')         self.master.title('weekOneMerch')         self.connection = sqlite3.connect('vikingsdatabase.db')         self.cur = self.connection.cursor()         self.idLabel = Label(self.master, text="ID", width=10)         self.idLabel.grid(row=0, column=0)         self.nameLabel = Label(self.master, text="Name", width=10)         self.nameLabel.grid(row=0, column=1)         self.colorLabel = Label(self.master, text="Color", width=10)         self.colorLabel.grid(row=0, column=2)         self.soldLabel = Label(self.master, text="Sold", width=10)         self.soldLabel.grid(row=0, column=3)         self.availableLabel = Label(self.master, text="Available", width=10)         self.availableLabel.grid(row=0, column=4)         self.showallweekOneMerch()
             # Show our stock with SELECT    def readfromdatabase1(self):         self.cur.execute("SELECT * FROM for_sale_week1")         return self.cur.fetchall()         def showallweekOneMerch(self):                   data = self.readfromdatabase1()                   for index, dat in enumerate(data):             Label(self.master, text=dat[0]).grid(row=index+1, column=0)             Label(self.master, text=dat[1]).grid(row=index+1, column=1)             Label(self.master, text=dat[2]).grid(row=index+1, column=2)             Label(self.master, text=dat[3]).grid(row=index+1, column=3)             Label(self.master, text=dat[4]).grid(row=index+1, column=4)
             class weekTwoMerch():
     #class created to see weekTwoMerch that have been previously inputted#
    def __init__(self,master):
         self.master=master
         self.master.geometry('600x210+100+200')
         self.master.title('weekTwoMerch')
         self.connection = sqlite3.connect('vikingsdatabase.db')
         self.cur = self.connection.cursor()
         self.idLabel = Label(self.master, text="ID", width=10)
         self.idLabel.grid(row=0, column=0)
         self.nameLabel = Label(self.master, text="Name", width=10)
         self.nameLabel.grid(row=0, column=1)
         self.colorLabel = Label(self.master, text="Color", width=10)
         self.colorLabel.grid(row=0, column=2)
         self.soldLabel = Label(self.master, text="Sold", width=10)
         self.soldLabel.grid(row=0, column=3)
         self.availableLabel = Label(self.master, text="Available", width=10)
         self.availableLabel.grid(row=0, column=4)
         self.showallweekThreeMerch()
         
    # Show our sock with SELECT
    def readfromdatabase(self):
         self.cur.execute("SELECT * FROM for_sale_week2")
         return self.cur.fetchall()
     
    def showallweekTwoMerch(self):
          
         data = self.readfromdatabase()
          
         for index, dat in enumerate(data):
             Label(self.master, text=dat[0]).grid(row=index+1, column=0)
             Label(self.master, text=dat[1]).grid(row=index+1, column=1)
             Label(self.master, text=dat[2]).grid(row=index+1, column=2)
             Label(self.master, text=dat[3]).grid(row=index+1, column=3)
             Label(self.master, text=dat[4]).grid(row=index+1, column=4)

class weekThreeMerch():
     #class created to see weekOneMerch that have been previously inputted#
    def __init__(self,master):
         self.master=master
         self.master.geometry('600x210+100+200')
         self.master.title('weekThreeMerch')
         self.connection = sqlite3.connect('vikingsdatabase.db')
         self.cur = self.connection.cursor()
         self.idLabel = Label(self.master, text="ID", width=10)
         self.idLabel.grid(row=0, column=0)
         self.nameLabel = Label(self.master, text="Name", width=10)
         self.nameLabel.grid(row=0, column=1)
         self.colorLabel = Label(self.master, text="Color", width=10)
         self.colorLabel.grid(row=0, column=2)
         self.soldLabel = Label(self.master, text="Sold", width=10)
         self.soldLabel.grid(row=0, column=3)
         self.availableLabel = Label(self.master, text="Available", width=10)
         self.availableLabel.grid(row=0, column=4)
         self.showallweekThreeMerch()
    # Show our sock with SELECT
    def readfromdatabase(self):
         self.cur.execute("SELECT * FROM for_sale_week3")
         return self.cur.fetchall()
     
    def showallweekThreeMerch(self):
          
         data = self.readfromdatabase()
          
         for index, dat in enumerate(data):
             Label(self.master, text=dat[0]).grid(row=index+1, column=0)
             Label(self.master, text=dat[1]).grid(row=index+1, column=1)
             Label(self.master, text=dat[2]).grid(row=index+1, column=2)
             Label(self.master, text=dat[3]).grid(row=index+1, column=3)
             Label(self.master, text=dat[4]).grid(row=index+1, column=4)             def main():     root=Tk()     myGUIWelcome=Welcome(root)     root.mainloop()if __name__ == '__main__':     main()