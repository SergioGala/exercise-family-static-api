
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
init_members=[
        {  #id:self._generated_Id(),
           "name": "Jhon",
           #"last_name": "Jackson",
           "age": [33],
           "lucky_numbers": [7,13,22]
        },
        {  #id:self._generated_Id(),
           "name": "Jane",
           #"last_name": "Jackson",
           "age": [35],
           "lucky_numbers": [10,14,3]
        },
        {  #id:self._generated_Id(),
           "name": "Jimmy",
           #"last_name": "Jackson",
           "age": [5],
           "lucky_numbers": [1]
        },
        ]
class FamilyStructure:
    def __init__(self, last_name, members=[]):
        self.last_name = last_name
        self._next_id = 1
        # example list of members
        self._members = []
        [self.add_member(member) for member in members]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
       generated_id = self._next_id
       self._next_id += 1
       return generated_id

    def add_member(self, member):
        # fill this method and update the return

        pass

    def delete_member(self, id):
        # fill this method and update the return
        pass

    def get_member(self, id):
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
