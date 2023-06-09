import json
from pymongo import MongoClient
from bson.json_util import dumps



class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        uri = "mongodb://aacuser:SNHU1234@127.0.0.1:27017/?authSource=AAC&authMechanism=SCRAM-SHA-1"
        self.client = MongoClient(uri)
     # The database used by the client
        self.database = self.client['AAC']
     # The collection used by the database
        self.collections = self.database['animals']
         
# Create Method       
    def create(self,key_value_pairs: dict):
        try:    
            if isinstance(key_value_pairs,dict):
            # insert the document into AAC.animals collection
                self.database.animals.insert_many(key_value_pairs)  # data should be dictionary
            else:
                self.database.animals.insert_one(key_value_pairs)
                return True    
                

        except Exception as e:
            return e

# Read Method
    def read(self,key_value_pairs: dict):
        try:
            # search AAC.animals for specific values
            results = self.database.animals.find(key_value_pairs)
            
            return results

         # If error return the error message
        except Exception as e:
            return e

# Update Method
    def update(self, pairToFind: dict, pairToReplace: dict):
        try:
                # try updating the document that matches the criteria
                result = self.database.animals.update_one(pairToFind, pairToReplace)
                # return json object
                json_object = json.dumps(result.raw_result, indent=4)
                return json_object
            
                # if the update_one function was successful, return true
                if result.modified_count != 0:
                    print("Successfully updated document")

                else:
                    print("Failed to update document")

        # if an update error occurred, return the error
        except Exception as e:
            return e
# Delete Method
    def delete(self, key_value_pairs: dict):

        try:
            # try to delete a document in the database with the argument values
            result = self.database.animals.delete_one(key_value_pairs)
            # return json object
            json_object = json.dumps(result.raw_result, indent=4)
            return json_object
            # return json version of deleted object only if delete count was not 0
            if result.deleted_count > 0:
                print("Deletion successful")

            else:
                print("Failed to delete document")

        
        # if a deletion error occurred, return the error
        except Exception as e:
            return e