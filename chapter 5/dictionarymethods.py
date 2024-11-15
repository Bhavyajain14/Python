myDict = {
    "Fast" : "In a Quick Manner",
    "Bhavya" : "A Coder",
    "Marks" : [1,2,5],
    "AnotherDict" :{'Bhavya':'Player'},
    1: 2
}
# print(list(myDict.keys()))  #prints the keys of dictionary
# print(list(myDict.values()))  #prints the keys of dictionary
# print(list(myDict.items()))  #prints the (key,values) for all content of dictionary
print(myDict)
updateDict = {  
    "RM":"Rap Monster",
    "v":"victory",
    "JK": "Jungkook",
    "Bhavya" : "A dancer",
    
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("Bhavya"))
print(myDict["Bhavya"])
