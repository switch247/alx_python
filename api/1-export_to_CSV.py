import requests,sys,csv

def export_todo(id:int):
    url = f'https://jsonplaceholder.typicode.com/users/{id}'
    todo_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    x = requests.get(url)
    json_data = x.json()
    EMPLOYEE_NAME = json_data['name']
    
    y = requests.get(todo_url)
    json_data_2 = y.json()
    # print(json_data_2)
    csv_file= f'{id}.csv'
    with open(csv_file,'w') as csvFile:
        writer = csv.writer(csvFile)
        for i in json_data_2:
            writer.writerow([str(i['userId']),str(EMPLOYEE_NAME),str(i['completed']),str(i['title'])])
    __doc__="""doc for class"""
__doc__="""doc for module"""
if __name__ == "__main__":
    id = int(sys.argv[1])
    export_todo(id)
