'''
Created on Sep 20, 2017

@author: jwang02
'''

#This file was created by the CIO of PeriShip after the class activity where we went over it - I was simply curious how he would have gone about it, as a longtime fan of Python. One of the very neat things I like about coding is the possibility to find a solution that is uniquely yours; hopefully it is also the best, most efficient way too!

# Goal: Scrub and convert the data, loading it into a new list called rows
resultdictionarylist = []
with open("w2h_data.csv") as myfile:
    header = True
    for line in myfile:
        if header:
            # line.split() is call is to clean up the line being read in. The line has trailing newline character 
            # or other non-printable characters. Python string has a split() function call that splits the string
            # based on some given characters. If you don't give the targeted characters, then it will just "trim" the
            # front and trailing white spaces.
            # since the split() returns a list. We need to turn it into a string so we can call 
            # the split() again to split the characters based on the comma delimiter
            # to achieve that, we call "".join(line.split()). This uses the string "join()" function which takes a
            # list as the input parameters. Once we have the string, then call the split again to split into each
            # items.
            myKeys = "".join(line.split()).split(',')
            header = False
        else:
            # See line 13 comments.
            values = "".join(line.split()).split(',')
            resultdictionarylist.append({myKeys[n]:values[n] for n in range(0, len(myKeys))})

# Goal: For each row of data calculate and store the w2h_ratio and shape.
for oneDictionary in resultdictionarylist:
    oneDictionary["W2H Ratio"] = float(oneDictionary['Waist'])/float(oneDictionary['Hip'])
    if (oneDictionary["Gender"] == 'M' and oneDictionary["W2H Ratio"] > 0.9) or (oneDictionary["Gender"] == 'F' and oneDictionary["W2H Ratio"] > 0.8):
        oneDictionary['Shape'] = "Apple"
    else:
        oneDictionary['Shape'] = "Pear"

# Goal: pretty print the rows as an HTML table
html_table = "<!DOCTYPE html>"
# Please note:
# html_table += "<tr>" is the same as:
# html_table = html_table + "<tr>"
html_table += "<html>"
html_table += "<body>"
html_table += "<table>"
html_table += "<tr>"
html_table += "<th>ID</th>"
html_table += "<th>Waist</th>"
html_table += "<th>Hip</th>"
html_table += "<th>Gender</th>"
html_table += "<th>W2H Ratio</th>"
html_table += "<th>Shape</th>"
html_table += "</tr>"

for oneDictionary in resultdictionarylist:
    html_table += "<tr>"
    html_table += "<td>" + oneDictionary['ID'] + "</td>"
    html_table += "<td>" + oneDictionary['Waist'] + "</td>"
    html_table += "<td>" + oneDictionary['Hip'] + "</td>"
    html_table += "<td>" + oneDictionary['Gender'] + "</td>"
    html_table += "<td>" + str(oneDictionary['W2H Ratio']) + "</td>"
    html_table += "<td>" + str(oneDictionary['Shape']) + "</td>"
    html_table += "</tr>"
    
html_table += "</table>"
html_table += "</body>"
html_table += "</html>"

with open('StatsResults.html', 'a') as the_file:
    the_file.write(html_table)

