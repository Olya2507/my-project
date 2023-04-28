from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Myblog, Comment
from .forms import CommentForm


def myblog_index(request):
    myblogs = Myblog.objects.all()
    context = {
        'myblogs': myblogs
    }
    return render(request, 'myblog_index.html', context)


def myblog_detail(request, pk):
    myblog = Myblog.objects.get(pk=pk)
    comments = Comment.objects.filter(post=myblog)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=myblog,
            )
            comment.save()
            return redirect('/myblog')

    context = {
        'myblog': myblog,
        "comments": comments,
        "form": form
    }

    return render(request, 'myblog_detail.html', context)

