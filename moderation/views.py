from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

from questionanswer.models import QuestionReport


def is_moderator(user):
    """This method is used to create a decorator that gives access to a view only
        if the user belongs to the group 'moderators'.
    """
    if user.groups.filter(name='moderators').exists():
        return True
    else:
        raise PermissionDenied()


@login_required
@user_passes_test(is_moderator)
def moderation_home(request):
    return render(request, 'moderation_home.html')


@login_required
@user_passes_test(is_moderator)
def reported_questions(request):
    reported_question_list = QuestionReport.objects.filter(
        number_of_reports__gt=0)

    return render(request, 'reported_questions.html', {'reported_question_list': reported_question_list})