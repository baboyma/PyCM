# ./test/test_crud.py --

"""Import libraries"""
from pycm.crud import check_key, get_keys, create_key, read_secret, update_secret, delete_key
import keyring as kr
#from pytest import TestCase

class TestCrud():
    """Test keyring and crud functions"""

    # def __init__(self) -> None:
    #     kr.set_password(service_name='system',
    #                     username='username',
    #                     password='password')

    def test_default(self):
        """Check default passoword is correct"""
        assert kr.get_password('system', 'username') == 'password'

    def test_check_key(self):
        """Check if test key exisits"""
        assert check_key("system", "username") is True

    def test_create_key(self):
        """Create new key/secret pair for an account"""
        kr.set_password(service_name = "pytest", username = "key", password = "secret")
        assert create_key(account = "pytest", key = "key", secret = "secret") is False

    def test_get_keys(self):
        """Make sure get_keys() returns a list of keys"""
        keys = get_keys(account = "pytest")
        assert len(keys) == 1

    def test_read_secret(self):
        """Get the secret associated with a key for an account"""
        assert read_secret(account = "pytest", key = "key") == "secret"
