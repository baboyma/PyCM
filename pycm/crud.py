"""
File: pycm/crud.py
Author: Baboyma Kagniniwa
Date: 2023-09-03
Description: CRUD Functions for credentials management
"""

from getpass import getpass
import keyring as kr

def get_accounts() -> list:
    """Get list of all keyring service names

    Return: list of service names
    """

def get_keys(account: str) -> list:
    """Get list of keys associated with an account.

    Args:
        account -- Name of keyring service
    Returns:
        list: a list of keys
    """
    accnts = kr.get_credential(service_name = account, username = None)

    print(accnts)

    if accnts is None:
        print(f"No keys found for {account}")
        return []

    return accnts.keys()

def check_key(account:str, key:str) -> bool:
    """Check if key is associated with an account

    Args:
        account -- Keyring service name
        key -- Name of key associated with account
    Returns:
        bool: True (yes) or False (no)
    """

    keys = get_keys(account = account)

    if key in keys:
        return True

    print(f'No {key} key  found in {account} account')

    return False

def create_key(account: str, key: str, secret: str = None) -> bool:
    """Create new keyring key/value pair for for a given service.

    Args:
        account -- Name of keyring service
        key -- Username of specified keyring service
        secret -- Password of keyring service username. Defaults to None.
    Returns:
        bool: process outcome of create_key
    """

    if check_key(account, key) is True:
        print(f"{key} exists in specified service. \
              Use read_value() to get the value or update_value() to update existing account.")
        return False

    if secret is None:
        secret = getpass(prompt=f'Enter the value for {key} in {account}: ')

    kr.set_password(service_name = account,
                    username = key,
                    password = secret)

    return True

def read_secret(account: str, key: str) -> str:
    """Get secret of account key

    Args:
        account -- Name of keyring service
        key -- Username of keyring service
    Returns:
        str: Password of keyring service username
    """
    secret = ""

    if check_key(account, key) is True:
        secret = kr.get_password(service_name = account, username = key)

    return secret

def update_secret(account: str, key: str, secret: str) -> bool:
    """Update existing keyring key/value pair for a given service

    Args:
        service -- service name
        username -- account username
        password -- account password
    Returns:
        bool: outcome of update_account process
    """

    if check_key(account, key) is False:
        print(f"{key} does not exist in specified service. \
            Consider using create_account() to add new account")
        return False

    kr.set_password(service_name = account,
                    username = key,
                    password = secret)

    return True

def delete_key(account:str, key:str) -> bool:
    """Delete existing username/password pair for a given keyring service

    Args:
        account -- service name
        key -- account username
    Returns:
        bool: outcome of delete_key process
    """

    if check_key(account, key) is False:
        print(f"{key} does not exist in specified service")
        return False

    kr.delete_password(service_name = account,
                       username = key)

    return True
