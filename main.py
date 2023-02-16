# Write your code here
import json
import re

ride_data = json.loads(input())

pattern_stop_name = r'([A-Z][a-z]+ ?){1,} (Road|Avenue|Boulevard|Street)$'
pattern_a_time = r'[0-2]\d:[0-5][0-9]$'
errors = {'stop_name': 0, 'stop_type': 0, 'a_time': 0}
record_stop = {128:0, 256:0, 512:0, 1024:0}

def create_err(key):
    if key not in errors:
        errors[key] = 1
    else:
        errors[key] += 1


for ride in ride_data:
    # print(ride)
    for key, value in ride.items():
        if (key in ('bus_id', 'stop_id', 'next_stop') and not isinstance(value, int)):
            create_err(key)
            
        elif key == 'stop_name' and not re.match(pattern_stop_name, value):
            create_err(key)
        
        elif key == 'stop_type' and value not in ('S', 'O', 'F', ''):
            create_err(key)

        elif key == 'a_time' and not re.match(pattern_a_time, value):
            create_err(key)

        if key == 'bus_id' and value in record_stop:
            record_stop[value] += 1
            

# if errors:
#     print(f'Type and required field validation: {sum(errors.values())} errors')
#     for id, num in errors.items():
#         print(f'{id}:{num}')
for id, num in record_stop.items():
    print(f'bus_id: {id}, stops: {num}')