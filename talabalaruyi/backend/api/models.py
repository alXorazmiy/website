from django.db import models

class Floor(models.Model):
    number = models.SmallIntegerField()
    empty_place = models.IntegerField()
    busy_place = models.IntegerField()


    def __str__(self) -> str:
        return f"{self.number}- qavat"



class Room(models.Model):
    number = models.SmallIntegerField()
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, verbose_name='floor')
    place = models.SmallIntegerField()
    beds = models.JSONField(default={})


    def __str__(self) -> str:
        return f"{self.number}- xona {self.floor}"
    


class Faculty(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.CharField(max_length=200, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name='faculty')
    course = models.SmallIntegerField()
    in_time = models.DateTimeField(auto_now_add=False)
    out_time = models.DateTimeField(blank=True, null= True)
    floor = models.SmallIntegerField()
    room = models.SmallIntegerField()
    bed = models.SmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.last_name}  {self.first_name}"
    

class Image(models.Model):
    image = models.ImageField( upload_to='students/')



class Payments(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='student')
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default=0)

