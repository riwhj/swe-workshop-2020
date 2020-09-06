import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):
    def test_validate_name_with_valid_input(self):
        self.assertEqual(True, validate_name("ดีมดี่"))

    def test_validate_name_with_invalid_input_int(self):
        self.assertEqual(False, validate_name("1234"))

    def test_validate_name_with_invalid_input_string_and_int(self):
        self.assertEqual(False, validate_name("ดีมดี่1234"))

    def test_validate_name_with_invalid_input_special(self):
        self.assertEqual(False, validate_name("@!#$%"))

    def test_validate_name_with_invalid_input_space(self):
        self.assertEqual(False, validate_name("ก่อ กฤษฎิ์"))

    def test_validate_name_with_invalid_input_no_value(self):
        self.assertEqual(False, validate_name(""))

    

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
