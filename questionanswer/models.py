from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Question(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField('more information about question', blank=True, default='')
    content_markdown = models.TextField(null=True, default='')
    # slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    votes = models.IntegerField('number of votes cast', default=0)

    def __str__(self):
        return self.title

    def save_model(self, first_time=True):
        return super(Question, self).save()

    def save(self, *args, **kwargs):
        if self.id:
            super(Question, self).save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
            QuestionVote.objects.create(question=self)
            QuestionReport.objects.create(question=self)

class Answer(models.Model):
    content = models.TextField(blank=False)
    content_markdown = models.TextField(null=True, default='')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    votes = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.content[:60]

    def save(self, *args, **kwargs):
        if self.id:
            super(Answer, self).save(*args, **kwargs)
        else:
            super(Answer, self).save(*args, **kwargs)
            AnswerVote.objects.create(answer=self)
            AnswerReport.objects.create(answer=self)

    def save_model(self, first_time=True):
        return super(Question, self).save()


class QuestionVote(models.Model):

    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    users_downvoted = models.ManyToManyField(User, related_name='downvotes', blank=True)
    users_upvoted = models.ManyToManyField(User, related_name='upvotes', blank=True)
    votes = models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        # A model should have been saved (it should have id) before accessing its
        # many-to-many fields. Below written condition will be false when object is being
        # saved for the first time. But it will run each time we update this model
        if self.id:
            updated_votes = self.users_upvoted.all().count() - \
                self.users_downvoted.all().count()
            self.votes = updated_votes

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.question} votes: {self.votes}'


class AnswerVote(models.Model):

    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    users_downvoted = models.ManyToManyField(User, related_name='answer_downvotes', blank=True)
    users_upvoted = models.ManyToManyField(User, related_name='answer_upvotes', blank=True)
    votes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):

        if self.id:
            updated_votes = self.users_upvoted.all().count() - \
                self.users_downvoted.all().count()
            self.votes = updated_votes

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.answer} votes: {self.votes}'

class Report(models.Model):
    # how many times this question has been flagged
    number_of_reports = models.IntegerField(default=0)

    # who has flagged this question
    reporter = models.ManyToManyField(User, blank=True)

    # required so that django doesn't create table for this class
    class Meta:
        abstract = True

class QuestionReport(Report):
    """ Model to store info about harmful/explicit questions """

    # which question was flagged
    question = models.OneToOneField(Question, on_delete=models.CASCADE)


class AnswerReport(Report):
    """ Model to store info about harmful/explicit answer """

    # which question was flagged
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)


#Comment : 

# class QuestionComment(models.Model):

#     content = models.CharField("Write your comment here: ", max_length=350, blank=False, null=False)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False, null=False)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
#     created_at = models.DateTimeField(default=timezone.now)

