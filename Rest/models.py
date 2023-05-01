from django.db import models

# Create your models here.
class Student (models.Model):

    TEACHER = (
        ("ahmadi", "Ahmadi"),
        ("abdi", "Abdi"),
        ("bahrami", "Bahrami")
    )

    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    stdnum = models.IntegerField()
    teacher = models.CharField(max_length=7, choices=TEACHER)


    #Metadata
    class Meta :
        ordering = ['stdnum']

    #Methods
    # def get_absolute_url(self):
    #     return reverse('url', args=[args])

    # def __str__(self):
    #     return self.field
