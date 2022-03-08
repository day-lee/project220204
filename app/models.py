from django.db import models
from django.contrib.auth.models import User


class WorkoutClass(models.Model):
    venue = models.CharField(max_length=20)
    workout_type = models.CharField(max_length=20)
    credit = models.CharField(max_length=20)
    max_num = models.CharField(max_length=20)
    date = models.DateField(auto_now=False, auto_now_add=False)
    start_time =  models.TimeField()
    end_time = models.TimeField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.venue) + ' | ' + str(self.type)


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    is_paid = models.CharField(max_length=1)

    def __str__(self):
        return self.user


class MemberCredit(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.IntegerField()
    available_days = models.CharField(max_length=20) #사용 가능 기간
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
        #return str(self.user) + '|' + str(self.id)


class Booking(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    booked_class = models.ManyToManyField(WorkoutClass)
    date_created = models.DateTimeField(auto_now_add=True)
    is_cancelled = models.CharField(max_length=1)

    def __str__(self):
        return self.user
