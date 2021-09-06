# Question 1
print('------------Qestion No. 1------------')
import time
start_time = time.time()

for fizzbuzz in range(1,100):

    if fizzbuzz % 15 == 0:
        print("FizzBuzz")
        continue

    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue

    
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue

    print(fizzbuzz)

print('The execution time for this code is: ' + str(time.time()-start_time))

#Question 2
print('------------Qestion No. 2------------')
import math
r = int(input("Radius = "))
V = (4/3)*math.pi*pow(r,3)
print('The volume of the sphere with radius ' + str(r) + ' is = ' , V)

#Question 3
print('------------Qestion No. 3------------')
def getCSV(booksDict, csvFile):
    keys = list(booksDict.keys())
    items = booksDict[keys[0]]
    f = open(csvFile, "w")
    for j in range(len(items)):
        prt = ""
        for key in booksDict:
            prt += booksDict[key][j] +","

        f.write(prt[:-1] +"\n")
        
    f.close()
    print("\nBooks data have been writen to the file", csvFile, "\n")

#Question 4
print('------------Qestion No. 4------------')
def getDictionary(fileName):
    try:
        fhand = open(fileName)
    except:
        print("can't open the file!!: " + fileName)
        exit()
    
    books_info = {
        "Title" : [],
        "Author" : [],
        "ISBN13" : [],
        "Pages" : []
    }
    
    lineNum = 1
    
    for line in fhand:
        if(line[-1] == "\n"):
            line = line[:-1]
        records = list(map(str, line.split(",")))  
        if lineNum == 1:
            lineNum +=1
        else:
            # append data
            books_info["Title"].append(records[0])   
            books_info["Author"].append(records[1])    
            books_info["ISBN13"].append(records[2])   
            books_info["Pages"].append(records[3]) 

    f = open(fileName, "w")
    f.write("")
    f.close()
    return books_info           

if __name__ == "__main__":
    inpCsv = input("\nPlease enter the csv file: ")
    print("\nFollowing is the returned Dictionary: \n\n",getDictionary(inpCsv), "\n")


#Question 5
print('------------Qestion No. 5------------')