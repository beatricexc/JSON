import json

data = {
     "user": { 
       "name": "Jane Janet",
       "age" : 49
       
     }      
}

with open ("data_file.json", "w") as write_file:
  json.dump(data, write_file)
  
json_str = jdson.dumps(data)
print(json_str)
