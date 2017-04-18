sorted = open("mapper_output.txt","r")   
results = open("reducer_output.txt", "w")  # To store the output of average
results2 = open("reducerTotal_output.txt", "w") # To store the output of Total

totalVolume = 0  # Initially totalVolume and Count are zero
count = 0       
oldState = None    


lines = sorted.readlines()
for line in lines:
    datalist = line.strip().split("\t")
    if len(datalist) != 2:  # if bad input line
       continue             # ignore it

    thisState, thisVolume = datalist  # read into variables

   

    if oldState and oldState != thisState:        
        results.write("{0}\t{1}\n".format(oldState, (totalVolume/count)))
        results2.write("{0}\t{1}\n".format(oldState, (totalVolume)))
        oldState = thisState;
        totalVolume = 0
        count = 0

    oldState = thisState            
    totalVolume += float(thisVolume)
    count += 1




if oldState != None: 
    results.write("{0}\t{1}\n".format(oldState, (totalVolume/count)))
    results2.write("{0}\t{1}\n".format(oldState, (totalVolume)))
	

sorted.close() 
results.close() 



