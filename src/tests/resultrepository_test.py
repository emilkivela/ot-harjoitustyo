import unittest
from repositories.resultrepository import ResultRepository
from connect_db import get_db_connection

class TestResultRepository(unittest.TestCase):
    def setUp(self):
        self.resultrepository = ResultRepository(get_db_connection())
        self.resultrepository.delete_all()
    
    def test_can_save_info_in_db(self):
        self.resultrepository.save_info('kalle', 10)
        data = self.resultrepository.get_scoreboard()

        self.assertEqual(len(data), 1)