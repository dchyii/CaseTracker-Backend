from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Appointment(models.Model):
    APPOINTMENTS = (
        ('staffer', 'Staffer'),
        ('manager', 'Manager'),
        ('deputy director', 'Deputy Director'),
        ('director', 'Director')
    )
    name = models.CharField(max_length=20, choices=APPOINTMENTS)

class Domain(models.Model):
    DOMAINS = (
        ('services', 'Services'),
        ('infocomm tech', 'Infocomm Tech'),
        ('general goods', 'General Goods')
    )
    name = models.CharField(max_length=20, choices=DOMAINS)

class Team(models.Model):
    staffer = models.ForeignKey(User, on_delete=models.CASCADE)
    vetter = models.ForeignKey(User, on_delete=models.CASCADE)
    supporter1 = models.ForeignKey(User, on_delete=models.CASCADE)
    supporter2 = models.ForeignKey(User, on_delete=models.CASCADE)


class UserDetails(models.Model):
    user = models.ForeignKey(User)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Planning(models.Model):
    TYPE = (
        ('typeL', 'Type L'),
        ('typeD', 'Type D')
    )
    type = models.CharField(max_length=20, choices=TYPE)
    planned_completion_date = models.DateField(auto_now=False, auto_now_add=False)
    submitted_date = models.DateField(auto_now=False, auto_now_add=False)
    vetter = models.ForeignKey(User, on_delete=models.CASCADE)
    vetted_date = models.DateField(auto_now=False, auto_now_add=False)
    supporter1 = models.ForeignKey(User, on_delete=models.CASCADE)
    supported_date = models.DateField(auto_now=False, auto_now_add=False)
    supporter2 = models.ForeignKey(User, on_delete=models.CASCADE)
    supported2_date = models.DateField(auto_now=False, auto_now_add=False)
    completion_date = models.DateField(auto_now=False, auto_now_add=False)

class Bidding(models.Model):
    TYPE = (
        ('typeL', 'Type L'),
        ('typeD', 'Type D'),
        ('typeO', 'Type O')
    )
    type = models.CharField(max_length=20, choices=TYPE)
    planned_completion_date = models.DateField(auto_now=False, auto_now_add=False)
    submitted_date = models.DateField(auto_now=False, auto_now_add=False)
    vetter = models.ForeignKey(User, on_delete=models.CASCADE)
    vetted_date = models.DateField(auto_now=False, auto_now_add=False)
    supporter1 = models.ForeignKey(User, on_delete=models.CASCADE)
    supported_date = models.DateField(auto_now=False, auto_now_add=False)
    supporter2 = models.ForeignKey(User, on_delete=models.CASCADE)
    supported2_date = models.DateField(auto_now=False, auto_now_add=False)
    completion_date = models.DateField(auto_now=False, auto_now_add=False)

class Approval(models.Model):
    TYPE = (
        ('typeA', 'Type A'),
        ('typeB', 'Type B'),
        ('typeC', 'Type C')
    )
    type = models.CharField(max_length=20, choices=TYPE)
    planned_completion_date = models.DateField(auto_now=False, auto_now_add=False)
    submitted_date = models.DateField(auto_now=False, auto_now_add=False)
    vetter = models.ForeignKey(User, on_delete=models.CASCADE)
    vetted_date = models.DateField(auto_now=False, auto_now_add=False)
    supporter1 = models.ForeignKey(User, on_delete=models.CASCADE)
    supported_date = models.DateField(auto_now=False, auto_now_add=False)
    supporter2 = models.ForeignKey(User, on_delete=models.CASCADE)
    supported2_date = models.DateField(auto_now=False, auto_now_add=False)
    completion_date = models.DateField(auto_now=False, auto_now_add=False)

class Contracting(models.Model):
    TYPE = (
        ('manager', 'Manager'),
        ('deputy director', 'Deputy Director'),
        ('director', 'Director')
    )
    type = models.CharField(max_length=20, choices=TYPE)
    planned_completion_date = models.DateField(auto_now=False, auto_now_add=False)
    submitted_date = models.DateField(auto_now=False, auto_now_add=False)
    vetter = models.ForeignKey(User, on_delete=models.CASCADE)
    vetted_date = models.DateField(auto_now=False, auto_now_add=False)
    supporter1 = models.ForeignKey(User, on_delete=models.CASCADE)
    supported_date = models.DateField(auto_now=False, auto_now_add=False)
    supporter2 = models.ForeignKey(User, on_delete=models.CASCADE)
    supported2_date = models.DateField(auto_now=False, auto_now_add=False)
    completion_date = models.DateField(auto_now=False, auto_now_add=False)

class Case(models.Model):
    STATUS = (
        ('planning', 'Planning'),
        ('bidding', 'Bidding'),
        ('approval', 'Approval'),
        ('contracting', 'Contracting')
    )
    STEP = (
        ('drafting', 'Drafting'),
        ('vetting', 'Vetting'),
        ('clearance1', 'Clearance 1'),
        ('clearance2', 'Clearance 2'),
        ('pending approval', 'Pending Approval')
    )
    title = models.CharField(max_length=50)
    value = models.PositiveIntegerField()
    staffer = models.ForeignKey(User, on_delete=models.CASCADE)
    current_status = models.CharField(max_length=20, choices=STATUS)
    current_step = models.CharField(max_length=20, choices=STEP)
    current_step_user = models.ForeignKey(User, on_delete=models.CASCADE)
    next_step = models.CharField(max_length=20, choices=STEP)
    next_step_user = models.ForeignKey(User, on_delete=models.CASCADE)
    planning = models.ForeignKey(Planning, on_delete=models.CASCADE)
    bidding = models.ForeignKey(Bidding, on_delete=models.CASCADE)
    approval = models.ForeignKey(Approval, on_delete=models.CASCADE)
    contracting = models.ForeignKey(Contracting, on_delete=models.CASCADE)

class Comment(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_created=True, auto_now=True)