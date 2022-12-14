def is_compatible_resource(resource: str) -> bool:
    return resource in ["users", "posts", "comments", "todos"]
    
def is_good_nested_resource(resource: str, secondary_resource: str) -> bool:
    return (
        (resource == "users" and secondary_resource == "posts") or
        (resource == "users" and secondary_resource == "todos") or
        (resource == "posts" and secondary_resource == "comments")
    )
    
