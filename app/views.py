from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from app.models import Post


def index(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(
        request,
        "app/index.html",
        {
            "post_list": qs,
        },
    )


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)  # pk = primary key
    return render(
        request,
        "app/post_detail.html",
        {
            "post": post,
        },
    )
