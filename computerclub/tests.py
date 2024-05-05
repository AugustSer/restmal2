from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Order, User
from django.contrib.auth.models import User
from .serializers import OrderSerializer


class OrdersTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(name='user')
        self.status = Order.objects.create(name='status')
        self.order1 = Order.objects.create(user=self.user,status='Open')
        self.user1 = User.objects.create_user('malkov', 'malkov@malkov.ru')

    def malkov_anonymous_user(self):
        response = self.client.get('/api/orders/', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def malkov_get_orders_list(self):
        self.client.force_login(self.user1)
        response = self.client.get('/api/orders/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        serializer = OrderSerializer(Order.objects.all(), many=True)
        self.assertListEqual(response.data, serializer.data)

    def malkov_get_order(self):
        self.client.force_login(self.user1)
        response = self.client.get(f'/api/orders/{self.order1.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = OrderSerializer(Order.objects.get(id=self.order1.id))
        self.assertDictEqual(response.data, serializer.data)



from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['orders.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def malkov_order_page(self):
        self.selenium.get(f"{self.live_server_url}/")
        elements = self.selenium.find_elements(By.XPATH, '//div')
        for element in elements:
            self.assertIn(element.text, list(map(lambda b: b.user, Order.objects.all())))
