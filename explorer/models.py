from django.db import models
from random import choice, getrandbits
from string import hexdigits
from base64 import b64encode
# Create your models here.
def generate_random_hex():
    return ''.join([choice(hexdigits) for _ in range(64)])
def generate_random_base64():
    return b64encode(bytearray(getrandbits(8) for _ in range(64))).decode()

class MedBlock(models.Model):
    hash = models.CharField(max_length=64, default=generate_random_hex)
    data = models.TextField()
    signature = models.TextField(default=generate_random_base64)
    insuranceHasPermission = models.BooleanField(default=False)
    createdBy = models.CharField(max_length=400)
    file = models.FileField(null=True, blank=True, upload_to='uploads')
    type = models.TextField()

    def __str__(self):
        return "<MedBlocks {}>".format(self.hash)
# class Permission(models.Model):
#     pass        