import requests
import json


contents_API = ["films", "people", "planets", "species", "starships", "vehicles"]
all_json_file = ""

for content in contents_API:
    new_res_all = ""
    for i in range(100):
        url = "https://swapi.dev/api/{}/{}".format(content, i)
        response = requests.get(url)
        new_res = ""
        if response.status_code == 200:
            json_response = json.loads(response.text)
            res = str(json_response)
            new_res = '{"id": "' + str(i) + '", ' + res[1::]
            new_res_all = new_res_all + "," + new_res
    str_content = ',"' + content + '":[' + new_res_all[1::] + "]"
    all_json_file = all_json_file + str_content

all_json_file = all_json_file.replace("'", '"')
all_json_file = all_json_file.replace("http://swapi.dev/api/", 'http://localhost:3000/')
all_json_file = all_json_file.replace('"s\\', "'s\\")
all_json_file = all_json_file.replace('"s ', "'s ")
all_json_file = all_json_file.replace(" None", ' "None"')
all_json_file = all_json_file.replace('Twi"lek', "Twi'lek")
all_json_file = all_json_file.replace('Pau"an', "Pau'an")

with open("star_wars_db.json", "w+") as f:
    f.write("{" + all_json_file[1::] + "}")
