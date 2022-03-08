from django.contrib import admin
from .models import Appointment, Domain, Team, UserDetails, Planning, Bidding, Approval, Contracting, Case, Comment

# class AdminCase(admin.ModelAdmin):
#     model = Case
#     list_display = ('__all__')

# Register your models here.
admin.site.register(Appointment, list_display = ('id', 'name'))
admin.site.register(Domain, list_display = ('id', 'name'))
admin.site.register(Team, list_display = ('id', 'staffer', 'vetter', 'supporter1', 'supporter2'))
admin.site.register(UserDetails, list_display  = ('id', 'user', 'appointment', 'domain', 'team'))
admin.site.register(Planning)
admin.site.register(Bidding)
admin.site.register(Approval)
admin.site.register(Contracting)
admin.site.register(Case, list_display = ('id', 'title', 'value', 'staffer', 'current_status', 'current_step', 'current_step_user', 'current_status_due_date', 'next_step', 'next_step_user', 'planning', 'bidding', 'approval', 'contracting'))
admin.site.register(Comment, list_display = ('id', 'case', 'commenter', 'comment'))