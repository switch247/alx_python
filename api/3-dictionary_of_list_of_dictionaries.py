#!/usr/bin/python3
import json
import requests


def get_all_users_todos():
    '''
    Given Task:
    Create a Python function that utilizes the Trello API to retrieve all the todos associated with a specific user.
    The function should take the user's Trello API key and return a list of all the todos for useres
    '''
    user_url = 'https://jsonplaceholder.typicode.com/users'
    try:
        response = requests.get(user_url)
        users = response.json()
        all_users_todo = {}

        for user in users:
            user_id = user['id']
            todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                user_id)
            response_todos = requests.get(todos_url)
            response_todos.raise_for_status()
            todos = response_todos.json()
            user_todo_list = []

            for todo in todos:
                user_todo_list.append({
                    'username': user['username'],
                    'task': todo['title'],
                    'completed': todo['completed'],
                })

            all_users_todo[user_id] = user_todo_list

        json_file_name = 'todo_all_employees.json'
        with open(json_file_name, mode='w') as json_file:
            json.dump(all_users_todo, json_file)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_all_users_todos()