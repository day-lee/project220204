from django.contrib import admin
from .models import WorkoutClass, Member, MemberCredit, Booking

admin.site.register(WorkoutClass)
admin.site.register(Member)
admin.site.register(MemberCredit)
admin.site.register(Booking)
