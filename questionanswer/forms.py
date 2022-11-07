from django.forms.models import ModelForm

from questionanswer.models import Question
from questionanswer.models import Answer


class QuestionCreationForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('asked_by', 'created_at', 'votes', 'content_markdown')


class AnswerCreationForm(ModelForm):
    class Meta:
        model = Answer
        exclude = ('question', 'answered_by', 'created_at',
                   'votes', 'content_markdown')


#Comment :

# class QuestionCommentForm(ModelForm):

#     class Meta:
#         model = QuestionComment
#         exclude = ('question', 'author', 'created_at')