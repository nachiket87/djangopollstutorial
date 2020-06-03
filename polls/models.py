from django.db import models
import datetime

class Question(models.Model):
    question =  models.CharField(max_length=200)
    pub_date = models.DateField('date published' , auto_now=True)

    def __str__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    # each choice is assigned a 'question' which is what ForeignKey does.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)