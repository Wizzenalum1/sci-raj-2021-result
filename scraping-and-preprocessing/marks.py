import requests
import json
from pathlib import Path




URL = '''https://resultsapi.livehindustan.com/getresultother/'''

def write_json(new_data, filename='data.json'):
    with open(filename,'a+') as file:
        # First we load existing data into a dict.
#        print("file is opened")
        file_data = json.dumps(new_data)
        file_data = file_data+",\n"        
#        print('data creating')
        file.write(file_data)
        # Join new_data with file_data inside emp_details
        print('file data writen',file_data)

try:
	i = 1500199
	for i in range(1751850,1800306):
		URI  = URL+str(i)+"/4"
		print(URI,i)
		r = requests.post(url = URI)
		data = r.json()
#		print(data)
		if(data["status"]==200):
			dic = { 'school':data["result"]['CENT_NAME'],
                    'name':data['result']['CAN_NAME'],
					'roll_no': data["result"]['ROLL_NO'],
					'fname'	: data["result"]['FNAME'],
					'mname'	: data["result"]['MNAME'],
					'percent': data["result"]['PER'],
					'marks': data["result"]['TOT_MARKS'],
                    'district':data["result"]['DIST'],
					}
			print(dic)
		else:print(data)
# #			print("after crateing")
			# fileName = "./raw_data/"+data["result"]["GROUP"]
			# write_json(dic,fileName)


except Exception as e:
	print("ERROR is ", e)
