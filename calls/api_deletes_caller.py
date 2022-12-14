import requests

from utils import resource_checkers, link_modifiers

class ApiDeletesCaller:
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key
        self._header = {"Authorization": f"Bearer {api_key}"}

    def delete_object(self, resource: str, specific: str) -> None:
        try:
            if not resource_checkers.is_compatible_resource(resource):
                raise TypeError
            
            self.__parse_delete_operation(resource, specific)
        except TypeError:
            print("Incompatible DELETE resource type")
    
    def __parse_delete_operation(self, resource: str, specific: str) -> None:
        try:
            integer_specific = int(specific)

            self.__delete_object_of_type(resource, specific)
        except ValueError:
            print("DELETE specific must be formed of numbers only")

    def __delete_object_of_type(self, resource: str, specific: int) -> None:
        base_path = f"https://gorest.co.in/public/v2/{resource}/{specific}"
        delete_result = requests.delete(base_path, headers=self._header)

        print(delete_result.status_code)
