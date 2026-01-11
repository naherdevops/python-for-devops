info = {
    "name" : "Poly Chowdhury", #str
    "city" : "Tampa", #str
    "qualification": "BA",
    "salary": 22.5, # float
    "married": True, # Bool
    "favourites" : ["teaching", "movies", 18]
}

print("I live in",info["city"])
print("I love ", info.get("favourite","Not Found"))

info.update({"channel": "Not Found"})

print(dir(info))

for key,value in info.items():
    print(key,value)