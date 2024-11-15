myDict = {
    "pankha" : "Fan",
    "Dabba" : "Box",
    "vastu" : "item"
}
print("Options are", myDict.keys())
a = input("Enter the Hindi Word\n")
print("The Meaning of your hindi word is",myDict.get(a))