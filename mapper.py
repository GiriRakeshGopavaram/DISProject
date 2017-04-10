
mapper_input = open("Natural_Gas_Residential_Consumption_Data.txt","r")  # open file, read-only raw data

mapper_output = open("mapper_output.txt", "w") # open file, write - just our key, value pairs

for line in mapper_input:  

    data = line.strip().split("    ") 

    
    if len(data) == 4:

        state, month, year, consumption_amount = data

        print "{0}\t{1}".format(state, consumption_amount)

        mapper_output.write("{0}\t{1}\n".format(state, consumption_amount))

mapper_input.close()
mapper_output.close()
