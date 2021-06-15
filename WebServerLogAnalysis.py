"""
Matthew Wilson
EC1841586
Edinburgh College
Assessment Outcomes 3 and 4 Assessment
"""


#Ask for username to print name back. This gives the program a bit more personality.
def login():
    print ("Welcome to the web server logs analysis program\n **************************************")
    user = input("Username: ")
    print("**********************************")
    print ("Hello, ", user, ". Welcome back, Amigo.")
    print("**********************************")


#Reads the file. Files MUST be within the directory of this Python program.
#Asks for filename, opens the file and currently prints the content within.

def readfile():
    print("Which file would you like to read? (Make sure file is in the same directory as this python program")
    #Open the file, store as fh and make readable from other functions
    filename = (input("Filename: "))
    with open(filename, 'r') as fh:
        file_contents = fh.readlines()


    return file_contents


#Extract the IP addresses from text file.
def extractIp(file):

    #Create list
    lst = []

    #Read file line for line and selecting first section before space. Creating first list item into variable.
    for line in file:
        lineSplit = line.split()
        lst.append(lineSplit[0])

    return lst


#Find most frequently occuring IP address
def mostFrequent(ipList):
    dictionary = {}
    #Looping IP addresses within list
    for x in range(len(ipList)):

        #Adding count to IP dictionary entry
        #If IP address is not within the dictionary then add to dictionary, if it does then +1 to its count.
        if ipList[x] in dictionary:

            currentCount = dictionary.get(ipList[x])

            dictionary.update({ipList[x]: currentCount +1})

        else:

            dictionary[ipList[x]] = 1


    #Sorting IP addresses based on count, ranging from highest to lowest.
    ipListSort = dict(sorted(dictionary.items(), key = lambda x: x[1], reverse= True))

    dict_items = ipListSort.items()
    #Take the first entry of the dictionary and print
    firstEntry = list(dict_items)[:1]
    print ("The most frequently occuring entry is: ", firstEntry)


    print ("The remaining IP's are sorted by their frequency from highest to lowest: ", ipListSort)





#Main function that calls other functions, controlling flow.
def main():
    login()
    file = readfile()
    lst = extractIp(file)
    mostFrequent(lst)


#Run main
main()








