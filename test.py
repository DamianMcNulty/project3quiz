from runserver import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get('/hello', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    # / contains 'Hello, World!'
    def test_hello_name(self):
        tester = app.test_client(self)
        response = tester.get('/hello', content_type='html/text')
        self.assertTrue(b'Hello, World!', response.data)

if __name__ == '__main__':
    unittest.main()