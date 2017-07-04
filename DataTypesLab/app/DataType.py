

def data_type(data):
    if data == None:
        return "no value"

    elif isinstance(data, bool):

        return data
    elif isinstance(data, str):

        return len(data)
    elif isinstance(data, int):

        if data == 100:
            return "equal to 100"
        elif data >= 100:
            return "more than 100"
        return "below 100"

    elif isinstance(data, list):
        if len(data) < 3:
            return None
        return len(data)