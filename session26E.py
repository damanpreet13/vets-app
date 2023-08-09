#file = open("ipl-data-2023.csv", "r")
#List of strings
#lines = file.readlines()
#for line in lines:
  #  print(line)


with open("ipl-data-2023.csv", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)