import json
import sys
from json.decoder import JSONDecodeError


class Login:
    """Creator username and password, load username and password"""

    def __init__(self):
        """Initialize"""
        self.__username = None
        self.__password = None
        self.__file = 'info.json'

    def __get_info(self):
        """Get information (username, password)"""
        try:
            # Get all usernames for duplication cases
            cases = []
            # Get content of file
            content = self.read()
            # Check status of content
            if content:
                # Appending usernames
                for value in content.values():
                    cases.append(value['username'])
            # Check operation
            status_user, status_pass = False, False
            # Get username
            self.__username = input('username: ')
            # Convert username to lowercase
            self.__username = self.__username.lower()
            if not self.__username:
                raise Exception('Empty username!')
            # Check duplicate username
            elif self.__username in cases:
                self.__username = ''
                raise Exception(
                    'Please choice a another username, this is duplicated!')
            else:
                status_user = True
                # Get password
                self.__password = input('password: ')
                # Convert password to lowercase
                self.__password = self.__password.lower()
                if not self.__password:
                    raise Exception('Empty password!')
                else:
                    status_pass = True
        # Except json decode error
        except JSONDecodeError:
            pass
        # Except exception erorr
        except Exception as e:
            print(e)
        finally:
            # Checking operation
            if status_user and status_pass:
                print('Done!')
                return True
            else:
                print('Incomplete operation!')
                # Exit from program
                sys.exit()

    def __convert_to_dict(self):
        """Convert username and password to dictionary"""
        content = self.read()
        # Check content
        if content:
            # Get last user id
            for key in content.keys():
                user_id = key
            # Convert user id to list and assignment new id
            id_plus = user_id.split('user')
            id_plus = int(user_id[-1]) + 1
            user = 'user{}'.format(id_plus)

        else:
            user = "user0"
        # A data layout dictionary
        data = {
            user: {
                "username": self.__username,
                "password": self.__password
            }
        }
        # Check content for empty
        if content:
            content.update(data)
            return content
        # Return first data(a new file created)
        return data

    def add(self):
        """Create file for store information"""
        try:
            # Get information from user
            self.__get_info()
            # Convert data to dictionary(json)
            info = self.__convert_to_dict()
            # Write file
            self.write(info)
        except Exception as e:
            print('Incomplete write operation({})'.format(e))

    def remove(self):
        """Remove user with username"""
        try:
            # Get username for remove user
            username = input('Enter username for remove: ')
            # Convert username to lowercase
            username = username.lower()
            # Check empty username
            if not username:
                raise Exception('Empty username!')
            # Load file
            content = self.read()
            # Status for check username(founded or not founded)
            status = False
            # Check username for remove user
            for key in content.keys():
                if content[key]['username'] == username:
                    del content[key]
                    status = True
                    break
            # Check status
            if status:
                # Write new content
                self.write(content)
                print('Done')
            else:
                print('Your username is not found!')
        # Except exception errors
        except Exception as e:
            print('Incomplete remove operation({})'.format(e))

    def read(self):
        """Load information file"""
        try:
            # Load file
            with open(self.__file) as f:
                content = json.load(f)
            return content
        except FileNotFoundError:
            # Create file if isn't exist
            with open(self.__file, 'w') as f:
                return False
        except JSONDecodeError:
            pass

    def write(self, content, type='w'):
        """Writing to file"""
        try:
            with open(self.__file, type) as f:
                json.dump(content, f)
        except Exception as e:
            print(e)

    def login(self):
        """Login user"""
        content = self.read()
        # Status check user login
        status = True
        try:
            while status:
                # Check content
                if content:
                    print('====== Login ======')
                    # Get username
                    username = input('username: ')
                    # Convert username to lowercase
                    username = username.lower()
                    # Check empty username
                    if not username:
                        raise Exception('Empty username!')
                    # Get password
                    password = input('password: ')
                    # Convert password to lowercase
                    password = password.lower()
                    if not password:
                        raise Exception('Empty password!')
                    # Get value of users and check username and password
                    for value in content.values():
                        if username == value['username'] and password == value['password']:
                            status = False
                            print('Logining Done!')
                            break
                    if status:
                        print('Your username or password is not correct!')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    login = Login()
    login.add()
    login.add()
    login.add()
    login.add()
    login.remove()
    login.login()
