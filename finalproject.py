# ###  You have to design a Food Ordering app for a restaurant

# ## The application will have a log-in for admin and users to log-in

# #-------------------------------- **Admin** ----------------------------------

# # Admin will have the following functionalities: 
# """
# 1. Add new food items. Food Item will have the following details:
#             🔴 FoodID //It should be generated automatically by the application.
#             🔴 Name
#             🔴 Quantity. For eg, 100ml, 250gm, 4pieces etc
#             🔴 Price
#             🔴 Discount
#             🔴 Stock. Amount left in stock in the restaurant.
            
# """
# # Function for adding new food items
import random
food_menu =[]
def add_food():
    food_id = random.randint(1000,9999)
    name = input("Enter the name of the food item: ")
    quantity =input("Enter the quantity of the food item:")
    price = float(input("Enter the price of the food item: "))
    discount =float(input("Enter the discount of the food item: "))
    stock = int(input("Enter the stock of the food item: "))
    
    food_item = {'FoodID':food_id,
                 'Name':name,
                 'Quantity':quantity,
                 'Price':price,
                 'Discount':discount,
                 'Stock':stock}
    
    food_menu.append(food_item)
    print("Food menu is : " , food_menu)
    print("Food item added sucessfully")
    
    
# 2. Edit food items using FoodID.

def edit_food():
    food_id = int(input("Enter the food id of the food item to edit: "))
    for item in food_menu:
        if item['FoodID'] == food_id:
            item['Name'] = input("Enter the new name of the food item: ")
            item['Quantity'] = input("Enter the new quantity of the food item: ")
            item['Price'] =float(input("Enter the new price of the food item: "))
            item['Discount'] = float(input("Enter the new discount of the food item: "))
            item['Stock'] = int(input("Enter the new stock of the food item: "))
            print("Food menu is : " , food_menu)
            print("Food item edited successfully")
            return # used to exit the function early
    print("Food item not found")
    
# 3. View the list of all food items.

def view_food_list():
    if not food_menu:
        print("No food items available")
        
    else:
        print("List of food items: ")
        for item in food_menu:
            print(f"FoodID : {item['FoodID']} , Name : {item['Name']},"
                  f"Quantity: {item['Quantity']},Price: {item['Price']},"
                  f"Discount: {item['Discount']}, Stock :{item['Stock']}")
            
# 4. Remove a food item from the menu using FoodID.

def remove_food():
    food_id=int(input("Enter the foodid of the food item to remove: "))
    for item in food_menu:
        if item['FoodID'] == food_id:
            food_menu.remove(item)
            print("Food item removed successfully")
            return
        
    print("Food item not found")
    
# # sample admin menu

# while True:
#     print("\n_______________________Admin Menu_________________________")
    
#     print("1. Add new food items")
#     print("2. Edit food items")
#     print("3. View list of all food items")
#     print("4. Remove a food item")
#     print("5. Exit")
    
    
#     choice = int(input("Enter your choice (1-5): "))
    
#     if choice ==1:
#         add_food()
#     elif choice==2:
#         edit_food()
#     elif choice ==3:
#         view_food_list()
#     elif choice==4:
#         remove_food()
#     elif choice==5:
#         break
#     else:
#         print("Invalid choice . Please enter a valid option")    
    


####################
#--------------------------------- **User** ----------------------------------
"""
# The user will have the following functionalities: ⬅️

    👉 1. Register on the application. Following to be entered for registration:
            🔴 Full Name
            🔴 Phone Number
            🔴 Email
            🔴 Address
            🔴 Password
"""
user_profiles = []
def register_user():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address= input("Enter your address: ")
    password= input("Create password: ")
    
    
    user_profile = {'Full Name':full_name,
                    'Phone Number': phone_number,
                    'Email': email,
                    'Address':address,
                    'Password':password}
    
    user_profiles.append(user_profile)
    print("user profile is : ",user_profiles)
    print("Registration successful")
    

def login_user():
    email =input("Enter your email address: ")
    password = input("Enter your password: ")
    
    
    for user in user_profiles:
        if user['Email'] == email and user['Password'] ==password:
            print("Login Succesful")
            print(user)
            return user
        
    print("Invalid email or password")
    return None 
            

"""   
3. The user will see 3 options:
            🔴 Place New Order
            🔴 Order History
            🔴 Update Profile   
            
""" 

# function place new order 

#users = [{'Full Name': 'Mamatha', 'Phone Number': '123456789', 'Email': 'mamatha123@gmail.com','Address': 'banglore', 'Password': 'mamatha@123'}]
food_menu = [
    {
        "FoodID": random.randint(1000, 9999),
        "Name": "Tandoori Chicken",
        "Quantity": "4 pieces",
        "Price": 240.0,
        "Discount": 0.0,
        "Stock": 50
    },
    {
        "FoodID": random.randint(1000, 9999),
        "Name": "Vegan Burger",
        "Quantity": "1 piece",
        "Price": 320.0,
        "Discount": 0.0,
        "Stock": 30
    },
    {
        "FoodID": random.randint(1000, 9999),
        "Name": "Truffle Cake",
        "Quantity": "500gm",
        "Price": 900.0,
        "Discount": 0.0,
        "Stock": 20
    }
]

