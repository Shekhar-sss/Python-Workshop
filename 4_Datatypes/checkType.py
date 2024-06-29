def determine_type(value):
    # Try to convert the input value to an integer
    try:
        int_value = int(value)
        return f"'{value}' is an Integer."
    except ValueError:
        # If conversion to an integer fails, proceed to the next check
        pass
    
    # Try to convert the input value to a float
    try:
        float_value = float(value)
        return f"'{value}' is a Float."
    except ValueError:
        # If conversion to a float fails, proceed to the next check
        pass
    
    # Check if the input value is a boolean ('true' or 'false')
    if value.lower() == 'true' or value.lower() == 'false':
        return f"'{value}' is a Boolean."
    
    # Check if the input value is 'None'
    if value.lower() == 'none':
        return f"'{value}' is NoneType."
    
    # If none of the above checks succeed, assume the input value is a string
    return f"'{value}' is a String."

def main():
    while True:
        # Prompt the user to enter a value
        user_input = input("Enter a value (or type 'exit' to quit): ")
        
        # Check if the user wants to exit the program
        if user_input.lower() == 'exit':
            break
        
        # Determine the type of the entered value
        value_type = determine_type(user_input)
        
        # Print the determined type
        print(value_type)

# Entry point of the program
if __name__ == "__main__":
    main()
