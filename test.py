import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Integer, Float, String, Column
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

def main():

    from sqlalchemy import event
    from sqlalchemy.engine import Engine
    @event.listens_for(Engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


    Base = declarative_base()
    engine = create_engine('sqlite:///manager.db', echo = True)


    class Consultant(Base): # Consultant table class

        __tablename__ = 'consultant'

        ConsultantId = Column (Integer, primary_key = True)
        ConsultantName = Column (String)
        Address = Column (String)
        City = Column (String)
        State = Column (String)
        ZipCode = Column (Integer)
        Commission = Column (Float)
        Rate = Column (Float)

        customer = relationship("Customer", back_populates="consultant")

        def __repr__(self):
            return 'Consultant: ConsultantId = {} ConsultantName = {} Address = {} City = {} State = {} ZipCode = {} Commission = {} Rate = {}'.format(self.ConsultantId, self.ConsultantName, self.Address, self.City, self.State, self.ZipCode, self.Commission, self.Rate)


    class Customer(Base): # Customer table class with relationship with the consutant
        __tablename__ = 'customer'

        CustomerId = Column (Integer, primary_key = True)
        CustomerName = Column (String)
        Address = Column (String)
        City = Column (String)
        State = Column (String)
        ZipCode = Column (Integer)
        Balance = Column (Float)
        ConsultantId = Column (Integer, ForeignKey('consultant.ConsultantId'))
        consultant = relationship("Consultant", back_populates='customer')
        order = relationship("Order", back_populates="customer")

        def __repr__(self):
                return 'Customer: CustomerId = {} CustomerName = {} Address = {} City = {} State = {} ZipCode = {} Balance = {}, assigned to consultant = {}'.format(self.CustomerId, self.CustomerName, self.Address, self.City, self.State, self.ZipCode, self.Balance, self.ConsultantId, self.consultant)


    class Product (Base): # Product table
        __tablename__ = 'product'

        ProductKey = Column (Integer, primary_key = True)
        ProdName = Column (String)
        Description = Column (String)
        Price = Column (Float)
        Quantity = Column (Integer)

        order = relationship("Order", back_populates="product")


        def __repr__(self):
            return 'Product: ProductKey = {} ProdName = {} Description = {} Price = {} Quantity = {}'.format(self.ProductKey, self.ProdName, self.Description, self.Price, self.Quantity )



    class Order (Base): # Order table with relationship with the customer and the Product table
        __tablename__ = 'order'

        OrderNum = Column (Integer, primary_key = True)
        ProdName = Column (String)
        Price = Column (Float)
        Quantity = Column (Integer)
        TotalPrice = Column (Float)
        CustomerNum = Column (Integer, ForeignKey('customer.CustomerId'))
        customer = relationship ("Customer", back_populates = 'order')
        ProductKey = Column (Integer, ForeignKey('product.ProductKey'))
        product = relationship ("Product", back_populates = 'order')

        def __repr__(self):
            return 'Order: OrderNum = {} ProdName = {} Price = {} Quantity = {} TotalPrice = {}, assigned to customer = {}'.format(self.OrderNum, self.ProdName, self.Price, self.Quantity, self.TotalPrice, self.CustomerNum, self.customer)


    Base.metadata.create_all(engine)

    # Initializing rows for Customer, Consultant, product, and Order
    conslt1 = Consultant(ConsultantName = 'David Thomas', Address = '123 boggs street', City = 'Brimstone', State = 'CT', ZipCode = 11200, Commission = 5000.00, Rate = 0.1)
    conslt2 = Consultant(ConsultantName = 'Elaine Jones', Address = 'Eagle park', City = 'Brimstone', State = 'CT', ZipCode = 11222, Commission = 7500.00, Rate = 0.09)
    conslt3 = Consultant(ConsultantName = 'Simon Lee', Address = '69 Rocky Hill', City = 'Brimstone', State = 'NY', ZipCode = 11444, Commission = 600.00, Rate = 0.07)

    Cust1 = Customer (CustomerName = 'Flamingo Michael', Address = '723 Pine St.', City = 'Edmonton', State = 'CT', ZipCode = 11222, Balance = 365.00, ConsultantId = 2)
    Cust2 = Customer (CustomerName = 'Flintoff Francis', Address = '12 Monica Counar', City = 'Ulster', State = 'NY', ZipCode = 18850, Balance = 500.00, ConsultantId = 1)
    Cust3 = Customer (CustomerName = 'Taylor Nicole', Address = '730 Loun Eve. ', City = 'Edmonton', State = 'CT', ZipCode = 11233, Balance = 100.00, ConsultantId = 3)
    Cust4 = Customer (CustomerName = 'Salvatore Stefen', Address = '31 Carnine Lee', City = 'Carver', State = 'NJ', ZipCode = 22843, Balance = 450.00, ConsultantId = 2)
    Cust5 = Customer (CustomerName = 'Winchester Dean', Address = '751 Lounsbury', City = 'Franklin', State = 'NY', ZipCode = 22455, Balance = 750.00, ConsultantId = 3)

    Product1 = Product(ProdName = 'Xbox one', Description = 'Game', Price = 299.00, Quantity = 15)
    Product2 = Product(ProdName = 'Xbox one S', Description = 'Game', Price = 350.00, Quantity = 30)
    Product3 = Product(ProdName = 'PS4', Description = 'Game', Price = 235.00, Quantity = 10)
    Product4 = Product(ProdName = 'Ipad Pro', Description = 'Tablet', Price = 599.00, Quantity = 5)
    Product5 = Product(ProdName = 'Ipad mini', Description = 'Tablet', Price = 399.00, Quantity = 30)
    Product6 = Product(ProdName = 'Surface studio', Description = 'Computer', Price = 3500.00, Quantity = 3)
    Product7 = Product(ProdName = 'htc vive ', Description = 'VR', Price = 760.00, Quantity = 8)
    Product8 = Product(ProdName = 'Hololens', Description = 'VR', Price = 3000.00, Quantity = 2)
    Product9 = Product(ProdName = 'MacBook Air', Description = 'Computer', Price = 750.00, Quantity = 5)
    Product10 = Product(ProdName = 'IPhone7', Description = 'Phone', Price = 800.00, Quantity = 10)

    Order1 = Order ( Price = 350.00, ProdName = 'Xbox one S', Quantity = 1,TotalPrice = 350.00,CustomerNum = 4)
    Order2 = Order ( Price =760.00, ProdName = 'htc vive', Quantity = 1,TotalPrice = 760.00, CustomerNum = 5)
    Order3 = Order ( Price = 800.00, ProdName = 'IPhone7', Quantity = 2,TotalPrice = 1600.00, CustomerNum = 2)
    Order4 = Order ( Price = 399.00, ProdName = 'Ipad mini', Quantity = 1,TotalPrice = 399.00, CustomerNum = 1)

    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind = engine)

    save_session = Session() # creating a new session

    # Creating all tables
    save_session.add_all([conslt1, conslt2, conslt3, Cust1, Cust2, Cust3, Cust4, Cust5, Product1, Product2, Product3, Product4, Product5, Product6, Product7, Product8, Product9, Product10, Order1, Order2, Order3, Order4])
    print (save_session.new)
    print (save_session.dirty)

    save_session.commit()
    save_session.close()

    # inititalizing sessions
    search_Consl = Session()
    search_Cust = Session()
    search_Product = Session()
    search_Order = Session()

    # Printing tables
    for table in search_Consl.query(Consultant):
        print (table)


    for table in search_Cust.query(Customer):
        print (table)


    for table in search_Product.query(Product):
        print (table)


    for table in search_Order.query(Order):
        print (table)

    # Closing all sessions
    search_Consl.close()
    search_Cust.close()
    search_Product.close()
    search_Order.close()

    loop = True

    while loop:
        menu()
        choice = input("Enter your choice: ")

        # inititalizing sessions
        search_Consl = Session()
        search_Cust = Session()
        search_Product = Session()
        search_Order = Session()
        add_session = Session()
        delete_session = Session()
        update_session = Session()
        view_session = Session()

