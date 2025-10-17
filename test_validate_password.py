import unittest
from validate_password import validate_password
from validate_password import password_strength


class TestValidate_password(unittest.TestCase):

    def test_validate_password(self):
        password = "Tshepiso@01"
        self.assertEquals(validate_password(password),True)
    
    def test_password_length(self):
        password = "Tshepi"
        self.assertEquals(validate_password(password),False)

    def test_password_numbers_specialchar(self):
        password = "Tshepiso"
        self.assertEquals(validate_password(password),False)

    def test_password_letters(self):
        password = "04568888"
        self.assertEquals(validate_password(password),False)

    #def test_password_not_string(self):
        #password = 54
        #with self.assertRaises((ValueError)):
            #validate_password(password)

    def test_password_strength(self):
        self.assertEquals(password_strength("Tshepi"),"weak")
        self.assertEquals(password_strength("Tshepiso"),"moderate")
        self.assertEquals(password_strength("Tshepiso@01"),"strong")


if __name__ == "__main__":
    unittest.main()

    