text=input("Enter a string :")

index=text.find(" ")
    
if index != -1:
    print(f"Double space deteted at index position:{index}")
    
else:
    print("No double spaces found in the string.")