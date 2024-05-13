import os
# Dictionary to store game library with their quantities and rental costs
game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1},
    # Add more games as needed
}

# Dictionary to store user accounts with their balances and points
user_accounts = {}


# Admin account details
admin_username = "admin"
admin_password = "adminpass"

# Function to use clear screen
def Cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Function to display available games with their numbers and rental costs
def display_available_games(username):
    for index, game in enumerate(game_library, start = 1):
        game_quantity = game_library[game]["quantity"]
        game_cost = game_library[game]["cost"]
        print(f"{index}: {game}: Quantity: {game_quantity}, Cost: {game_cost}")
    print("")
    input("Enter to continue...")
    Cls()
    user_menu(username)        

# Function to register a new user
def register_user():
    print("Leave it blank in order to return")
    print("Registering user.....")
    
    create_username = input("Username: ")
    if create_username != "":    
        create_password = input("Password: ")
        if create_password != "":
            account_details = {"Password": create_password, "Balance": 0, "Points": 0, "Inventory": []}
            user_accounts[create_username] = account_details
            input("Account registered sucessfully!")
            Cls()
            main()
        else:
            input("Returning to main menu...")
            Cls()
            main()

    else:
        input("Returning to main menu...")
        Cls()
        main()

# Function to rent a game
def rent_game(username):
    print("To rent a game, enter its designated number. Leave it blank to return to the user menu.")
    
    for index, game in enumerate(game_library, start = 1):
        game_quantity = game_library[game]["quantity"]
        game_cost = game_library[game]["cost"]
        print(f"{index}: {game}: Quantity: {game_quantity}, Cost: {game_cost}")
        
    rent_choice = input("Enter: ")
    
    try:
        if rent_choice != "":
            if rent_choice == "1":
                if game_library["Donkey Kong"]["quantity"] > 0 and user_accounts[username]["Balance"] >= game_library["Donkey Kong"]["cost"]:
                    user_accounts[username]["Inventory"].append("Donkey Kong")
                    game_library["Donkey Kong"]["quantity"] -= 1
                    user_accounts[username]["Balance"] -= game_library["Donkey Kong"]["cost"]
                    user_accounts[username]["Points"] += int((game_library["Donkey Kong"]["cost"])/2)
                    input("Game rented successfully!")
                    Cls()
                    user_menu(username)
                else:
                    input("Donkey Kong is already sold out, press enter to return.")
                    Cls()
                    rent_game(username)
                    
            elif rent_choice == "2":
                if game_library["Super Mario Bros"]["quantity"] > 0 and user_accounts[username]["Balance"] >= game_library["Super Mario Bros"]["cost"]:
                    user_accounts[username]["Inventory"].append("Super Mario Bros")
                    game_library["Super Mario Bros"]["quantity"] -= 1
                    user_accounts[username]["Balance"] -= game_library["Super Mario Bros"]["cost"]
                    user_accounts[username]["Points"] += int((game_library["Super Mario Bros"]["cost"])/2)
                    input("Game rented successfully!")
                    Cls()
                    user_menu(username)
                else:
                    input("Super Mario Bros is already sold out, press enter to return.")
                    Cls()
                    rent_game(username)
                    
            elif rent_choice == "3":
                if game_library["Tetris"]["quantity"] > 0 and user_accounts[username]["Balance"] >= game_library["Tetris"]["cost"]:
                    user_accounts[username]["Inventory"].append("Tetris")
                    game_library["Tetris"]["quantity"] -= 1
                    user_accounts[username]["Balance"] -= game_library["Tetris"]["cost"]
                    user_accounts[username]["Points"] += int((game_library["Tetris"]["cost"])/2)
                    input("Game rented successfully!")
                    Cls()
                    user_menu(username)
                else:
                    input("Tetris is already sold out, press enter to return.")
                    Cls()
                    rent_game(username)
                    
            else:
                raise Exception("Invalid choice. Please enter a number from 1-3.")
        else:
            input("Enter to return...")
            Cls()
            user_menu(username)
    except Exception as b:
        print("Error: ", b)
        input("Enter to continue...")
        Cls()
        user_menu(username)
        

# Function to return a game
def return_game(username):
    print("To return a game, enter its designated number. Leave it blank to return to the user menu.")
    print(f"{username}'s Inventory:")
    
    for index, game in enumerate(user_accounts[username]["Inventory"], start = 1):
        print(f"{index}. {game}")
        
    return_choice = int(input("Enter: "))
    if return_choice != "":
        user_accounts[username]["Inventory"].pop(return_choice - 1)
        input("Game returned successfully!")
        Cls()
        user_menu(username)
    else:
        print("Enter to return...")
        Cls()
        user_menu(username)

