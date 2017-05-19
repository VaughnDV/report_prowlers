from app import app
import unittest

class FLaskTestCase(unittest.TestCase):

    # Ensure that flask route is set up correctly
    def test_index(self):
        # mocks out the fuctionality of the app
        tester = app.test_client(self)
        # tests '/' url
        response = tester.get('/', content_type='html/test')
        # checks response code is 200
        self.assertEqual(response.status_code, 200)


    # Ensure that apecified content is on page
    def test_index_loads(self):
        # mocks out the fuctionality of the app
        tester = app.test_client(self)
        # tests '/' url
        response = tester.get('/', content_type='html/test')
        # checks for content 'Report Prowlers' on page
        self.assertEqual(b'Report Prowlers' in response.data)


    

if __name__ == '__main__':
    unittest.main()