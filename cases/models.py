from tabnanny import verbose
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

    def __str__(self):
        return self.name

class Domain(models.Model):
    DOMAINS = (
        ('services', 'Services'),
        ('infocomm tech', 'Infocomm Tech'),
        ('general goods', 'General Goods')
    )
    name = models.CharField(max_length=20, choices=DOMAINS)

    def __str__(self):
        return self.name

class Team(models.Model):
    staffer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_staffer")
    vetter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_vetter", blank=True, null=True)
    supporter1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_supporter1", blank=True, null=True)
    supporter2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_supporter2", blank=True, null=True)

    def __str__(self):
        return str(self.staffer) + "'s team"

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "users details"

    def __str__(self):
        return str(self.user) + "'s details"

class Planning(models.Model):
    TYPE = (
        ('typeL', 'Type L'),
        ('typeD', 'Type D')
    )
    type = models.CharField(max_length=20, choices=TYPE)
    planned_completion_date = models.DateField(auto_now=False, auto_now_add=False)
    submitted_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    vetter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="planning_vetter", blank=True, null=True)
    vetted_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    supporter1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="planning_supporter1", blank=True, null=True)
    supported_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    supporter2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="planning_supporter2", blank=True, null=True)
    supported2_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    completion_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return "Planning ID: " + str(self.id)

class Bidding(models.Model):
    TYPE = (
        ('typeL', 'Type L'),
        ('typeD', 'Type D'),
        ('typeO', 'Type O')
    )
    type = models.CharField(max_length=20, choices=TYPE)
    planned_completion_date = models.DateField(auto_now=False, auto_now_add=False)
    submitted_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    vetter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidding_vetter", blank=True, null=True)
    vetted_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    supporter1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidding_supporter1", blank=True, null=True)
    supported_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    supporter2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidding_supporter2", blank=True, null=True)
    supported2_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    completion_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return "Bidding ID: " + str(self.id)

class Approval(models.Model):
    TYPE = (
        ('typeA', 'Type A'),
        ('typeB', 'Type B'),
        ('typeC', 'Type C')
    )
    type = models.CharField(max_length=20, choices=TYPE)
    planned_completion_date = models.DateField(auto_now=False, auto_now_add=False)
    submitted_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    vetter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="approval_vetter", blank=True, null=True)
    vetted_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    supporter1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="approval_supporter1", blank=True, null=True)
    supported_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    supporter2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="approval_supporter2", blank=True, null=True)
    supported2_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    completion_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return "Approval ID: " + str(self.id)

class Contracting(models.Model):
    TYPE = (
        ('manager', 'Manager'),
        ('deputy director', 'Deputy Director'),
        ('director', 'Director')
    )
    type = models.CharField(max_length=20, choices=TYPE)
    planned_completion_date = models.DateField(auto_now=False, auto_now_add=False)
    submitted_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    vetter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contracting_vetter", blank=True, null=True)
    vetted_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    supporter1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contracting_supporter1", blank=True, null=True)
    supported_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    supporter2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contracting_supporter2", blank=True, null=True)
    supported2_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    completion_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return "Contracting ID: " + str(self.id)

class Case(models.Model):
    STATUS = (
        ('planning', 'Planning'),
        ('bidding', 'Bidding'),
        ('approval', 'Approval'),
        ('contracting', 'Contracting'),
        ('completed', 'Completed')
    )
    STEP = (
        ('drafting', 'Drafting'),
        ('vetting', 'Vetting'),
        ('clearance1', 'Clearance 1'),
        ('clearance2', 'Clearance 2'),
        ('pending approval', 'Pending Approval'),
        ('completed', 'Completed')
    )
    title = models.CharField(max_length=50)
    value = models.PositiveIntegerField()
    folder_link = models.URLField(max_length=2000)
    staffer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="case_staffer")
    current_status = models.CharField(max_length=20, choices=STATUS)
    current_step = models.CharField(max_length=20, choices=STEP)
    current_step_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="current_step_user")
    next_step = models.CharField(max_length=20, choices=STEP, blank=True, null=True)
    next_step_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="next_step_user", blank=True, null=True)
    planning = models.ForeignKey(Planning, on_delete=models.CASCADE, blank=True, null=True)
    bidding = models.ForeignKey(Bidding, on_delete=models.CASCADE, blank=True, null=True)
    approval = models.ForeignKey(Approval, on_delete=models.CASCADE)
    contracting = models.ForeignKey(Contracting, on_delete=models.CASCADE)

    def __str__(self):
        return "Case ID: " + str(self.id)

class Comment(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return "Comment ID: " + str(self.id)