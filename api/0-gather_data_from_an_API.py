import requests,sys

def get_todo(id:int):
    url = f'https://jsonplaceholder.typicode.com/users/{id}'
    url_2 = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    x = requests.get(url)
    json_data = x.json()
    EMPLOYEE_NAME = json_data['name']
    # print(json_data)
    y = requests.get(url_2)
    json_data_2 = y.json()
    TOTAL_NUMBER_OF_TASKS = len(json_data_2)
    NUMBER_OF_DONE_TASKS=0
    for i in json_data_2:
        if i['completed']==True:
            NUMBER_OF_DONE_TASKS+=1
    print(f'Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for i in json_data_2:
        if i['completed']==True:
            print(f"\t {i['title']}")
    __doc__="""doc for class"""
__doc__="""doc for module"""
if __name__ == "__main__":
    id = int(sys.argv[1])
    get_todo(id)
