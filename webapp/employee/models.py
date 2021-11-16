from django.db import models

# Create your models here.

class Role(models.Model):
    charge = models.CharField(max_length=255)
    def __str__(self):
        return self.charge

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    role = models.ForeignKey(Role,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return (f"""{self.first_name} {self.last_name}""")


    def login(self,user):
        if Employee.objects.filter(username=user).exits():
            pass



    @classmethod
    def do_login(cls, username, password):
        pass


