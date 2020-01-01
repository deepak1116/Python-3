# The logic to check all type of JSONTypes inside the
# JSON file .
def dictionary_convert(dictionary):
    for obj_key, value in dictionary.items():
        if not isinstance(value, (dict, list)):
            # The obj_key is key/value pair.No sub JSONType is present
            value = crypt.object_encrypt(value)
            dictionary.update({obj_key: value})
        else:
            # If the dictionary contain type dict or list again call
            # inne_check() method to check the type is dict or list.
            inner_check(value)
    return dictionary


def list_convert(list_obj):
    for value in list_obj:
        if not isinstance(value, (dict, list)):
            # No sub JSONType is present.The object is key/value pair.
            index = list_obj.index(value)
            list_obj[index] = crypt.object_encrypt(value)
        else:
            inner_check(value)
    return list_obj


def inner_check(object):
    # Dividing check to figure out what type of object
    if isinstance(object, dict):
        object = dictionary_convert(object)
    elif isinstance(object, list):
        object = list_convert(object)
    return object
