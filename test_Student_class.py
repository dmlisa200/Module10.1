import unittest
from Student_class import Student

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = student.Student('Kilmer, 'Lisa')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Kilmer')
        self.assertEqual(self.student.first_name, 'Lisa')

    def test_object_created_all_attributes(self):
        student = student.Student('Kilmer', 'Lisa', 'CS', '3.5')
        assert student.last_name == 'Kilmer'
        assert student.first_name == 'Lisa'
        assert student.major == 'CS'
        assert student.gpa == '3.5'

    


if __name__ == '__main__':
    unittest.main()
