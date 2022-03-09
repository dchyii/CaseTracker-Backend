from django.contrib import admin
from .models import Appointment, Domain, Team, UserDetails, Case, Step, Comment

# Register your models here.
admin.site.register(Appointment, list_display = ('id', 'name'))
admin.site.register(Domain, list_display = ('id', 'name'))
admin.site.register(Team, list_display = ('id', 'staffer', 'vetter', 'supporter1', 'supporter2'))
admin.site.register(UserDetails, list_display  = ('id', 'user', 'appointment', 'domain', 'team'))
admin.site.register(Case, list_display = ('id', 'title', 'value', 'folder_link', 'staffer', 'need_by_date', 'current_res_party', 'purchase_type', 'planning_deadline', 'bidding_deadline', 'approval_type', 'approval_deadline', 'contracting_type', 'contracting_deadline'))
admin.site.register(Step, list_display = ('id', 'case', 'stage', 'step', 'staffer', 'res_party', 'completed_date'))
admin.site.register(Comment, list_display = ('id', 'case', 'commenter', 'comment'))