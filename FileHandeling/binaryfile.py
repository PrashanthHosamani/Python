# with open('FileHandeling/Screenshot 2025-08-26 at 12.53.14.png', 'r') as f:
#     f.read()
  
with open('FileHandeling/Screenshot 2025-08-26 at 12.53.14.png', 'rb') as f:
    with open("screenshot_copy.png",'wb' ) as wf:
        wf.write(f.read())
        
# with open('FileHandeling/Screenshot 2025-08-26 at 12.53.14.png', 'rb') as f:
#     print(f.read())
    
#dict

d = {
    'name' : "Nitish",
    'age' : 33,
    'gender' : 'male'
}
import json
with open('dict.json', 'w') as f:
    json.dump(d, f)


