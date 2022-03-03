from django.contrib import admin
from .models import Appointment, Domain, Team, UserDetails, Planning, Bidding, Approval, Contracting, Case, Comment

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Domain)
admin.site.register(Team)
admin.site.register(UserDetails)
admin.site.register(Planning)
admin.site.register(Bidding)
admin.site.register(Approval)
admin.site.register(Contracting)
admin.site.register(Case)
admin.site.register(Comment)