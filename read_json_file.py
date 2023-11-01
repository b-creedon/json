## Adding comment to working branch version... 

import json

f = open("/Users/bcreedon/DR_INTERNAL/MS_Visual_Studio/json/TestFiles/T000801326_INV_RCPT.json", "r")
file_line_counter = 0

for json_line in f:
  file_line_counter += 1

  # parse json_line:
  parsed_json = json.loads(json_line)

  # Print the type of parsed_json variable
  print("(", file_line_counter, ") JSON Line is Type:", type(parsed_json) )

  # the result is a Python dictionary:
  # print(parsed_json) 
  # print(parsed_json['eventMessage']) 

  ##### If Type: <class 'list'> THEN loop through each element in the JSON List/Array
  list_element_counter = 0

  for i in parsed_json:
    list_element_counter += 1
    print("\t(", list_element_counter, "): eventMessage[", i['eventMessage'], "], sourceTransactionId[", i['sourceTransactionId'], "]")
  #####

f.close() 

