def placeholder_for_update():
            print("Update Game Details")
            print("1. Quantity")
            print("2. Cost")
            print("3. Return")
            print("")
           
            game_update_choice = int(input("Enter: "))
            to_except(game_update_choice, 1, 3)
            if game_update_choice == "1": 
                    print("1")
            elif game_update_choice == "2":
                    print("2")
            elif game_update_choice =="3":
                    print("3")      
            else:
                raise Exception("Invalid choice. Please enter a number from 1-3.")
           
def to_except(input, min, max):
    try:
        if input >= min and input <= max:
            return
        else:
            raise Exception(f"Invalid, please enter a number from {min} to {max}")
    except Exception as e:
          print("Error: ", e)
          input("Enter to continue...")
          placeholder_for_update()