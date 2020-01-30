from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poll


def polls_list(request):
    max_objects = 20
    polls = Poll.objects.all()[:max_objects]
    data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)


def polls_detail(request, pk):
    polls = get_object_or_404(Poll, pk=pk)
    data = {"results":{
        "question": Poll.question,
        "created_by": Poll.created_by.username,
        "pub_date": Poll.pub_date
    }}
    return JsonResponse(data)
