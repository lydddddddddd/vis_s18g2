import json
file_directory = "C:/Users/LYDDD/Desktop/s18/vis_s18g2/json/promotion_route.json"
json_data=open(file_directory).read()

data = json.loads(json_data)
print(data)

with open("C:/Users/LYDDD/Desktop/s18/vis_s18g2/json/promotion_rote_output.json","wb") as f:
    json.dump(data,f, indent=2)
