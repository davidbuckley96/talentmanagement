from django.shortcuts import render, redirect
from .models import Article, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from datetime import datetime


def home(request):
    articles = Article.objects.all()
    if articles:
        if len(articles) == 1:
            article_1 = Article.objects.all().order_by('-date_created')[0]
            article_2 = Article.objects.all().order_by('-date_created')[0]
        else:
            article_1 = Article.objects.all().order_by('-date_created')[0]
            article_2 = Article.objects.all().order_by('-date_created')[1]

    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Saving to the Database
        ContactForm.objects.create(
            email=email,
            message=message,
            date_sent=datetime.today()
        )

        # Sending the email
        send_mail('Hello from David Buckley',
                  f'Hey there, {email}, it worked! You are receiving this email to confirm the following message has reached us: \n"{message}". \nThanks for using my website!\n\nBest regards, \nDavid Buckley.',
                  'settings.EMAIL_HOST_USER',
                  [email],
                  fail_silently=False)
        messages.success(request, 'Email sent!')
        return redirect('home')

    if articles:
        context = {'articles': articles, 'article_1': article_1, 'article_2': article_2}
    else:
        context = {'articles': articles}
    return render(request, 'home.html', context)


def article(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'article.html', context)


def articles_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles_list.html', context)


def about(request):
    return render(request, 'about.html')


def why_us(request):
    return render(request, 'why_us.html')
