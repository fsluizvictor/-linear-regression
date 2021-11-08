import unittest
from mock import MagicMock
from flat import service
from flat.models import MyClass
from datetime import datetime

class TestService(unittest.TestCase):
    """Service unit test"""
    
    def test_get(self):
        uid = "ab"
        ret = service.get_object(uid)
        service.repository = MagicMock()
        service.repository.get = MagicMock(return_value=dict(uid=uid, 
                                                             createdAt=datetime.now(),
                                                             modifiedAt=datetime.now()))
        self.assertEqual(ret.uid, uid)
        self.assertInstanceOf(ret, MyClass)