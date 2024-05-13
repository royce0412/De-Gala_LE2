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
def display_available_games():
    for index, game in enumerate(game_library, start = 1):
        game_title = game_library[game]
        game_quantity = game_library[game]["quantity"]
        game_cost = game_library[game]["cost"]
        print(f"{index}: {game_title}: Quantity: {game_quantity}, Cost: {game_cost}")        

# Function to register a new user
def register_user():
    print("Leave it blank in order to return")
    print("Registering user.....")
    
    create_username = input("Username: ")
    if create_username != "":    
        create_password = input("Password: ")
        if create_password != "":
            account_details = {"Password": create_password, "Balance": 0, "Inventory": []}
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
    pass

# Function to return a game
def return_game(username):
    pass

# Function to top-up user account
def top_up_account(username, amount):
    pass

# Function to display user's inventory
def display_inventory(username):
    pass

# Function for admin to update game details
def admin_update_game(username):
    pass

# Function for admin login
def admin_login():
    pass

# Admin menu
def admin_menu():
    pass

# Function for users to redeem points for a free game rental
def redeem_free_rental(username):
    pass

# Function to display game inventory
def display_game_inventory():
    pass

# Function to handle user's logged-in menu
def logged_in_menu(username):
    print("Logging in...")
    
    username = input("Username: ")
    if username != "":
        login_password = input("Password: ")
        if login_password != "":
        
        else:
            input("Returning to main menu...")
            Cls()
            main()
    else:
        input("Returning to main menu...")
        Cls()
        main()
    

# Function to check user credentials
def check_credentials(username, password):
    pass
    
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
        input("Error: ", e)

    
if __name__ == "__main__":
    main()

print(user_accounts)