from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def question_list(request):
    questions = Question.objects.order_by('-created_at')
    return render(request, 'qa/question_list.html', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.views += 1
    question.save()
    if request.method == 'POST':
        content = request.POST.get('content')
        if content and request.user.is_authenticated:
            Answer.objects.create(
                question=question,
                content=content,
                author=request.user,
                created_at=timezone.now()
            )
            return redirect('question_detail', pk=pk)
    return render(request, 'qa/question_detail.html', {'question': question})

@login_required
def ask_question(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Question.objects.create(
                title=title,
                content=content,
                author=request.user,
                created_at=timezone.now()
            )
            return redirect('question_list')
    return render(request, 'qa/ask_question.html')

# Create your views here.
