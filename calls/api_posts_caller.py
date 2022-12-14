import json, requests
from utils import input_generators, resource_checkers

class ApiPostsCaller:
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key
        self._header = {"Authorization": f"Bearer {api_key}"}

    def post_object(self, object_type: str, object_body: dict="random") -> None:
        """
            Creates a post request for any supported object type (users, posts, comments, todos). Object body can either be passed
            as an argument, or randomly generated if object_body is passed as "random"
        """

        try:
            if not resource_checkers.is_compatible_resource(object_type):
                raise TypeError
            
            self.__post_single_object(object_type, object_body)
        except TypeError:
            print("Invalid POST resource type")

    def __post_single_object(self, object_type: str, object_body) -> str:
        if object_body == "random":
            object_body = input_generators.user_generator()

        base_path = f"https://gorest.co.in/public/v2/{object_type}"
        post_object = requests.post(base_path, data=object_body, headers=self._header)

        print(post_object.status_code)
        print(post_object.content)
