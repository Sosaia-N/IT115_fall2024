#I import the json.
import json

#Make dictionary from json about me.

data1 = {

    'name':'Sosaia Ngauamo',
    'age': 20,
    'city':'White Center',
    'intersets':['football','videogames','Traveling','comupter','basketball'],
    'is_student': False


}

#with statement will 
with open('data1.json''w') as json_files:

    #Dump the data Dictionary into JSON file.
    json.dump(data1,json_file,indent=4)

#confirmation indext statement
print("Data has been written to data1.json")


##########
#Read the JSON file.

with open ('data1/json','r') as json_files:


    loaded_data = json.load(json_file)
#show out the data1 about myself 
print("Successfuly able to read data1.json")
print(loaded_data)



#########
#Change the contents of the JSON Dicitonary

#
loaded_data['age'] = 20
loaded_data['interests'].append('fun')

#loaded_data['interests'].remove('anything you want to remove')

####
#Resave the altered JSON file.
with open('data1.json','w') as json_file:

    #dump the data dictionary into the JSON file.
    json.dump(data1,json_file,index=4)

print("Data has been re-written to data.json")


