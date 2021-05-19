from django.shortcuts import render, HttpResponse, redirect

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("Placeholder to later display all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a blog")

def create(request):
    return redirect('/')

def show(request, id):
    return HttpResponse(f"Placeholder to display blog number {id}")

def edit(request, id):
    return HttpResponse(f"Placeholder to edit blog number {id}")

def destroy(request, id):
    return redirect('/')
