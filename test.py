import unittest
from student_crud import StudentRegistrationSystem  # Assuming the file is named crud.py


class TestStudentRegistrationSystem(unittest.TestCase):
    def setUp(self):
        # Initialize the Student Registration System
        self.system = StudentRegistrationSystem()

    def test_create_student(self):
        # Test creating a new student
        result = self.system.create_student(1, "Alice", 20, "Computer Science")
        self.assertTrue(result)  # Assert that the creation was successful

        # Test creating a student with an existing ID
        result = self.system.create_student(1, "Bob", 21, "Mathematics")
        self.assertFalse(result)  # Assert that creation fails due to duplicate ID

    def test_read_student(self):
        # Test reading an existing student
        self.system.create_student(1, "Alice", 20, "Computer Science")
        result = self.system.read_student(1)
        self.assertEqual(result, 1)  # Assert that the student ID is returned

        # Test reading a non-existent student
        result = self.system.read_student(2)
        self.assertIsNone(result)  # Assert that None is returned for non-existent student

    def test_read_all_students(self):
        # Test reading students when none exist
        result = self.system.read_all_students()
        self.assertEqual(result, [])  # Assert that an empty list is returned

        # Test reading multiple students
        self.system.create_student(1, "Alice", 20, "Computer Science")
        self.system.create_student(2, "Bob", 22, "Mathematics")
        result = list(self.system.read_all_students())
        self.assertEqual(len(result), 2)  # Assert that two students are returned

    def test_update_student(self):
        # Test updating an existing student
        self.system.create_student(1, "Alice", 20, "Computer Science")
        result = self.system.update_student(1, name="Alicia", age=21, major="Physics")
        self.assertTrue(result)  # Assert that the update was successful

        # Test updating a non-existent student
        result = self.system.update_student(2, name="Bob")
        self.assertFalse(result)  # Assert that the update fails for non-existent student

    def test_delete_student(self):
        # Test deleting an existing student
        self.system.create_student(1, "Alice", 20, "Computer Science")
        result = self.system.delete_student(1)
        self.assertTrue(result)  # Assert that the deletion was successful

        # Test deleting a non-existent student
        result = self.system.delete_student(2)
        self.assertFalse(result)  # Assert that the deletion fails for non-existent student


if __name__ == "__main__":
    unittest.main()
