from django.shortcuts import render, redirect
from .models import MessageBlock, CommentBlock
from login_and_registration.models import User

def commentWallDisplay(request):
    if not 'user_id' in request.session:
        return redirect('/')

    context = {
        "all_messages" : MessageBlock.objects.all(),
        "current_user" : User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'messageWall.html', context)

def createMessage(request):
    MessageBlock.objects.create(contained_text = request.POST['message'])
    new_message = MessageBlock.objects.last()
    new_message.user.add(User.objects.get(id = request.session['user_id']))
    return redirect('/wall')

def createComment(request):
    CommentBlock.objects.create(
        contained_text = request.POST['comment'], 
        parent_message = MessageBlock.objects.get(id = request.POST['message_id'])
        )
    new_comment = CommentBlock.objects.last() 
    new_comment.comment_users.add(User.objects.get(id = request.session['user_id']))
    return redirect('/wall')

def logout(request):
    del request.session['user_id']
    return redirect('/')
# Create your views here.
