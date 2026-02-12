#Create A Dictionary
sample_dict = {
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"New York"
}
keys = ["name","salary"]
def extractByList(inputDictionary, keysToExtract):
    newDic = {}

    for x in keysToExtract:
        if x in inputDictionary:
            newDic[x]=inputDictionary[x]
    return newDic

print(extractByList(sample_dict, keys))

studentDict = {
    "class": {
        "student": {
            "name":"Mike","marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
#Print history!
print(studentDict["class"]["student"]["marks"]["history"])