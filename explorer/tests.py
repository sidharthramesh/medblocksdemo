from django.test import TestCase
from .models import MedBlock
# Create your tests here.
class TestMedBlock(TestCase):
    def test_creation(self):
        a = MedBlock.objects.create(data="Hello there", created_by="Your Mom")
        print(a)