import testutils
from unittest import TestCase


class Test(TestCase):

    # @classmethod
    # def setup_class(cls):
    #     print('\r\nSetting up the class')
    #     testutils.create_lambda('lambda')
    #
    # @classmethod
    # def teardown_class(cls):
    #     print('\r\nTearing down the class')
    #     testutils.delete_lambda('lambda')

    def test_that_lambda_returns_correct_message(self):
        # payload = testutils.invoke_function_and_get_message('lambda')
        payload_dict = testutils.invoke_function_and_get_message('sls1-local-greet')
        print("payload: " + str(payload_dict))
        expected_message_dict = {'statusCode': 200, 'body': "Oh hai, Rai!"}
        print("expected_message_dict: " + str(expected_message_dict))
        assert payload_dict['body'] == expected_message_dict['body']
        assert payload_dict['statusCode'] == expected_message_dict['statusCode']