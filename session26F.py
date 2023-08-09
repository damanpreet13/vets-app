def fetch():
    file = open("ipl-data-2023.csv", "r")
    lines = file.readlines()

    for line in lines:
        yield line
# if  a function, yields , it means we get Generator in return
result = fetch()
print("result:", result)
# how to use with loop EXPLORE
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result))
#print(next(result,"no more record"))
#print(next(result,"no more record"))

while True:
    data = next(result,"Nothing")
    print(data)
    if data == "Nothing":
        break