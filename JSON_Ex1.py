import json

data = {
     "user": { 
       "name": "Jane Janet",
       "age" : 49
       
     }      
}

with open ("data_file.json", "w") as write_file:
  json.dump(data, write_file, indent = 4)
  
json_str = json.dumps(data, indent = 4)
print(json_str)
