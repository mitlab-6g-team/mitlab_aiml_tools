def format_actor_string(input_str):
    if "_" in input_str:
        result_str = input_str.title().replace("_", "")
    else:
        result_str = input_str.capitalize()
    return result_str
