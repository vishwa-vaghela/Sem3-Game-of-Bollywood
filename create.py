import os
file=open("movies.txt","r")
file1=open("movies_.txt","a+")
for i in file:
    for j in i:
        if j==' ':
            file1.write("/")
        elif j not in 'AEIOUaeiou':
            file1.write("_")
        else:
            file1.write(j)
    file1.write("\n")
    
        