#''' Consultant block to add, view, edit, and delete Consultant'''

        if choice == '1':
            for table in search_Consl.query(Consultant):
                print (table)

            loop2 = True
            while loop2:
                ConslMenu()
                choiceOpt = input("Enter your choice: ")
                if choiceOpt == '1':

                    for table in search_Consl.query(Consultant):#Printing table
                        print (table)

                if choiceOpt == '2': #adding new Consultant
                    ConName = Name(); ConAddress = Address(); ConCity = City(); ConState = State(); ConZipCode = ZipCode(); ConComm = Commission(); ConRate = Rate()
                    NewConsl = Consultant(ConsultantName = ConName, Address = ConAddress, City = ConCity, State = ConState, ZipCode = ConZipCode, Commission = ConComm, Rate = ConRate)
                    add_session.add(NewConsl)
                    add_session.commit()
                    print("New Consultant has been added")

                if choiceOpt == '3': #Viewing Consultant info
                    ConsID = Id()
                    print(view_session.query(Consultant).filter_by(ConsultantId = ConsID).one)

                if choiceOpt == '4': # Updating consultant name
                    ConsID = Id(); NewCOnslt = Name()
                    for row in update_session.query(Consultant).filter_by(ConsultantId = ConsID):
                        row.ConsultantName = NewCOnslt
                        update_session.commit()

                if choiceOpt == '5': # updating Consultant Address
                    ConsID = Id(); NewAddress = Address(); NewCity = City(); NewState = State(); NewZipCode = ZipCode()
                    for row in update_session.query(Consultant).filter_by(ConsultantId = ConsID):
                        row.Address = NewAddress
                        row.City = NewCity
                        row.State = NewState
                        row.ZipCode = NewZipCode
                        update_session.commit()

                if choiceOpt == '6': # updating Consultant Commission
                    ConsID = Id(); NewCOmm = Commission()
                    for row in update_session.query(Consultant).filter_by(ConsultantId = ConsID):
                        row.Commission = NewCOmm
                        update_session.commit()

                if choiceOpt == '7': # updating Consultant rate
                    ConsID = Id(); NewRate = Rate()
                    for row in update_session.query(Consultant).filter_by(ConsultantId = ConsID):
                        row.Rate = NewRate
                        update_session.commit()

                if choiceOpt == '8': # Deleting Consultant
                    ConsID = Id()
                    for row in delete_session.query(Consultant).filter_by(ConsultantId = ConsID):
                        delete_session.delete(row)
                        update_session.commit()

                if choiceOpt == '9': # Going back to the main menu
                    break





