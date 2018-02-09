'''
Identifiers:
\d   any number
\D   anything but a number
\s   space
\S   anything but a space
\w   any character
\W   anything but a character
.    any character except for a newline
\b   the whitespace around words
\.   a period

modifiers:
{1,3}  we are expecting 1-3
+      match 1 or more
?      match 0 or 1
*      match 0 or more
$      match the end of a string
^      matching the beginning of a string
|      either or
[]     range or variance  [A-Za-z] or [A-Z] or [1-5a-qA-Z]
{x}    expecting x amount

white Space Characters:
\n     new line
\s     Space
\t     tab
\e     escape
\f     from feed
\r     return

Dont forget!:
. + * ? [] $ ^ { } | \
'''
import re
exampleStr = '''
Jessica is 15 years old and Daniel is 27 years old.
Edward is 96 and his grandfather Oscar, is 102.
'''
ages = re.findall(r'\d{1,3}',exampleStr)
names = re.findall(r'[A-Z][a-z]*', exampleStr)
print(ages)
print(names)
ageDict ={}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x += 1
print(ageDict)
