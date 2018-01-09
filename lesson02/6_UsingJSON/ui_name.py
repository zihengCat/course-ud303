import requests

def simple_record():
    r = requests.get("http://uinames.com/api?ext&region=United%20States", timeout = 2.0)
    json_data = r.json()
    return json_data

if __name__ == '__main__':
    print(simple_record())