#''' Customer block to add, view, edit, and delete Customer'''
        if choice == '2':
            for table in search_Cust.query(Customer): #Printing table
                print (table)

            loop2 = True
            while loop2:
                CustMenu()
                choiceOpt = input("Enter your choice: ")
                if choiceOpt == '1':

                    for table in search_Cust.query(Customer): #Printing table
                        print (table)

                if choiceOpt == '2': # Adding new Customer
                    CustName = Name(); CustAddress = Address(); CustCity = City(); CustState = State(); CustZipCode = ZipCode(); CustBalance = Balance(); ConsId = Id()
                    NewCust = Customer(CustomerName = CustName, Address = CustAddress, City = CustCity, State = CustState, ZipCode = CustZipCode, Balance = CustBalance, ConsultantId = ConsId)
                    add_session.add(NewCust)
                    add_session.commit()
                    print("New Customer has been added")

                if choiceOpt == '3': # View Customer Info
                    CustID = Id()
                    print(view_session.query(Customer).filter_by(CustomerId = CustID).one)

                if choiceOpt == '4': # Updating Customer name
                    CustID = Id(); NewCust = Name()
                    for row in update_session.query(Customer).filter_by(CustomerId = CustID):
                        row.CustomerName = NewCust
                        update_session.commit()

                if choiceOpt == '5':# updating customer Address
                    CustID = Id(); NewAddress = Address(); NewCity = City(); NewState = State(); NewZipCode = ZipCode()
                    for row in update_session.query(Customer).filter_by(CustomerId = CustID):
                        row.Address = NewAddress
                        row.City = NewCity
                        row.State = NewState
                        row.ZipCode = NewZipCode
                        update_session.commit()

                if choiceOpt == '6': # Updting Customer Balance
                    CustID = Id()
                    Pay = float (input("Enter the amount to pay: "))
                    for row in update_session.query(Customer).filter_by(CustomerId = CustID):
                        row.Balance = (row.Balance - Pay)
                        update_session.commit()

                if choiceOpt == '7': # Updating Customer Consultant
                    CustID = Id()
                    NewCOnsltId = Id()
                    for row in update_session.query(Customer).filter_by(CustomerId = CustID):
                        row.ConsultantId = NewCOnsltId
                        update_session.commit()

                if choiceOpt == '8':# Deleting Customer
                    CustID = Id()
                    for row in delete_session.query(Customer).filter_by(CustomerId = CustID):
                        delete_session.delete(row)
                        update_session.commit()

                if choiceOpt == '9': # back to the main menu
                    break




