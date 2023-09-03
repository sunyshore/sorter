# put your list of items in another .txt file
file1 = open('sorter/rankings/make_list/list.txt', 'r')
st = file1.readlines()

newst = ''
skip = 0
count = 0

for line in st:
    newst += line[skip:] + '<br>'
    count += 1

print(newst)
print(count)
#print(st)