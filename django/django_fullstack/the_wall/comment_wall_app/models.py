from django.db import models

class MessageBlock(models.Model):
    contained_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField('login_and_registration.User', related_name = "message")

class CommentBlock(models.Model):
    contained_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment_users = models.ManyToManyField('login_and_registration.User', related_name = "comments")
    parent_message = models.ForeignKey(MessageBlock, related_name = "message_comments", on_delete=models.CASCADE)