def get_val(collection: dict, key: str, default='git'):
    # return collection.get(key, default)
    if key in collection:
        return collection[key]

    return default
