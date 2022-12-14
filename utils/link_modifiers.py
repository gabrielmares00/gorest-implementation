def append_key_to_path(path: str, api_key: str) -> str:
    return path + f"?access-token={api_key}"