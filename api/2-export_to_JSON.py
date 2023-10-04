import requests,sys,json

def export_todo(id:int):
    url = f'https://jsonplaceholder.typicode.com/users/{id}'
    todo_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    x = requests.get(url)
    json_data = x.json()
    EMPLOYEE_NAME = json_data['name']
    
    y = requests.get(todo_url)
    data = y.json()
    # Filter tasks owned by the employee
    filtered_tasks = [task for task in data if task['userId'] == id]

    # Prepare the data in the desired format
    formatted_data = {str(id): [{'task': task['title'], 'completed': task['completed'], 'username': EMPLOYEE_NAME} for task in filtered_tasks]}

    # Save the data as a JSON file
    file_name = f"{id}.json"
    with open(file_name, 'w') as file:
        json.dump(formatted_data, file)

    # print(f"Data saved to {file_name}")
    __doc__="""doc for class"""
__doc__="""doc for module"""
if __name__ == "__main__":
    id = int(sys.argv[1])
    export_todo(id)
