from django.db import models

class University(models.Model):
    name = models.CharField(max_length=100)
    # Add any additional fields specific to the university

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    # Add any additional fields specific to the department

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    # Add any additional fields specific to the city

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    full_name_arabic = models.CharField(max_length=100)
    full_name_english = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    agree_to_terms = models.BooleanField()

    def __str__(self):
        return self.full_name_english
