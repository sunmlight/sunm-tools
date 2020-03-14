from django.db import models

# Create your models here.
class Note(models.Model):
    auth = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    txt = models.TextField()
    delete = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title

    @property
    def history(self):
        return NoteHistory.objects.filter(note=self, delete=False)


class NoteHistory(models.Model):
    note = models.ForeignKey('Note', on_delete=models.CASCADE)
    txt = models.TextField()
    version = models.IntegerField()
    delete = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "NoteHistory"
        verbose_name_plural = "NoteHistorys"

    def __str__(self):
        return "{}-{}".format(self.note, self.version)