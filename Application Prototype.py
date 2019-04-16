import tkinter as tk

# for picking colors: https://www.w3schools.com/colors/colors_picker.asp
# for tutorial video: https://www.youtube.com/watch?v=D8-snVfekto
# for tkinter guide: https://www.tutorialspoint.com/python3/python_gui_programming.htm


class CustomerInfo:
    def __init__(self):
        HEIGHT = 600 
        WIDTH = 700
        root = tk.Tk()
        
        canvas = tk.Canvas(root,height=HEIGHT, width = WIDTH, bg= 'black')
        canvas.pack()
        
        #This is used for the backgroud
        lower_frame = tk.Frame(root, bg="black")
        lower_frame.place(relx=0,rely=0,relwidth = 1, relheight=1)        
        #All of the content goes on top of the frame
        frame = tk.Frame(root, bg="#e6e6e6")
        frame.place(relx=0.01,rely=0.01,relwidth = 0.98, relheight=0.98)
        
        label =tk.Label(frame, text= "Glamping World Phone Ordering",font='Helvetica 18 bold', bg='light grey')
        label.place(relx=0, rely=0,relwidth=1, relheight=.1) 
        #Just a line break so it looks good
        label =tk.Label(frame,font='Helvetica 12', bg='black')
        label.place(relx=0, rely=.1,relwidth=1, relheight=.0075)

        photo = tk.PhotoImage(file="P:\Python\GWlogo.gif") # specify the path to your file
        label = tk.Label(frame, image=photo, bg='light grey',justify='right')  #put the image in a label to disdaply it in the window
        label.place(relx=.8, rely=.0,relwidth=.2, relheight=.1)  # show the label on the screen
        
        
        
        
        #Customer information section break
        label =tk.Label(frame, text= "Customer's Information",justify='left', font='Helvetica 12 bold', bg="#e6e6e6")
        label.place(relx=0, rely=.1075,relwidth=.27, relheight=.05)
        
        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(frame, text = "New Customer", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5,width = 20,bg="#e6e6e6", font='Helvetica 10 bold')
        C2 = tk.Checkbutton(frame, text = "Returning Customer", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20,bg="#e6e6e6", font='Helvetica 10 bold')
        C1.place(relx=.3, rely=.1075,relwidth=.2, relheight=.045)
        C2.place(relx=.5, rely=.1075,relwidth=.22, relheight=.045)

        label =tk.Label(frame, text= "First Name", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.05, rely=.15,relwidth=.2, relheight=.05)
        first_name_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        first_name_entry.place(relx=.25, rely=.15,relwidth=.25, relheight=.05)
        
        label =tk.Label(frame, text= "Surname", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.5, rely=.15,relwidth=.2, relheight=.05)
        last_name_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        last_name_entry.place(relx=.7, rely=.15,relwidth=.25, relheight=.05)
        
        label =tk.Label(frame, text= "Customer ID", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.05, rely=.2,relwidth=.2, relheight=.05)
        customerID_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        customerID_entry.place(relx=.25, rely=.2,relwidth=.25, relheight=.05)
        
        label =tk.Label(frame, text= "Birthday(Optional)", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.5, rely=.2,relwidth=.2, relheight=.05)
        birthday_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        birthday_entry.place(relx=.7, rely=.2,relwidth=.25, relheight=.05)
    
        label =tk.Label(frame, text= "Dial Code", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.05, rely=.25,relwidth=.2, relheight=.05)
        var = tk.StringVar()
        options_menu = tk.OptionMenu(frame,var,"+1","+506","+44","+52","+91","+86")
        options_menu.place(relx=.25, rely=.25,relwidth=.1, relheight=.05)
    
        label =tk.Label(frame, text= "Phone Number", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.36, rely=.25,relwidth=.15, relheight=.05)
        phone_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        phone_entry.place(relx=.52, rely=.25,relwidth=.15, relheight=.05)
    
        label =tk.Label(frame, text= "Email", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.665, rely=.25,relwidth=.07, relheight=.05)
        email_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        email_entry.place(relx=.74, rely=.25,relwidth=.255, relheight=.05)
        

        label =tk.Label(frame, text= "Porduct Details",justify='left', font='Helvetica 12 bold', bg="#e6e6e6")
        label.place(relx=0, rely=.3,relwidth=.18, relheight=.05)
    
        label =tk.Label(frame, text= "Product Name", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.05, rely=.35,relwidth=.2, relheight=.05)
        var2 = tk.StringVar()
        options_menu2 = tk.OptionMenu(frame,var2,"Tent","Sleeping Bag","Sleeping Pad","First Aid Kit","Tarp","Backpack")
        options_menu2.place(relx=.25, rely=.35,relwidth=.15, relheight=.05)

        label =tk.Label(frame, text= "Product Number", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.4, rely=.35,relwidth=.2, relheight=.05)
        var3 = tk.StringVar()
        options_menu3 = tk.OptionMenu(frame,var3,"1001","1002","1003","1007","1010","1013")
        options_menu3.place(relx=.6, rely=.35,relwidth=.1, relheight=.05)

        label =tk.Label(frame, text= "Item Size", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.73, rely=.35,relwidth=.1, relheight=.05)
        var4 = tk.StringVar()
        options_menu4 = tk.OptionMenu(frame,var4,"XS","S","M","L","XL","XXL")
        options_menu4.place(relx=.85, rely=.35,relwidth=.1, relheight=.05)
    
        label =tk.Label(frame, text= "Item Quantity", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.05, rely=.4,relwidth=.2, relheight=.05)
        var5 = tk.StringVar()
        options_menu5 = tk.OptionMenu(frame,var5,"1","2","3","4","5","6","7","8","9")
        options_menu5.place(relx=.25, rely=.4,relwidth=.08, relheight=.05)

        label =tk.Label(frame, text= "Currency", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.35, rely=.4,relwidth=.12, relheight=.05)
        var6 = tk.StringVar()
        options_menu6 = tk.OptionMenu(frame,var6,"United States Dollar","Costa Rican colón")
        options_menu6.place(relx=.48, rely=.4,relwidth=.2, relheight=.05)


        product_cost = 0
        
        if var2 == "Tent":
            product_cost = 100
        elif var2 == "Sleeping Bag":
            product_cost = 40
        elif var2 == "Sleeping Pad":
            product_cost = 15
        elif var2 == "First Aid Kit":
            product_cost = 30
        elif var2 == "Tarp":
            product_cost = 10
        elif var2 == "Backpack":
            product_cost = 90


        label =tk.Label(frame, text= "Product Cost", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.69, rely=.4,relwidth=.16, relheight=.05)
        ####THIS NEEDS TO BE FIXED TO DISPLAY THE ACTUAL PRICE####
        label =tk.Label(frame, textvariable = product_cost, font='Helvetica 12', bg="white")
        label.place(relx=.86, rely=.4,relwidth=.08, relheight=.05)
        ####THIS NEEDS TO BE FIXED TO DISPLAY THE ACTUAL PRICE####
        
        button2 = tk.Button(frame, text="Add item to cart",font='Helvetica 12', bg='light gray', fg='black')
        button2.place(relx=.05, rely=.45,relwidth=.2, relheight=.05)




        label =tk.Label(frame, text= "Shipping Details",justify='left', font='Helvetica 12 bold', bg="#e6e6e6")
        label.place(relx=0, rely=.5,relwidth=.18, relheight=.05)

        CheckVar3 = tk.IntVar()
        CheckVar4 = tk.IntVar()
        C3 = tk.Checkbutton(frame, text = "In-Store Pickup", variable = CheckVar3, onvalue = 1, offvalue = 0, height=5,width = 20,bg="#e6e6e6", font='Helvetica 10 bold')
        C4 = tk.Checkbutton(frame, text = "Ship to Address", variable = CheckVar4, onvalue = 1, offvalue = 0, height=5, width = 20,bg="#e6e6e6", font='Helvetica 10 bold')
        C3.place(relx=.3, rely=.5,relwidth=.2, relheight=.045)
        C4.place(relx=.5, rely=.5,relwidth=.2, relheight=.045)

        label =tk.Label(frame, text= "Address", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.05, rely=.55,relwidth=.15, relheight=.05)
        address_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        address_entry.place(relx=.2, rely=.55,relwidth=.3, relheight=.05)
        
        label =tk.Label(frame, text= "City", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.45, rely=.55,relwidth=.10, relheight=.05)
        city_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        city_entry.place(relx=.535, rely=.55,relwidth=.15, relheight=.05)
        
        label =tk.Label(frame, text= "State/Provinces", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.68, rely=.55,relwidth=.18, relheight=.05)
        var7 = tk.StringVar()
        options_menu7 = tk.OptionMenu(frame,var7,"San Jose","Heredia","Alajuela", "Cartago", "Puntarenas", "Guanacaste","Limon")
        options_menu7.place(relx=.86, rely=.55,relwidth=.135, relheight=.05)

        label =tk.Label(frame, text= "Country", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.05, rely=.6,relwidth=.15, relheight=.05)
        var8 = tk.StringVar()
        options_menu8 = tk.OptionMenu(frame,var8,"Costa Rica","United States")
        options_menu8.place(relx=.2, rely=.6,relwidth=.15, relheight=.05)

        CheckVar5 = tk.IntVar()
        CheckVar6 = tk.IntVar()
        C5 = tk.Checkbutton(frame, text = "5% (standard 5-7 business days)", variable = CheckVar5, onvalue = 1, offvalue = 0, height=5,width = 20,bg="#e6e6e6", font='Helvetica 10 bold')
        C6 = tk.Checkbutton(frame, text = "10% (standard 3-5 business days)", variable = CheckVar6, onvalue = 1, offvalue = 0, height=5, width = 20,bg="#e6e6e6", font='Helvetica 10 bold')
        C5.place(relx=.3, rely=.65,relwidth=.32, relheight=.045)
        C6.place(relx=.65, rely=.65,relwidth=.34, relheight=.045)

        label =tk.Label(frame, text= "Postal Code", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.45, rely=.6,relwidth=.13, relheight=.05)
        postal_code_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        postal_code_entry.place(relx=.6, rely=.6,relwidth=.15, relheight=.05)


        label =tk.Label(frame,justify='left', text= "Payment Details", font='Helvetica 12 bold', bg="#e6e6e6")
        label.place(relx=0, rely=.7,relwidth=.18, relheight=.05)


        label =tk.Label(frame, text= "Name on Card", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.05, rely=.74,relwidth=.18, relheight=.05)
        name_on_card_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        name_on_card_entry.place(relx=.25, rely=.74,relwidth=.3, relheight=.05)


        label =tk.Label(frame, text= "CVV", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.64, rely=.74,relwidth=.1, relheight=.05)
        CVV_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        CVV_entry.place(relx=.75, rely=.74,relwidth=.1, relheight=.05)

        label =tk.Label(frame, text= "Card Number", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.05, rely=.79,relwidth=.18, relheight=.05)
        card_number_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        card_number_entry.place(relx=.25, rely=.79,relwidth=.3, relheight=.05)

        label =tk.Label(frame, text= "Expiration", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.58, rely=.79,relwidth=.15, relheight=.05)
        var10 = tk.StringVar()
        options_menu10 = tk.OptionMenu(frame,var10,"01","02","03","04","05","06","07","08","09","10","11","12")
        options_menu10.place(relx=.72, rely=.79,relwidth=.08, relheight=.05)
        var11 = tk.StringVar()
        options_menu11 = tk.OptionMenu(frame,var11,"19","20","21","22","23","24","25","26")
        options_menu11.place(relx=.8, rely=.79,relwidth=.08, relheight=.05)


        button = tk.Button(frame, text="Submit Order",font='Helvetica 14 bold', bg='light gray', fg='black', command = root.destroy)

        button.place(relx=.79, rely=.94,relwidth=.2, relheight=.05)
    
        label =tk.Label(frame, text= "Billing Address", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.05, rely=.88,relwidth=.175, relheight=.05)
        address_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        address_entry.place(relx=.23, rely=.88,relwidth=.3, relheight=.05)
        
        label =tk.Label(frame, text= "City", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.45, rely=.88,relwidth=.10, relheight=.05)
        city_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        city_entry.place(relx=.535, rely=.88,relwidth=.15, relheight=.05)
        
        label =tk.Label(frame, text= "State/Provinces", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.68, rely=.88,relwidth=.18, relheight=.05)
        var7 = tk.StringVar()
        options_menu7 = tk.OptionMenu(frame,var7,"San Jose","Heredia","Alajuela", "Cartago", "Puntarenas", "Guanacaste","Limon")
        options_menu7.place(relx=.86, rely=.88,relwidth=.135, relheight=.05)

        label =tk.Label(frame, text= "Country", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.05, rely=.93,relwidth=.15, relheight=.05)
        var8 = tk.StringVar()
        options_menu8 = tk.OptionMenu(frame,var8,"Costa Rica","United States")
        options_menu8.place(relx=.2, rely=.93,relwidth=.15, relheight=.05)
        
        label =tk.Label(frame, text= "Postal Code", font='Helvetica 12', bg="#e6e6e6")
        label.place(relx=.45, rely=.93,relwidth=.13, relheight=.05)
        postal_code_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
        postal_code_entry.place(relx=.6, rely=.93,relwidth=.15, relheight=.05)


        CheckVar8 = tk.IntVar()
        C8 = tk.Checkbutton(frame, text = "Same as Shipping Address", variable = CheckVar8, onvalue = 1, offvalue = 0, height=5, width = 20,bg="#e6e6e6", font='Helvetica 10 bold')
        C8.place(relx=.1, rely=.8389,relwidth=.34, relheight=.0375)
        root.mainloop()

        

CustomerInfo()





