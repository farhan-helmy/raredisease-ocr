import easyocr
import json

reader = easyocr.Reader(['en'])
result = reader.readtext('page1.jpg')

data = []
for detection in result:
    print(detection[1])
    data.append({'text': detection[1]})

with open('output.json', 'w') as outfile:
    json.dump(data, outfile)
