# put your list of items in another .txt file
file1 = open('sorter/rankings/list.txt', 'r')
st = file1.readlines()

newst = ''
skip = 0

for line in st:
    newst += line[skip:] + '<br>'

print(newst)
#print(st)