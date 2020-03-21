# note api for other app
# API仅供app内部调用

from .models import Note


class NoteApi:
    def __init__(self, auth=None):
        # 设置Note权限， 无权限标识仅能查看public内容
        self.auth = auth

    def get_notes(self, search=None):
        pass

    def edit_note(self, id, obj):
        pass

    def del_notes(self, ids):
        return Note.objects.filter(auth=self.auth, id__in=ids).update(delete=True)

    def create_note(self, obj):
        pass
