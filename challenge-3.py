def printFunction(nestedObject, inputKey):
    keys = inputKey.split('/')
    for key in keys:
        if key not in nestedObject:
            return {key, "Not Exist"}
        nestedObject = nestedObject[key]
    return nestedObject


nestedObject = {'a': {'b': {'c': 'd'}}}
key = "a/b/c"
print(printFunction(nestedObject, key))
