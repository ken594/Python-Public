### Section 8: String slicing

## slicing = create a substring by extracting elements from another string
#            indexing[] or slice()
#            [start:stop:step]

name = "Bro Code"

# start inclusive, stop exclusive
first_name = name[:3] 
# print Bro
last_name = name[4:]
# print Code
print(first_name)
print(last_name)

funky_name = name[::2]
# funky_name = name[0:8:2]
print(funky_name)

## Reverse string
reversed_name = name[::-1]
print(reversed_name)


website = "http://google.com"

## slice object
sliceObj = slice(7,-4)
print(website[sliceObj])