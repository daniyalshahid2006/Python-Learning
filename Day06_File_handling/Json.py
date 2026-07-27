import json
from xml.etree.ElementTree import indent

student = {
    "name" : "daniyal",
    "age": 25,
    "skills":
        {
          "python": "basic",
          "web development": "basic",
        "gaming": "master",
        }
}

with open("student.json","w") as file:
    json.dump(student,file,indent=4)
with open("student.json","r") as file:
    data = json.load(file)
    print(json.dumps(data["age","skills"]))