order_history =[]
user_profiles = [{'Full Name': 'abc', 'Phone Number': '12345', 'Email': 'abc@gmail.com', 'Address': 'hyd', 'Password': 'abc@123'}]

def place_order(user):
    print("\n__________menu___________")
    for idx,item in enumerate(food_menu,start=1):
        print(f"{idx}. {item['Name']} ({item['Quantity']}) [INR {item['Price']}]")
        
    selected_items=[]    
    try:
        choices =list(map(int,input("Enter the number of the items you want to order (comma separated): ").split(',')))
        selected_items = [food_menu[i-1] for i in choices ]
        
    except (ValueError,IndexError):
        print("Invalid input")
        
        
    print("________________selected items______________")
    
    for item in selected_items:
        print(f"{item['Name']} ({item['Quantity']}) [INR {item['Price']}]")
        
    Place_order_option = input("Do you want to place order? (yes/no)").lower()
    
    if Place_order_option =='yes':
        total_amount = sum(item['Price'] for item in selected_items)
        
      
        print("user_details" , user)        
        order_detail = {'User': user["Full Name"],
                        'Items':selected_items,
                        "Total Amount":total_amount}
        
        order_history.append(order_detail)
        print("order details are: ",order_detail)
        print("order placed successfully")
    else:
        print("order not placed")
        



# # Call the login_user function to get user information
# logged_in_user = login_user()

# # Check if the login was successful before proceeding
# if logged_in_user:
#     # Call the place_order function and pass the logged-in user
#     place_order(logged_in_user)
# else:
#     print("Login failed. Cannot place an order without a logged-in user.")



       

    
order_history = [{'User': 'abc', 'Items': [{'FoodID': 1329, 'Name': 'Tandoori Chicken', 'Quantity': '4 pieces', 'Price': 240.0, 'Discount': 0.0, 'Stock': 50}], 'Total Amount': 240.0} ]  
user_profiles = [{'Full Name': 'abc', 'Phone Number': '12345', 'Email': 'abc@gmail.com', 'Address': 'hyd', 'Password': 'abc@123'}]

## Order History 

def view_order_history():
    if not order_history:
        print("No orders placed yet")
        
    else:
        print("_________________________order history______________")
        for order in order_history:
            print(f"User :{order['User']} ")
            print("Items")
            for item in order['Items']: 
            
                print(f"{item['Name']} ({item['Quantity']}) [INR {item['Price']}]")

                
            print(f"Total amount: INR {order['Total Amount']}")
            
            
# while True:
#     print("\n_______________________Order history________________________")
    
#     print("1. view_order_history")

#     print("2. Exit")
    
    
#     choice = int(input("Enter your choice (1-2): "))
    
#     if choice ==1:
#         view_order_history()
#     elif choice==2:
#         break
#     else:
#         print("Invalid choice")

## Update Profile 
user_profiles = [{'Full Name': 'abc', 'Phone Number': '12345', 'Email': 'abc@gmail.com', 'Address': 'hyd', 'Password': 'abc@123'}]

def update_profile(users_list):
    email = input("Enter email address: ")
    found_user =None
    
    for user in users_list:
        if user['Email'] == email:
            found_user = user
            break    
    if found_user:
        print("\n_____________________user profile updation____________")
        new_phone_number = input("Enter new phone number : ")
        new_email = input("Enter new email : ")
        # add all the fileds which user can update
        found_user['Phone Number'] = new_phone_number
        found_user['Email'] = new_email
        print("user list after updation : ",found_user)
        print("Profile updated ")
        
    else:
        print("User not found")
        
        
while True:
    print("\n_______________________update_profile_______________________")
    
    print("1. update_profile")

    print("2. Exit")
    
    
    choice = int(input("Enter your choice (1-2): "))
    
    if choice ==1:
        update_profile(user_profiles)
    elif choice==2:
        break
    else:
        print("Invalid choice")
        
#############################
food_menu =[{"FoodID": , "Name" : }]
"""
Add Search Functionality:

1. Create a new function, say search_food(), that takes a keyword as input from the user.
2. Search for food items whose names contain the entered keyword.
3. Display the matching food items along with their details.
Details are as below:
#             🔴 FoodID //It should be generated automatically by the application.
#             🔴 Name
#             🔴 Quantity. For eg, 100ml, 250gm, 4pieces etc
#             🔴 Price
#             🔴 Discount
#             🔴 Stock. Amount left in stock in the restaurant.

"""
