from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from .models import Apartment, CustomUser

import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="customuser@gmail.com", password="12345")

    def test_custom_user_model(self):
        user = CustomUser.objects.get(id=1)
        self.assertEqual(user, self.user)
        self.assertEqual(user.email, "customuser@gmail.com")
        self.assertEqual(user.password, "12345")
        


class RoomModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="testuser@gmail.com", password="12345")
        self.room = Apartment.objects.create(
            owner=self.user,
            title="testroom",
            address="testaddress",
            city="testcity",
            state="teststate",
            zipcode="123456",
            description="testdescription",
            price=100,
            bhk=2,
            sqft=1000,
            tenants=0,
            photo="default_image.jpg",
        )

    def test_room_model(self):
        room = Apartment.objects.get(id=1)
        self.assertEqual(room, self.room)
        self.assertEqual(room.owner, self.user)
        self.assertEqual(room.title, "testroom")
        self.assertEqual(room.address, "testaddress")
        self.assertEqual(room.city, "testcity")
        self.assertEqual(room.state, "teststate")
        self.assertEqual(room.zipcode, "123456")
        self.assertEqual(room.description, "testdescription")
        self.assertEqual(room.price, 100)
        self.assertEqual(room.bhk, 2)
        self.assertEqual(room.sqft, 1000)
        self.assertEqual(room.tenants, 0)
        self.assertEqual(room.photo, "default_image.jpg")
        

class RoomListViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="test@gmail.com", password="12345")
        self.room = Apartment.objects.create(
            owner=self.user,
            title="testroom",
            address="testaddress",
            city="testcity",
            state="teststate",
            zipcode="123456",
            description="testdescription",
            price=100,
            bhk=2,
            sqft=1000,
            tenants=0,
            photo="default_image.jpg",
        )

    def test_room_list_view(self):
        response = self.client.get(reverse("room-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testroom")
        self.assertContains(response, "testaddress")
        self.assertContains(response, "testcity")
        self.assertContains(response, "teststate")
        self.assertContains(response, "123456")
        self.assertContains(response, "testdescription")
        self.assertContains(response, "100")
        self.assertContains(response, "2")
        self.assertContains(response, "1000")
        self.assertContains(response, "0")
        self.assertContains(response, "default_image.jpg")


class RoomDetailViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="test@gmail.com", password="12345")
        self.room = Apartment.objects.create(
            owner=self.user,
            title="testroom",
            address="testaddress",
            city="testcity",
            state="teststate",
            zipcode="123456",
            description="testdescription",
            price=100,
            bhk=2,
            sqft=1000,
            tenants=0,
            photo="default_image.jpg",
        )

    def test_room_detail_view(self):
        response = self.client.get(reverse("room-detail", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testroom")
        self.assertContains(response, "testaddress")
        self.assertContains(response, "testcity")
        self.assertContains(response, "teststate")
        self.assertContains(response, "123456")
        self.assertContains(response, "testdescription")
        self.assertContains(response, "100")
        self.assertContains(response, "2")
        self.assertContains(response, "1000")
        self.assertContains(response, "0")
        self.assertContains(response, "default_image.jpg")

'''
class RoomCreateViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="test1@gmail.com", password="12345")

    def test_room_create_view(self):
        self.client.login(email="test1@gmail.com", password="12345")
        print(self.user)
        image_file = open('media/default_image.png', 'rb')
        
        form_data = {
                "owner": self.user,
                "title": "testroom",
                "address": "testaddress",
                "city": "testcity",
                "state": "teststate",
                "zipcode": "123456",
                "description": "testdescription",
                "price": 100,
                "bhk": 2,
                "sqft": 1000,
                "tenants": 0,
                "photo": image_file,
            }
        
        response = self.client.post( 
            reverse("room-list"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Apartment.objects.count(), 1)
        self.assertEqual(Apartment.objects.get(id=1).title, "testroom")
        self.assertEqual(Apartment.objects.get(id=1).address, "testaddress")
        self.assertEqual(Apartment.objects.get(id=1).city, "testcity")
        self.assertEqual(Apartment.objects.get(id=1).state, "teststate")
        self.assertEqual(Apartment.objects.get(id=1).zipcode, "123456")
        self.assertEqual(Apartment.objects.get(id=1).description, "testdescription")
        self.assertEqual(Apartment.objects.get(id=1).price, 100)
        self.assertEqual(Apartment.objects.get(id=1).bhk, 2)
        self.assertEqual(Apartment.objects.get(id=1).sqft, 1000)
        self.assertEqual(Apartment.objects.get(id=1).tenants, 0)
        self.assertEqual(Apartment.objects.get(id=1).photo, "default_image.png")
'''













