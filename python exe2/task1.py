# Insert string into the variable and perform following tasks:
var="this is dummy test for testin purose"

# -Print the type of the variable with a message “The type of the variable is:”
print("The type of the variable is:",type(var))

# -Print the string with a message “The string is:”
print("The string is:",var)

# -Display the 3rd character of the string
print("third character of the string is:",var[2])

# -Display character from 4th to 6th from the string
print("third character of the string is:",var[4:7])

# -Change the 3rd character of the string replace it with ‘A’.
print("The string before replaceing third character:",var)
var[3]='A'
print("The string after replaceing third character:",var)
