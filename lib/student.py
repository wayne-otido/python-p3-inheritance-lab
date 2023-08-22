#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__("My", "Student")
        self.knowledge = []
    
    def learn(self, new_info):
        self.knowledge.append(new_info)