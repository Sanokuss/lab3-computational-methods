import unittest
from main import app

class TestNewtonAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_calculate_success(self):
        # Перевіряємо коректний POST-запит із JSON
        response = self.app.post('/calculate', json={"x": 5})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "success")

    def test_calculate_no_data(self):
        # Перевіряємо помилку при відсутності даних
        response = self.app.post('/calculate', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
