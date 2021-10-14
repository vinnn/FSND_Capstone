# ----------------------------------------------------------------------------#
# Imports.
# ----------------------------------------------------------------------------#
# print('__file__={0:<35} | __name__={1:<25} | __package__={2:<25}'.format(__file__,__name__,str(__package__)))


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


        self.castassistant_jwt = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJUdEl4MFNJZVNLRlpXMkFpbFMxMiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2Fwc3RvbmUtdGVuYW50LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTVkYTAzZWFmMGM3NTAwNjkxNTZiOGIiLCJhdWQiOiJmc25kLWNhcHN0b25lLWFwaS1pZGVudGlmaWVyIiwiaWF0IjoxNjM0MjA0MDg4LCJleHAiOjE2MzQyOTA0ODgsImF6cCI6IjVEeFBsQ2tPYUdDSWJmUHg2bFlVMXpuaEZqaUVpRnNDIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.ua1CjrluoPgZDlPKK2UJokTfSeCnGOv5L-4UjZ_fWIp1PclvBZrdTzQdpEIcIpVqOjFgg3AFdIkhUiFcJjoLxDNn77RZMqEOJ2xURG6c-KO-oiTzT_ZJkzUOgw4pB5Bxv_wc60GSEtDUdTXRQ_z4UdmzPdfO1Ire5zGBNM2esodq3lh8bdAsJgV7QGst9t0qyP1xyxJjn2RdYClGIGiIVc_GwMoHwmb0IaSHZWyXBpXYRJ6OuzfLVkQYGUZKE79NmXbq2BXN5MrkK_sNkr2zgrpmJQjKN-9EOPGBdtGVj72lk4tYfZRrWV_rP7_v2cvT4FN9aq9oVHW4BRurrGnk9w'

        self.prodexec_jwt = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJUdEl4MFNJZVNLRlpXMkFpbFMxMiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2Fwc3RvbmUtdGVuYW50LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTYwMWEyZjVjZDk2YjAwNzAyZDA5NGUiLCJhdWQiOiJmc25kLWNhcHN0b25lLWFwaS1pZGVudGlmaWVyIiwiaWF0IjoxNjM0MjA0ODE0LCJleHAiOjE2MzQyOTEyMTQsImF6cCI6IjVEeFBsQ2tPYUdDSWJmUHg2bFlVMXpuaEZqaUVpRnNDIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.5VDTMXjy7oc_EqXi5ImwygbCVfvb-iEF6fyWxJG2HBwfbjiOZZyRDU431wqsMvy8MElX1Yy79mm3LzRJPa2mA4Mluq3_aMdjwXT4Nz95KzIhlzgrkD32KYUK-NtlIOue-4AEczVQuZPXvFduEe3RvhzKwna4f9G7QMevV1phglE39IkZcNzcZ4cyNLmDYn3aSPIwfMN7r3Ij4_sslcJSM7gTsz_FUVZa9NSxxitc5i5CFimMItZaFUMrxXwP4Xc6V6-67jFj2hENXq_XUtdPKHs23GFeVnK9G-f7NFiFZdo3EiU4gsddQSU8B0HfzS8EmLYlWWCida0FBHxwacawWw'


        # MODIFIED END


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # creates a new question object, to be used
        # in the POST question tests:
        self.new_actor = {
            'name': 'Titi?',
            'age': 40,
            'gender': 'Male', 
        }
        self.update_actor = {
            'name': 'actor3newname',
            'age': 100,
            'gender': 'Male', 
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
        res = self.client().get('/actors2',
            headers={'Authorization':'Bearer'+ self.castassistant_jwt}
            )
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
        res = self.client().get('/actors',
            headers={'Authorization':'Bearer '+ self.castassistant_jwt}
            )
        
        # Load the data using json.loads:
        data = json.loads(res.data)

        # check responses:
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[0]['success'], True)
        self.assertTrue(data[0]['actors'])  # check the result contains 'actors' dictionary

  # Test. [DELETE ACTOR id => OK ]
  # ----------------------------------------#    
    # def test_200_delete_actor(self):
        # Get response by making client make the DELETE request:
        # res = self.client().delete('/actors/8',
        #     headers={'Authorization':'Bearer '+ self.prodexec_jwt}
        #     )        

        # # Load the data using json.loads:
        # data = json.loads(res.data)

        # # check responses:
        # self.assertEqual(res.status_code, 200)
        # self.assertEqual(data[0]['success'], True)


  # Test. [DELETE NON-EXISTENT ACTOR => ERROR ]
  # ----------------------------------------#    
    def test_404_delete_nonexistent_actor(self):
        # Get response by making client make the GET request:
        res = self.client().delete('/actors/2000',
            headers={'Authorization':'Bearer '+ self.prodexec_jwt}
            )                
        # Load the data using json.loads:
        data = json.loads(res.data)

        print("DATA : ")
        print(data)

        # check responses:
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

  # Test. [POST ACTOR id => OK ]
  # ----------------------------------------#    
    # def test_200_post_actor(self):
    #     # Get response by making client make the 
    #     # POST request (new_question is defined above):
    #     res = self.client().post('/actors', 
    #         json=self.new_actor,
    #         headers={'Authorization':'Bearer '+ self.prodexec_jwt}            
    #         )
    #     # Load the data using json.loads:
    #     data = json.loads(res.data)

    #     # check responses:
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data[0]['success'], True)


  # Test. [POST ACTOR WITH NO INFO => ERROR ]
  # ----------------------------------------#    
    def test_422_post_wrong_actor_info(self):
        # Get response by making client make the 
        # POST request, without json input info:
        res = self.client().post('/actors', 
            json='wrongactor',
            headers={'Authorization':'Bearer '+ self.prodexec_jwt}            
            )
        # Load the data using json.loads:
        data = json.loads(res.data)

        # check responses:
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

  # Test. [PATCH ACTOR id => OK ]
  # ----------------------------------------#    
    def test_200_patch_actor(self):
        # Get response by making client make the 
        # PATCH request (update_actor is defined above):
        res = self.client().patch('/actors/3', 
            json=self.update_actor,
            headers={'Authorization':'Bearer '+ self.prodexec_jwt}            
            )

        # Load the data using json.loads:
        data = json.loads(res.data)

        # check responses:
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[0]['success'], True)


  # Test. [PATCH ACTOR WITH NO INFO => ERROR ]
  # ----------------------------------------#    
    def test_422_patch_no_patchdata(self):
        # Get response by making client make the 
        # PATCH request, without json input info:
        res = self.client().patch('/actors/3', 
            json='wrongpatch',
            headers={'Authorization':'Bearer '+ self.prodexec_jwt}            
            )

        # Load the data using json.loads:
        data = json.loads(res.data)

        # check responses:
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()


