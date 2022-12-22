import random
import json

file = open("TestData.json", "r", encoding='utf8')
DATA = json.load(file)

def get_data():
    r = random.randint(1, len(DATA))
    data = DATA
    return data[f"Task {r}"]["Question"], data[f"Task {r}"]["Answers"], data[f"Task {r}"]["C Answer"], f"assets/images/"+data[f"Task {r}"]["Asset"], data[f"Task {r}"]["fact"]
    


if __name__ == '__main__':
    print(get_data())
