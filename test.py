from runserver import app
import unittest


class FlaskTestCase(unittest.TestCase):

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
    
    # login route works ok
    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    # login.html contains 'Enter username'
    def test_login_has_username(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Enter username', response.data)

    # login.html contains 'Play'
    def test_login_has_play(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Play', response.data)

    #Given a user called f1 the user can play the quiz
    def test_login_with_user(self):
        tester = app.test_client(self)
        response = tester.post(
        '/login',
        data=dict(name="f1"),
        follow_redirects=True
        )
        self.assertTrue(b'Player: f1', response.data)
 
    # Given a user called f1, another user called f1 can't play the quiz
    def test_username_login_again(self):
        tester = app.test_client(self)
        response = tester.post(
        '/login',
        data=dict(name="f1"),
        follow_redirects=True
        )
        response = tester.post(
        '/login',
        data=dict(name="f1"),
        follow_redirects=True
        )
        self.assertIn(b'The user name f1 is taken, try another username', response.data)
    
    # logout route works ok
    # def test_logout(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/logout', content_type='html/text')
    #     self.assertTrue(response.status_code, 200)

    # leaderboard.html contains 'Leaderboard'
    # def test_leaderboard_name(self):
    #     tester = app.test_client(self)
    #     response = tester.post(
    #     '/login',
    #     data=dict(name="f1"),
    #     follow_redirects=True
    #     )
    #     response = tester.get('/logout', content_type='html/text')
    #     self.assertTrue(b'Leaderboard', response.data)
  
    # game.html works ok
    def test_game(self):
        tester = app.test_client(self)
        response = tester.get('/game', content_type='html/text')
        self.assertTrue(response.status_code, 200)

     # A user answers the first question with the answer D
    # def test_game_answer(self):
    #     tester = app.test_client(self)
    #     response = tester.post(
    #     '/game',
    #     data=dict(answer="D"),
    #     follow_redirects=True
    #     )
    #     self.assertTrue(b'question 2', response.data)

     # A user answers the first 2 questions and the user's leaderboard score is 2
    # def test_leaderboard_score(self):
    #     tester = app.test_client(self)
    #     response = tester.post(
    #     '/game',
    #     data=dict(answer="D"),
    #     follow_redirects=True
    #     )
    #     response = tester.post(
    #     '/game',
    #     data=dict(answer="A"),
    #     follow_redirects=True
    #     )
    #     response = tester.post(
    #     '/leaderboard'
    #     )
    #     self.assertIn(b'2', response.data)

if __name__ == '__main__':
    unittest.main()