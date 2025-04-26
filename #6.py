num_list = []

while True:
    user_input = (input("Enter a number and type 'stop' when you're done: "))
    
    if user_input.lower() == 'stop':  
        break  
    try:
        number = float(user_input)
        num_list.append(number)
    except ValueError:
        print("ENTER A NUMBER OR 'stop'.")

if num_list:
    average = sum(num_list) / len(num_list)
    print("The average is:", average)
else:
    print("YOU HAD NO NUMBERS")