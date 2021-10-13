# ----------------------------------------------------------------------------#
# Imports.
# ----------------------------------------------------------------------------#
print('__file__={0:<35} | __name__={1:<25} | __package__={2:<25}'.format(__file__,__name__,str(__package__)))


import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from .api import create_app   # import the app=Flask(__name__) from api.py
from .database.models import setup_db, Actor  # import funtions and models form models.py


# ----------------------------------------------------------------------------#
# Test Class.
# ----------------------------------------------------------------------------#
class CastingTestCase(unittest.TestCase):
    """This class represents the Casting test case"""

    # Setup.
    # ----------------------------------------#
    def setUp(self):
        """Executed before each test. 
        Define test variables and initialize app."""


        # MODIFIED START
#        self.app = create_app()
#        self.client = self.app.test_client
        self.app = create_app()
        self.client = self.app.test_client

#        self.database_name = "casting_test"
#        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)        
        self.database_filename = "database11_test.db"
        self.project_dir = os.path.dirname(os.path.abspath(__file__))
        self.database_path = "sqlite:///{}".format(os.path.join(self.project_dir, self.database_filename))
#        setup_db(self.app, self.database_path)
        setup_db(self.app)   #, self.database_path)
        # MODIFIED END


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # creates a new question object, to be used
        # in the POST question tests:
        self.new_question = {
            'question': 'Who is Titi?',
            'answer': 'Your cat',
            'difficulty': 1,
            'category': 1 
        }
        self.new_search = {
            'searchTerm': 'creator'
        }
        self.new_quiz = {
          'quiz_category': {'type': 'Geography', 'id': '3'},
          'previous_questions': []
        }

  # Teardown.
  # ----------------------------------------#    
    def tearDown(self):
        """Executed after reach test"""
        pass

  # Test. [GET NON-EXISTENT URL => ERROR ]
  # ----------------------------------------#    
    def test_404_nonexistent_url(self):
        # Get response by making client make the GET request:
        res = self.client().get('/actors2')
        # Load the data using json.loads:
        data = json.loads(res.data)

        # check responses:
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

  # Test. [GET ACTORS => OK ]
  # ----------------------------------------#    
    def test_200_get_categories(self):
        # Get response by making client make the GET request:
        res = self.client().get('/actors')
        # Load the data using json.loads:
        data = json.loads(res.data)

        # check responses:
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[0]['success'], True)
        self.assertTrue(data[0]['actors'])  # check the result contains 'actors' dictionary


        # print('PRINT RES:')
        # print(res)


        # print('PRINT DATAA:')
        # print(data)

        # print("data['success']")
        # print(data[0]['success'])


  # Test. [DELETE ACTOR id => OK ]
  # ----------------------------------------#    
    # def test_200_delete_actor(self):
    #     # Get response by making client make the GET request:
    #     res = self.client().delete('/questions/2')
    #     # Load the data using json.loads:
    #     data = json.loads(res.data)

    #     # check responses:
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted'], True)

  # Test. [DELETE NON-EXISTENT ACTOR => ERROR ]
  # ----------------------------------------#    
    # def test_422_delete_nonexistent_actor(self):
    #     # Get response by making client make the GET request:
    #     res = self.client().delete('/questions/2000')
    #     # Load the data using json.loads:
    #     data = json.loads(res.data)

    #     # check responses:
    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')

  # Test. [POST ACTOR id => OK ]
  # ----------------------------------------#    
    # def test_200_post_actor(self):
    #     # Get response by making client make the 
    #     # POST request (new_question is defined above):
    #     res = self.client().post('/questions', json=self.new_question)
    #     # Load the data using json.loads:
    #     data = json.loads(res.data)

    #     # check responses:
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['created'], True)

  # Test. [POST ACTOR WITH NO INFO => ERROR ]
  # ----------------------------------------#    
    # def test_422_post_wrong_actor_info(self):
    #     # Get response by making client make the 
    #     # POST request, without json input info:
    #     res = self.client().post('/questions')
    #     # Load the data using json.loads:
    #     data = json.loads(res.data)

    #     # check responses:
    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')

  # Test. [PATCH ACTOR id => OK ]
  # ----------------------------------------#    
    # def test_200_patch_actor(self):
    #     # Get response by making client make the 
    #     # POST request (new_question is defined above):
    #     res = self.client().post('/searched_questions', json=self.new_search)
    #     # Load the data using json.loads:
    #     data = json.loads(res.data)

    #     # check responses:
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)


  # Test. [PATCH ACTOR WITH NO INFO => ERROR ]
  # ----------------------------------------#    
    # def test_422_patch_no_patchdata(self):
    #     # Get response by making client make the 
    #     # POST request, without json input info:
    #     res = self.client().post('/searched_questions')
    #     # Load the data using json.loads:
    #     data = json.loads(res.data)

    #     # check responses:
    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()


