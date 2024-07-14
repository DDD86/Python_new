def key_params_to_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        try:
            hash(key)
            key_to_use = key
        except TypeError:
            key_to_use = str(key)  

        result_dict[key_to_use] = value

    return result_dict

params_dict = key_params_to_dict(a=1, b='hello', c=[1, 2, 3], d={'key': 'value'})

for key, value in params_dict.items():
    print(f"{key}: {value}")
