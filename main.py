Question 1

fileName= input("Enter the fileName: ")

#try to read the file
print("Trying to read the file...")
try:with open (fileName, 'r') as file:
    print("Success! file has been found, here's what's inside: ")

except fileNotFoundError: 
    print("Warning! file not found. it will be created now.")

Question 2

#get note from user
print("Getting your note..")
note = input("Type your note: ")

#write it into the file
print("Writing it into the file..")

try:with open (fileName, 'a') as file:
    file.write(note + '\n')
    print("Success! your note has been saved to the file.")

except Exception as e:
    print(f"Error! something went wrong:{e}")