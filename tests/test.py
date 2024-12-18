import unittest
from unittest.mock import patch
from time import gmtime, strftime
from boLogger.boLogger import Logging, CustomLog  # Adjust import path as needed

class TestLogging(unittest.TestCase):
    time = strftime("[%d/%m/%y %H:%M:%S] ", gmtime())
    
    def test_header_log(self):
        # Capture print output
        with patch('builtins.print') as mock_print:
            logger = Logging()
            logger.header("Test Header")
            
            # Assert print was called with expected output
            mock_print.assert_called_once_with(
                f'\033[95m{self.time}HEADER....:\033[0m Test Header\033[0m'
            )

    def test_info_log(self):
        # Capture print output
        with patch('builtins.print') as mock_print:
            logger = Logging()
            logger.info("Test Info")
            
            # Assert print was called with expected output
            mock_print.assert_called_once_with(
                f'\033[96m{self.time}INFO......:\033[0m Test Info\033[0m'
            )


    def test_error_log(self):
        # Capture print output
        with patch('builtins.print') as mock_print:
            logger = Logging()
            logger.error("This should show an error message")
            
            # Assert print was called with expected output
            mock_print.assert_called_once_with(
                f'\033[91m{self.time}ERROR.....:\033[0m This should show an error message\033[0m'
            )


class TestCustomLog(unittest.TestCase):
    time = strftime("[%d/%m/%y %H:%M:%S] ", gmtime())
    
    def test_set_default(self):
        # Capture print output
        with patch('builtins.print') as mock_print:
            logger = CustomLog()
            result = logger.set_default("info", "Cyan", bold=True, underlined=False)
            self.assertTrue(result)
            
            logger.view_deafult()
            
            # Note: You might need to adjust the exact string based on your implementation
            mock_print.assert_called_with(
                f'\033[96m{self.time}INFO......:\033[0m Default settings: Title=\'info\', Color=\'Cyan\', Bold=True, Underlined=False\033[0m'
            )

    
    def test_custom_log(self):
        # Capture print output
        with patch('builtins.print') as mock_print:
            logger = CustomLog()
            logger.set_default("warning", "Yellow")
            logger.custom_log("This is a custom log")
            
            mock_print.assert_called_once_with(
                f'\033[33m{self.time}WARNING...:\033[0m This is a custom log\033[0m'
            )

if __name__ == '__main__':
    unittest.main()