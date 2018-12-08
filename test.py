from runserver import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get('/hello', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    # /hello contains 'Hello, World!'
    def test_hello_name(self):
        tester = app.test_client(self)
        response = tester.get('/hello', content_type='html/text')
        self.assertTrue(b'Hello, World!', response.data)
    
     # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    # index.html contains 'Java Quiz'
    def test_index_name(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Java Quiz', response.data)
        
    # Given a user called f1 the user can play the game
    def test_index_username_login(self):
        tester = app.test_client(self)
        response = tester.post(
        '/',
        data=dict(name="f1"),
        follow_redirects=True
        )
        self.assertIn(b'Given the following code:', response.data)
    
        
    # Given a user called f1, another user called f1 can't play the game
    def test_index_username_login_again(self):
        tester = app.test_client(self)
        response = tester.post(
        '/',
        data=dict(name="f1"),
        follow_redirects=True
        )
        response = tester.post(
        '/',
        data=dict(name="f1"),
        follow_redirects=True
        )
        self.assertIn(b'The user name f1 has already been taken', response.data)
        
    # leaderboard.html contains 'Leaderboard'
    def test_leaderboard_name(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Leaderboard', response.data)
    
    # leaderboard route works ok
    def test_leaderboard(self):
        tester = app.test_client(self)
        response = tester.get('/leaderboard', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    # user f1 appears in leaderboard
    def test_leaderboard_user(self):
        tester = app.test_client(self)
        response = tester.post(
        '/',
        data=dict(name="f1"),
        follow_redirects=True
        )
        self.assertIn(b'f1', response.data)
        
    # game.html works ok
    def test_game(self):
        tester = app.test_client(self)
        response = tester.get('/game', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
     # Given a user called f1 the user can play the game
    def test_game_question_num(self):
        tester = app.test_client(self)
        response = tester.post(
        '/',
        data=dict(name="f2"),
        follow_redirects=True
        )
        self.assertIn(b'question 1', response.data)

if __name__ == '__main__':
    unittest.main()