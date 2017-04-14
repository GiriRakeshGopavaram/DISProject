f = open("Data File.txt","r")  # open file, read-only raw data
o = open("mapper_output.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split("    ") 
  
    if len(data) == 4:
        state, month, year, volume = data
        o.write("{0}\t{1}\n".format(state, volume))
f.close()
o.close()