# Read in the file
with open('a.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('O\t', 'O\t\n')

# Write the file out again
with open('a.txt', 'w') as file:
  file.write(filedata)

with open('a.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('\n', ' ')

# Write the file out again
with open('a.txt', 'w') as file:
  file.write(filedata)

buyuktursil = open("a.txt")
buyuktursil2 = buyuktursil.readlines()
bos_liste = []


for y in buyuktursil2:
    if y.find("O\t") == -1:
        bos_liste.append(y)

with open("a.txt", "w+") as f:
    f.seek(0)
    for s in bos_liste:
        f.write(s)
