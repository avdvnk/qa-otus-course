from lesson3.openbrewerydb.open_api import OpenAPI
import json

if __name__ == '__main__':
    response = OpenAPI.get_by_name("cooper")
    data = json.loads(response)
    for item in data:
        if "cooper" not in item.get("name", None).lower():
            print(item.get("name", None))
    print(200)
