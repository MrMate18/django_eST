from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name}"




class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.title} - {self.date} from {self.start_time} for {self.duration} hour(s)"






