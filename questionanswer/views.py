from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Answer, Question, QuestionVote, AnswerVote, QuestionReport, AnswerReport
from questionanswer.forms import AnswerCreationForm, QuestionCreationForm
# from comments.forms import QuestionCommentForm
import markdown2


# def home(request):
#     question_list = Question.objects.order_by('-created_at')[:10]

#     return render(request, 'question.html', {'question_list': question_list})


def all_questions(request):
    question_list = Question.objects.order_by('-created_at')

    paginator = Paginator(question_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'all_questions.html', {'page_obj': page_obj})


def question_details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.all()

    answer_creation_form = AnswerCreationForm()
    # question_comment_form = QuestionCommentForm()

    return render(request, 'question_details.html', {'question': question, 'answers': answers, 'answer_creation_form': answer_creation_form})


@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionCreationForm(request.POST)
        if form.is_valid():
            question_content = form.cleaned_data['content']
            content_in_html = markdown2.markdown(question_content)
            question = form.save(commit=False)
            question.asked_by = request.user
            question.content = content_in_html
            question.content_markdown = question_content

            question.save()

            return redirect(reverse('questionanswer:question_details', args=[question.id]))
    else:
        form = QuestionCreationForm()

    return render(request, 'createquestion.html', {'form': form})


@login_required
def create_answer(request, question_id):
    if request.method == 'POST':
        form = AnswerCreationForm(request.POST)

        question = get_object_or_404(Question, pk=question_id)

        if form.is_valid():
            # get content of answer in markdown sent by markdown in form
            answer_content_in_markdown = form.cleaned_data['content']

            # convert markdown to html
            answer_content_in_html = markdown2.markdown(
                answer_content_in_markdown)

            answer = form.save(commit=False)
            answer.answered_by = request.user
            answer.question = question

            # save markdown in 'content_markdown' and html in 'content' fields
            answer.content = answer_content_in_html
            answer.content_markdown = answer_content_in_markdown

            answer.save()

            return redirect(reverse('questionanswer:question_details', args=[question_id]))

    return redirect(reverse('questionaswer:question_details', args=[question_id]))


@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if question.asked_by == request.user:
        question.delete()
        messages.success(request, 'Question was successfully deleted.')
    else:
        messages.error(
            request, "You don't have permissions to delete that question")

    return redirect(reverse('questionanswer:home'))