# Function to top-up user account
def top_up_account(username):
    print("Account Top-Up")
    print("Enter a blank to return to the main menu.")
    top_up_amount = float(input("Enter amount: $"))
    print("")
    if top_up_amount != 0:
        user_accounts[username]["Balance"] += top_up_amount
        input("Amount entered successfully!")
        Cls()
        user_menu(username)
    elif top_up_amount < 0:
        print("Please enter a positive amount.")
        Cls()
        user_menu(username)
    else:
        print("Enter a key to return...")
        Cls()
        user_menu(username)
    
# Function to display user's inventory
def display_inventory(username):
    print(f"{username}'s Inventory:")
    for index, game in enumerate(user_accounts[username]["Inventory"], start = 1):
        print(f"{index}. {game}")
    input("Enter to return...")
    Cls()
    user_menu(username)
    
# Function for admin to update game details
def admin_update_game(username):
    pass

# Function for admin login
def admin_login():
    print("Please enter your username and password to login.")
    print("Enter while leaving it blank to return to the main menu.")
    admin_user = input("Username: ")
    if admin_user != "":
        if admin_user == "admin":
            admin_pass = input("Password: ")
            if admin_pass == "adminpass":
                Cls()
                admin_menu()
            else:
                input("Incorrect password.")
                Cls()
                admin_login()
        else:
            input("Incorrect username.")
            Cls()
            admin_login()
    else:
        input("Returning to menu...")
        Cls()
        main()
# Admin menu
def admin_menu():
    print("Welcome Admin! Please choose from the following choices below.")
    print("1. Update Game")
    print("2. View all games")
    print("1. ")
    
    

# Function for users to redeem points for a free game rental
def redeem_free_rental(username):
    print("Please redeem enough points for a free game rental.")
    print("Press no to return to the user menu.")
    redeem_point_display = user_accounts[username]["Points"]
    print(f"Points: {redeem_point_display}")
    
    try:
        redeem_choice = input("Would you like to redeem your free game rental? (y/n): ")
        if redeem_point_display >= 3:
            if redeem_choice == "y":
                user_accounts[username]["Points"] -= 3
                input("Successfully redeemed!... Enter to continue")
                Cls()
                user_menu(username)
            elif redeem_choice == "n":
                input("Returning to user menu...")
                Cls()
                user_menu(username)
            else:
                raise Exception("Invalid choice. Please only enter y or n.")
        else:
            input("Insufficient Points. Enter to continue")
            Cls()
            user_menu(username)
            
    except Exception as c:
        print("Error: ", c)
        input("Enter to continue...")
        Cls()
        user_menu(username)
    

# Function to display game inventory
def display_game_inventory():
    pass

# Function to handle user's logged-in menu
def logged_in_menu():
    print("Logging in...")
    
    username = input("Username: ")
    if username != "":
        login_password = input("Password: ")
        if login_password != "":
            if username in user_accounts and login_password == user_accounts[username]["Password"]:
                print("Enter to continue...")
                Cls()
                user_menu(username)
            else:
                print("Invalid username or password.")
        else:
            input("Returning to main menu...")
            Cls()
            main()
    else:
        input("Returning to main menu...")
        Cls()
        main()
    

# Function to check user credentials
def check_credentials(username):
    print("Account Credentials")
    credential_pass = user_accounts[username]["Password"]
    credential_balance = user_accounts[username]["Balance"]
    credential_points = user_accounts[username]["Points"]
    print(f" Username: {username}")
    print(f"  -Password: {credential_pass}")
    print(f"  -Balance: {credential_balance}")
    print(f"  -Points: {credential_points}")
    input("Enter to continue...")
    Cls()
    user_menu(username)
    
def user_menu(username):
    print(f"Welcome to the main menu, {username}!")
    print("1. Rent Game")
    print("2. Return Game")
    print("3. Top-up Account")
    print("4. Display Inventory")
    print("5. Display Available Games")
    print("6. Check Credentials")
    print("7. Redeem Free Game")
    print("8. Log Out")
    user_choice = input("Enter: ")
    Cls()
    
    try:
        if user_choice == "1":
                rent_game(username)
        elif user_choice == "2":
            return_game(username)
        elif user_choice == "3":
            top_up_account(username)
        elif user_choice == "4":
            display_inventory(username)
        elif user_choice == "5":
            display_available_games(username)
        elif user_choice == "6":
            check_credentials(username)
        elif user_choice == "7":
            redeem_free_rental(username)
        elif user_choice == "8":
            main()
        else:
            raise Exception("Invalid choice. Please enter a number from 1 to 7.")
        
    except Exception as a:
        print("Error: ", a)
        
# Main function to run the program
def main():
    print("Welcome to the Game Rental Shop!")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Register User")
    print("4. Exit")
    main_choice = input("Choice: ")
    Cls()
    try:
        if main_choice == "1":
            logged_in_menu()
        elif main_choice == "2":
            admin_login()
        elif main_choice == "3":
            register_user()
        elif main_choice == "4":
            exit()
        else:
            raise Exception("Invalid choice. Please enter a number from 1 to 4.")
    
    except Exception as e:
        print("Error: ", e)

    
if __name__ == "__main__":
    main()