#''' Product block to add, view, edit, and delete Product'''
        if choice == '3':
            for table in search_Product.query(Product): #Printing table
                print (table)

            loop2 = True
            while loop2:
                ProductMenu()
                choiceOpt = input("Enter your choice: ")
                if choiceOpt == '1':

                    for table in search_Product.query(Product): #Printing table
                        print (table)

                if choiceOpt == '2': # Adding new Product
                    ProductName = Name(); Desc = Description(); ProPrice = Price(); Qty = Quantity()
                    NewProd = Product(ProdName = ProductName, Description = Desc, Price = ProdPrice, Quantity = Qty)
                    add_session.add(NewProd)
                    add_session.commit()
                    print("New Product has been added")

                if choiceOpt == '3': # View Product Info
                    ProdID= Id()
                    print(view_session.query(Product).filter_by(ProductKey = ProdID).one)

                if choiceOpt == '4': # Updating Product name
                    ProdID = Id(); NewProd = Name()
                    for row in update_session.query(Product).filter_by(ProductKey = ProdID):
                        row.ProdName = NewProd
                        update_session.commit()

                if choiceOpt == '5':# updating Description
                    ProdID = Id(); NewDesc = Description()
                    for row in update_session.query(Product).filter_by(ProductKey = ProdID):
                        row.Description = NewDesc
                        update_session.commit()

                if choiceOpt == '6': # Updating Price
                    ProdID = Id(); newPrice = Price()
                    for row in update_session.query(Product).filter_by(ProductKey = ProdID):
                        row.Price = NewPrice
                        update_session.commit()

                if choiceOpt == '7': # Updating Quantity
                    ProdID = Id(); NewQty = Quantity()
                    for row in update_session.query(Product).filter_by(ProductKey = ProdID):
                        row.Quantity = NewQty
                        update_session.commit()

                if choiceOpt == '8':# Deleting Customer
                    ProdID = Id()
                    for row in delete_session.query(Product).filter_by(ProductKey = ProdID):
                        delete_session.delete(row)
                        update_session.commit()

                if choiceOpt == '9': # back to the main menu
                    break





