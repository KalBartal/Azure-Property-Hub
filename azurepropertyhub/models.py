from django.db import models
from django.contrib.auth import get_user_model
from properties.models import Property


User = get_user_model()


class Message(models.Model):

    class Meta:
        app_label = 'azurepropertyhub'

    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_messages')
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.recipient}: {self.subject}'
