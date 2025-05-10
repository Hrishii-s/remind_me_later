from django.db import models

class Reminder(models.Model):
    reminder_method_choices=[
        ('email','Email'),
        ('sms','SMS')
    ]
    message=models.TextField()
    reminder_time=models.DateTimeField()
    reminder_method=models.CharField(max_length=10,choices=reminder_method_choices)

    def __str__(self):
        return f"{self.message} sent at {self.reminder_time} by {self.reminder_method}"