import json


def func1(prefix, name):
    return prefix + ", " + name + "!"


def handler(event, context):

    return {
        'statusCode': 200,
        'body': json.dumps(func1("Oh hai", "Rai"))
    }