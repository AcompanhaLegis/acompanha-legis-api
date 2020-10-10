from django.test import TestCase
from user.serializers import NewUserSerializer
from user.models import CustomUser

class NewUserSerializerTestCase(TestCase):
    def setUp(self):
        pass

    def test_create(self):
        fake_user = {
            "email": "blabla@gmail.com",
            "password": "123deoliveira4",
        }
        new_user_serializer = NewUserSerializer()
        user = new_user_serializer.create(fake_user)

        self.assertEqual(user.email, "blabla@gmail.com")
        self.assertTrue(user.check_password("123deoliveira4"))
           