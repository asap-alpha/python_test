from array import array

# using list to insert a character in string

s1 = "word"

list = list(s1)
list.insert(3,"l")
new_string = "".join(list)
print(new_string)

# using array to achieve the same thing
ar_str = "word"

ar = array('u', ar_str)
ar.insert(3,"l")
new_string = "".join(ar)
print(new_string.upper())

title = "welcome home".title().istitle()
print(title)