from calls import api_deletes_caller, api_gets_caller, api_posts_caller
from utils import input_generators

from constants import API_KEY

def __api_get_calls():
    api_gets_caller_object = api_gets_caller.ApiGetsCaller(api_key=API_KEY)

    api_gets_caller_object.get_object("todos")
    api_gets_caller_object.get_object("users", "7028")
    api_gets_caller_object.get_object("users", "7028", "todos")
    api_gets_caller_object.get_object("user", "24", "comments") # This will throw TypeError because user is not a compatible resource
    api_gets_caller_object.get_object("users", "24", "comments") # This will throw TypeError because users cannot have comments


def __api_post_calls(user_body: dict="random"):
    api_posts_caller_object = api_posts_caller.ApiPostsCaller(api_key=API_KEY)

    api_posts_caller_object.post_object("users", user_body)


def __api_delete_calls(user_body: dict="random"):
    api_deletes_caller_object = api_deletes_caller.ApiDeletesCaller(api_key=API_KEY)

    api_deletes_caller_object.delete_object("users", "7187") #TEMP, to fix with point 4 and 5

#TODO: POST/DELETE calls for other object types (nested ones are weird?, can do both /users/x/todos or include user_id in /todos path)
#TODO: Parse non-2XX responses from server (e.g. 422 invalid request/404 not found/401 auth failed)
#TODO: Check properly if deleting nested resources works
if __name__ == "__main__":
    user_for_current_run = input_generators.user_generator()
    __api_get_calls()
    __api_post_calls(user_for_current_run)
    __api_delete_calls(user_for_current_run)
