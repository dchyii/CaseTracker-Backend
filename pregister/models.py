from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "users details"

    def __str__(self):
        return str(self.user) + "'s details"

class Case(models.Model):
    title = models.CharField(max_length=50)
    value = models.PositiveIntegerField()
    folder_link = models.URLField(max_length=2000)
    staffer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_staffer")
    need_by_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return "Case ID: " + str(self.id)

class Step(models.Model):
    STAGE = (
        ('planning', 'Planning'),
        ('bidding', 'Bidding'),
        ('approval', 'Approval'),
        ('contracting','Contracting')
    )

    STEP = (
        ('drafting','Drafting'),
        ('vetting','Vetting'),
        ('support1','Support1'),
        ('support2','Support2'),
        ('completed','Completed'),
        ('cancelled','Cancelled')
    )

    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="steps")
    type = models.CharField(max_length=1, blank=True, null=True)
    stage = models.CharField(max_length=20, choices=STAGE)
    step = models.CharField(max_length=20, choices=STEP)
    staffer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="staffer_steps")
    res_party = models.ForeignKey(User, on_delete=models.CASCADE, related_name="res_party_steps", blank=True, null=True)
    stage_deadline = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    completed_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return "Step ID: " + str(self.id)

class Comment(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return "Comment ID: " + str(self.id)