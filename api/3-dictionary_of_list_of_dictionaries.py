import requests,sys,json

def export_todo():
    url = f'https://jsonplaceholder.typicode.com/users'
    x = requests.get(url)
    json_data = x.json()
    # print(json_data)
    tasks= []
    for d in json_data:
        EMPLOYEE_NAME = d['name']
        id = int(d["id"])
        # print(id)
        todo_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
        y = requests.get(todo_url)
        data = y.json()
        # Filter tasks owned by the employee
        filtered_tasks = [task for task in data if task['userId'] == id]

        # Prepare the data in the desired format
        formatted_data = {str(id): [{'task': task['title'], 'completed': task['completed'], 'username': EMPLOYEE_NAME} for task in filtered_tasks]}
        # print(formatted_data)
        tasks.append(formatted_data)
    # Save the data as a JSON file
    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as file:
        json.dump(tasks, file)

    # print(f"Data saved to {file_name}")
    __doc__="""doc for class"""
__doc__="""doc for module"""
if __name__ == "__main__":
    export_todo()
