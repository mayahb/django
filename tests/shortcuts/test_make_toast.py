from django.shortcuts import make_toast
from django.test import SimpleTestCase


class MakeToastTests(SimpleTestCase):
    def test_make_toast(self):
        print("here we test if we can make toast")
        self.assertEqual(make_toast(), "toast")