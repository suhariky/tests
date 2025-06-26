import unittest
from unittest.mock import patch
import io

class TestHelloInput(unittest.TestCase):
    @patch('builtins.input', return_value='Алиса')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_greeting(self, mock_stdout, mock_input):
        import hello_input
        self.assertIn('Привет, Алиса!', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main() 