# note api for other app
# API仅供app内部调用

from .models import Note
from django.db.models import Q
from django.db import connections


class NoteApi:
    def __init__(self, data_type, auth=None):
        # 设置Note权限， 无权限标识仅能查看public内容
        self.auth = auth
        self.data_type = data_type
        self.base_filter = {
            "data_type": data_type,
            "delete": False,
        }
        if not auth:
            self.base_filter["public"] = True

    def get_notes(self, search=None):
        # search: [(key, value),(key2, value2),]
        search_dict = dict()
        if search:
            search_dict = {x[0]: x[1] for x in search}
        # 把base_filter条件放入搜索，并防止搜索条件覆盖base_filter
        search_dict.update(self.base_filter)
        if self.auth:
            rsls = Note.objects.filter(Q(auth=self.auth) | Q(public=True)).filter(
                **search_dict
            )
        else:
            rsls = Note.objects.filter(**self.base_filter)
        return rsls

    def edit_note(self, id, obj):
        pass

    def del_notes(self, ids):
        return Note.objects.filter(auth=self.auth, id__in=ids).update(delete=True)

    def create_note(self, obj):
        pass

    def get_note_history(self, id):
        pass

    def get_tags(self):
        tags = []
        with connections["default"].cursor() as cursor:
            sql = "select unnest(string_to_array(tag, ',')) as tags, count(1) from note_note group by tags"
            cursor.execute(sql)
            tags = [(r[0], r[1]) for r in cursor.fetchall()]
        return tags