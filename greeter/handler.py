import json


def build_message(prefix, name):
    return prefix + ", " + name + "!"


def greet(event, context):

    return {
        'statusCode': 200,
        'body': json.dumps(build_message("Oh hai", "Rai"))
    }