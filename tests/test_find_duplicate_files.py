import unittest
from unittest import mock
from problems.find_duplicate_files import find_duplicate_files


class Test(unittest.TestCase):

    @mock.patch('problems.find_duplicate_files.os.listdir')
    def test_something(self, mock_listdir):
        mock_listdir.return_value = ['blah.txt', 'bah.txt', 'bo.txt']
        result = find_duplicate_files('/blas')
        print(f"result: {result}")
        self.assertEqual(2, len(result))
