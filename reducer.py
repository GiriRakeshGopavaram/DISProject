reducer_input = open("mapper_output.txt","r")   
reducer_output = open("reducer_output.txt", "w")   

location_dict ={}
max_dict={}
min_dict = {}

for line in reducer_input:  
#Total consumption (in Million Cubic Feet) for each store:
 data = line.strip().split("\t") 
 if data[0] in location_dict:
  location_dict[data[0]] = location_dict[data[0]]+float(data[1])
 else:
  location_dict[data[0]] = float(data[1])

#Maximum consumption (in Million Cubic Feet) for each store:
 if data[0] in max_dict:
  if max_dict[data[0]]<float(data[1]):
   max_dict[data[0]] = float(data[1])
 else:
   max_dict[data[0]] = float(data[1])

#Minimum consumption (in Million Cubic Feet) for each store:
 if data[0] in min_dict:
  if min_dict[data[0]]>float(data[1]):
   min_dict[data[0]] = float(data[1])
 else:
  min_dict[data[0]] = float(data[1])

print '\n-------------------------\n'
print 'Total consumption (in Million Cubic Feet) for each state:'
reducer_output.write("Total consumption (in Million Cubic Feet) for each state:\n")
print '\n'
summation = raw_input("Would you like to see the results (Y/N): ");
if summation == 'Y':
 print '\n'
 for k,v in location_dict.items():
	print '{0}\t{1}'.format(v,k)
	reducer_output.write("{0}\t\t{1}\n".format(v, k))
 

print '\n-------------------------\n'
print 'Maximum consumption (in Million Cubic Feet) for each state:'
reducer_output.write("Maximum consumption (in Million Cubic Feet) for each state:\n")
print '\n'
maximum = raw_input("Would you like to see the results (Y/N): ");
if maximum == 'Y':
 print '\n'
 for k,v in max_dict.items():
  print '{0}\t{1}'.format(v,k)
  reducer_output.write("{0}\t\t{1}\n".format(v, k))
 
print '\n-------------------------\n'
print 'Minimum consumption (in Million Cubic Feet) for each state:'
reducer_output.write("Minimum consumption (in Million Cubic Feet) for each state:\n")
print '\n'
minimum = raw_input("Would you like to see the results (Y/N): ");
if minimum == 'Y':
 print '\n'
 for k,v in min_dict.items():
  print '{0}\t{1}'.format(v,k)
  reducer_output.write("{0}\t\t{1}\n".format(v, k))
 
reducer_input.close()
reducer_output.close()