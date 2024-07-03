import re

class Validate:

    def __init__(self) -> None:
        pass

    def is_ID(self, string: str) -> bool:
        '''
        Checks if a string is alphbetic.
        
        Args:
            string (str): An ID of a user.

        Returns: True if the string is continuous digits.
                False otherwise.
        '''
        check_list: list = string.split()
        if len(check_list) == 1 and check_list[0].isdigit():
            return True
        else:
            return False

    # - Validate user inputs to ensure correctness.
    def is_alphabetic(self, string: str) -> bool:
        '''
        Checks if a string is alphbetic.
        
        Args:
            string (str): A name of a user.

        Returns: True if the string as alphabetic.
                False otherwise.
        '''
        check_list: list = string.split()
        for name in check_list:
            if name.isalpha():
                continue
            else:
                return False
        return True
    
    # - Validate user inputs to ensure correctness.
    def is_email(self, email: str) -> bool:
        '''
        Checks if a string follows this pattern: "email@domain.TLD".
        
        Args:
            string (str): An email.

        Returns: True if the string follows this pattern: "email@domain.TLD".
                False otherwise.
        '''
        # return True
        pattern: str = "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$"
        if re.match(pattern, email) is None:
            return False
        else:
            return True
    
    