from django.shortcuts import render, render_to_response, get_object_or_404


def love_page(request, pagename):
    return render_to_response(pagename)
