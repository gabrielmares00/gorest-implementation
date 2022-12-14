import requests

from utils import resource_checkers, link_modifiers

class ApiGetsCaller:
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def get_object(self, resource: str, specific: str="all", secondary_resource: str="") -> None:
        try:
            if not resource_checkers.is_compatible_resource(resource):
                raise TypeError
            
            self.__parse_get_operation(resource, specific, secondary_resource)
        except TypeError:
            print("Incompatible GET resource type")
    
    def __parse_get_operation(self, resource: str, specific: str, secondary_resource: str) -> None:
        try:
            if specific == "all":
                self.__get_all_objects_of_type(resource)
            elif specific != "all" and secondary_resource == "":
                self.__get_specific_object_of_type(resource, specific)
            elif specific!= "all" and secondary_resource != "" and resource_checkers.is_good_nested_resource(resource, secondary_resource):
                self.__get_nested_resource_of_type(resource, specific, secondary_resource)
            else:
                raise TypeError
        except TypeError:
            print("Incompatible GET resource type combination")

    def __get_all_objects_of_type(self, resource: str) -> None:
        base_path = f"https://gorest.co.in/public/v2/{resource}"
        api_call_path = link_modifiers.append_key_to_path(base_path, self._api_key)
        get_result = requests.get(api_call_path)

        print(get_result.content)
    
    def __get_specific_object_of_type(self, resource: str, specific: str) -> None:
        base_path = f"https://gorest.co.in/public/v2/{resource}/{specific}"
        api_call_path = link_modifiers.append_key_to_path(base_path, self._api_key)
        get_result = requests.get(api_call_path)

        print(get_result.content)

    def __get_nested_resource_of_type(self, resource: str, specific: str, secondary_resource: str) -> None:
        base_path = f"https://gorest.co.in/public/v2/{resource}/{specific}/{secondary_resource}"
        api_call_path = link_modifiers.append_key_to_path(base_path, self._api_key)
        get_result = requests.get(api_call_path)

        print(get_result.content)