from vvvv import VVVVClient

def test_client_without_args():
    vvvv = VVVVClient()
    return True

def test_client_with_args():
    vvvv = VVVVClient('127.0.0.01', '4444')
    return True
