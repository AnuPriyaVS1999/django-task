import uuid
from django.db import models


class Word(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    word = models.CharField(max_length=100)
    is_edit = models.BooleanField(default=False)
   
    def _str_(self):
        return str(self.word)


class WordMeaning(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    word = models.ForeignKey("web.Word", on_delete=models.CASCADE)
    meaning = models.TextField()
    examples = models.TextField()
    synonyms = models.TextField()
    priority = models.IntegerField(null=True)
   

    def _str_(self):
        return str(self.word)