#''' Order block to add, view, edit, and delete Order'''
        if choice == '4':
            for table in search_Order.query(Order):# Printing table
                print (table)

            loop2 = True
            while loop2:
                OrderMenu()
                choiceOpt = input("Enter your choice: ")
                if choiceOpt == '1':

                    for table in search_Order.query(Order):# Printing table
                        print (table)

                if choiceOpt == '2': #Adding new order
                    CustID = int (input ("Enter the Customer number: "))
                    ProdID = int(input("Enter the product key: "))
                    Qty = int (input("Enter the Quantity to buy: "))

                    for row in search_Product.query(Product).filter_by(ProductKey = ProdID):
                        ProdPrice = row.Price
                        NProdName = row.ProdName
                        try: # Taking the product out of the stock
                            if Qty <= row.Quantity:
                                row.Quantity = row.Quantity - Qty

                            # elif row.Quantity == 0:
                            #     print ("The is not enough in store to be sold.")
                            #     break
                            #
                            else:
                                print ("Enter small Quantity")
                                Qty = int (input("Enter the Quantity to buy: "))
                        except ValueError:
                            print("This is has to be an integer")

                    NewOrder = Order( ProdName = NProdName, Price = ProdPrice, Quantity = Qty, TotalPrice = (ProdPrice * Qty), CustomerNum = CustID)
                    add_session.add(NewOrder)
                    add_session.commit()
                    print("New Order has been added")

                    # Updating the Commission
                    for row in search_Cust.query(Customer).filter_by(CustomerId = CustID):
                        ConsId = row.ConsultantId
                        row.Balance = row.Balance + (ProdPrice * Qty)
                        search_Cust.commit()
                    for row in search_Consl.query(Consultant).filter_by(ConsultantId = ConsId):
                        row.Commission = row.Commission + (ProdPrice * Qty * row.Rate)
                        search_Consl.commit()

                if choiceOpt == '3':# view order info
                    OrderId = Id()
                    print(view_session.query(Order).filter_by(OrderNum = OrderId).one)

                if choiceOpt == '4':# Updating Price
                    OrderId = Id(); NewPrice = Price()
                    for row in update_session.query(Order).filter_by(OrderNum = OrderId):
                        row.Price = NewPrice
                        row.TotalPrice = (row.Quantity * NewPrice)
                        update_session.commit()

                if choiceOpt == '5':# updating Quantity
                    OrderId = Id(); NewQty = Quantity()
                    for row in update_session.query(Order).filter_by(OrderNum = OrderId):
                        row.Quantity = NewQty
                        row.TotalPrice = (row.Price * NewQty)
                        update_session.commit()

                if choiceOpt == '6':# Deleting order
                    OrderId = Id()
                    for row in delete_session.query(Order).filter_by(OrderNum = OrderId):
                        delete_session.delete(row)
                        update_session.commit()

                if choiceOpt == '7': # back to the main menu
                    break

        if choice == '5': #Close the app
            break

        #Closing the sessions
        search_Consl.close()
        search_Cust.close()
        search_Product.close()
        search_Order.close()
        add_session.close
        delete_session.close
        update_session.close
        view_session.close

def menu(): #Main menu option
    print ('''
                1. Consultant table
                2. Customer table
                3. Product table
                4. Order table
                5. quit''')

def ConslMenu():# Consultant menu option
    print ('''
                1. to print table
                2. to add Consultant
                3. to search for a record
                4. to update Consultant Name
                5. to update Address/City/Staste/Zip Code
                6. to update Commission
                7. to update rate
                8. to delete Consultant
                9. Exit''')

def CustMenu():# Customer Menu Option
    print ('''
                1. to print table
                2. to add Customer
                3. to search for a record
                4. to update Customer Name
                5. to update Address/City/State/ZipCode
                6. to update Balance/Pay
                7. to update Consultant
                8. to delete Customer
                9. Exit''')

def ProductMenu():# Product Menu option
    print ('''
                1. to print table
                2. to add Product
                3. to search for a record
                4. to update Product Name
                5. to update Description
                6. to update Price
                7. to update Quantity
                8. to delete Product
                9. Exit''')

def OrderMenu():# Order Menu Option
    print ('''
                1. to print table
                2. to add Order
                3. to search for a record
                4. to update Price/Total Price
                5. to update Quantity/TotalPrice
                6. to delete Order
                7. Exit''')




#'''  block Of user Entries'''
def Name():
    Name = input("Enter the new Name: ")
    return Name

def Address():
    Address = input("Enter the address: ")
    return Address

def City():
    City = input("Enter the City: ")
    return City

def State():
    State = input("Enter The state: ")
    return State

def ZipCode():
    ZipCode = int(input("Enter zip code: "))
    return ZipCode

def Commission():
    Commission = float (input("Enter Commission: "))
    return Commission
def Rate():
    Rate = float (input("Enter rate: "))
    return Rate

def Price():
    Price = float (input("Enter price: "))
    return Price

def Quantity():
    Quantity = int (input("Enter Quantity received/ bought: "))
    return Quantity

def TotalPrice():
    TotalPrice = float (input("Enter Total price: "))
    return TotalPrice

def Description():
    Description = input("Enter the Description: ")
    return Description

def Balance():
    Balance = float (input("Enter Balance: "))
    return Balance
def Id ():
    Id = int(input("Enter the Id: "))
    return Id

main()