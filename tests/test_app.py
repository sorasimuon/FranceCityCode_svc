import unittest
from src.app import app


class Test_App(unittest.TestCase):

    def setUp(self):
        """
        Create a test client before each test
        """
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_code(self):
        """
        Check URL "/" returns 200
        """
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_get_city_error(self):
        """
        Check errors in URL GET /city
        """
        # Check error parameter name
        response = self.app.get("/city?nam=Magny+Le+Hongre", content_type='html/text')
        self.assertEqual(str(response.data, encoding="utf8"), "Error: Invalid parameters")

        # check error too many parameters
        response = self.app.get("/city?name=Serris&insee=10293")
        self.assertEqual(response.status_code, 400)

        # check error data not found
        response = self.app.get('/city?name=FakeCity')
        self.assertEqual(response.status_code, 400)




if __name__ == "__main__":
    unittest.main()

    