@login_required
def delete_answer(request, question_id, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    # check only user who wrote above answer is sending request
    if answer.answered_by == request.user:
        answer.delete()
        messages.success(request, 'Answer was successfully deleted.')
        return redirect(reverse('questionanswer:question_details', args=[question_id]))
    else:
        messages.error(
            request, "You don't have permissions to delete that answer.")
        return redirect(reverse('questionanswer:home'))


@login_required
def edit_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    # check only user who wrote above question is sending request
    # if not then send unauthorized user to home route
    if request.user != question.asked_by:
        messages.error("You don't have permissions to edit this question.")
        return redirect(reverse('questionanswer:home'))

    if request.method == 'POST':
        form = QuestionCreationForm(request.POST, instance=question)
        if form.is_valid():
            question_content_in_markdown = form.cleaned_data['content']
            question = form.save(commit=False)
            question_content_in_html = markdown2.markdown(
                question_content_in_markdown)
            question.content = question_content_in_html
            question.content_markdown = question_content_in_markdown
            question.save()
            return redirect(reverse('questionanswer:question_details', args=[question_id]))

    form = QuestionCreationForm(initial={
                                'title': question.title, 'content': question.content_markdown}, instance=question)
    return render(request, 'edit_question.html', {'form': form, 'question': question})


@login_required
def edit_answer(request, question_id, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    # check only valid user is sending request
    if request.user != answer.answered_by:
        messages.error("You don't have permissions to edit this answer.")
        return redirect(reverse('questionanswer:home'))

    if request.method == 'POST':
        form = AnswerCreationForm(request.POST, instance=answer)
        if form.is_valid():
            answer_content_in_markdown = form.cleaned_data['content']
            answer = form.save(commit=False)
            answer_content_in_html = markdown2.markdown(
                answer_content_in_markdown)
            answer.content = answer_content_in_html
            answer.content_markdown = answer_content_in_markdown
            answer.save()
            return redirect(reverse('questionanswer:question_details', args=[question_id]))

    form = AnswerCreationForm(
        initial={'content': answer.content_markdown}, instance=answer)

    return render(request, 'edit_answer.html', {'form': form, 'question_id': question_id,  'answer_id': answer_id})


@login_required
def vote_question(request, question_id, action):
    try:
        question_vote = QuestionVote.objects.get(question__id=question_id)
    except QuestionVote.DoesNotExist:
        return JsonResponse({"success": False})

    upvoting_users = question_vote.users_upvoted.all()
    downvoting_users = question_vote.users_downvoted.all()

    if action == 'up':
        if request.user in upvoting_users:
            pass
        elif request.user in downvoting_users:
            question_vote.users_downvoted.remove(request.user)
            question_vote.users_upvoted.add(request.user)
        else:
            question_vote.users_upvoted.add(request.user)
    elif action == 'down':
        if request.user in upvoting_users:
            question_vote.users_upvoted.remove(request.user)
            question_vote.users_downvoted.add(request.user)
        elif request.user in downvoting_users:
            pass
        else:
            question_vote.users_downvoted.add(request.user)
    elif action == 'delete':
        if request.user in upvoting_users:
            question_vote.users_upvoted.remove(request.user)
        elif request.user in downvoting_users:
            question_vote.users_downvoted.remove(request.user)
        else:
            return JsonResponse({"success": False})

    question_vote.save()

    return JsonResponse({"success": True, "total_votes": question_vote.votes})


@login_required
def vote_answer(request, answer_id, action):
    try:
        answer_vote = AnswerVote.objects.get(answer__id=answer_id)
    except AnswerVote.DoesNotExist:
        return JsonResponse({"success": False})

    upvoting_users = answer_vote.users_upvoted.all()
    downvoting_users = answer_vote.users_downvoted.all()

    if action == 'up':
        if request.user in upvoting_users:
            pass
        elif request.user in downvoting_users:
            answer_vote.users_downvoted.remove(request.user)
            answer_vote.users_upvoted.add(request.user)
        else:
            answer_vote.users_upvoted.add(request.user)
    elif action == 'down':
        if request.user in upvoting_users:
            answer_vote.users_upvoted.remove(request.user)
            answer_vote.users_downvoted.add(request.user)
        elif request.user in downvoting_users:
            pass
        else:
            answer_vote.users_downvoted.add(request.user)
    elif action == 'delete':
        if request.user in upvoting_users:
            answer_vote.users_upvoted.remove(request.user)
        elif request.user in downvoting_users:
            answer_vote.users_downvoted.remove(request.user)
        else:
            return JsonResponse({"success": False})

    answer_vote.save()

    return JsonResponse({"success": True, "total_votes": answer_vote.votes})


@login_required
def report_question(request, question_id):
    """ This view is used to report a question that a user finds harmful/explicit """

    question_report = get_object_or_404(
        QuestionReport, question__id=question_id)

    if request.user not in question_report.reporter.all():
        question_report.reporter.add(request.user)
        question_report.number_of_reports += 1
        question_report.save()
        messages.success(
            request, "Thank you for reporting this question. Our moderation team will take a look at it and if it violates the site's guidelines it will be removed.")
    else:
        messages.error(request, "You have already reported this question.")

    return redirect(reverse('questionanswer:question_details', args=[question_id]))


@login_required
def report_answer(request, answer_id: int):
    """ This view is used to report a answer that a user finds harmful/explicit """

    answer_report = get_object_or_404(AnswerReport, answer__id=answer_id)

    if request.user not in answer_report.reporter.all():
        answer_report.reporter.add(request.user)
        answer_report.number_of_reports += 1
        answer_report.save()
        messages.success(
            request, "Thank you for reporting this answer. Our moderation team will take a look at it and if it violates the site's guidelines it will be removed.")
    else:
        messages.error(request, "You have already reported this answer.")

    return redirect(reverse('questionanswer:question_details', args=[answer_report.answer.question.id]))


    # Comment: 

# @login_required
# def create_question_comment(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     if request.method == 'POST':
#         form = QuestionCommentForm(request.POST)

#         if form.is_valid():
#             # since we are going to add question and author manually we
#             # save this form with commit=False
#             comment = form.save(commit=False)
#             comment.question = question
#             comment.author = request.user
#             comment.save()

#     return redirect(reverse('questionanswer:question_details', args=[question_id]))


# @login_required
# def delete_question_comment(request, comment_id):
#     comment = get_object_or_404(QuestionComment, id=comment_id)

#     # id of the question to which target comment belongs to so that we can
#     # use it to redirect to question_details page
#     question_id = comment.question.id

#     # only the user who wrote comment can delete it
#     if comment.author == request.user:
#         comment.delete()
#         messages.success(request, "Successfully deleted the comment.")
#     else:
#         messages.error(
#             request, "You don't have the permission to delete that comment.")

#     return redirect(reverse("questionanswer:question_details", args=[question_id]))