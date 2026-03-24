from django.shortcuts import render
from.models import Hashtag

from django.http import JsonResponse

def hashtag_posts_view(request, tag):
    Hashtag = Hashtag.objects.filter(name=tag).first()

    if not Hashtag:
        post = []

    else:
        posts = Hashtag.posts.select_related("user").prefetch_related("images")


    return render(request,"hashtags/hashtag_feed.html",{
        "hashtag": tag,
        "posts": posts
    })


def hashtag_suggestions(request):

    q = request.GET.get("q","")

    tags = Hashtag.onjects.filter(name__icontains=q)[:10]

    data = [{"name": tag.name} for tag in tags]

    return JsonResponse(data, safe=False)


    