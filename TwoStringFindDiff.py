def find_difference(stringSent, stringRec):
    # Convert strings to lists to use the list operations
    listSent = list(stringSent)
    listRec = list(stringRec)
    # Remove characters in stringRec from stringSent
    for char in listRec:
        if char in listSent:
            listSent.remove(char)
    # Return the remaining characters in listSent
    return ''.join(listSent)
# Get user input
stringSent = input("Enter the first string (stringSent): ")
stringRec = input("Enter the second string (stringRec): ")
# Find the difference and print the result
output = find_difference(stringSent, stringRec)
print("Output:", output)


#notes: 
#1. convert the string to list
#2. compare the two string lists's 
#3. if char not present remove it 
#4. use join() to print the difference char that is after remove() the repeted characters are deleted now we just have to join the extra char

#join() - syntax: separator.join(iterable) - ''.join(listSent) combines the elements of listSent into a single string. Since the separator is an empty string '', there are no extra characters or spaces added between the elements.
