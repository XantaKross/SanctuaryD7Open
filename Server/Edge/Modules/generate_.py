dataset = {
    'generate_': [
        'generate a random number',
        'give me any random number'
    ]
}


def objective(func, cmd, func_dict):
    from random import randint
    return str(randint(-100000,100000))