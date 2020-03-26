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
        return Note.objects.filter(
            auth=self.auth, id__in=ids, **self.base_filter
        ).update(delete=True)

    def create_one(self, obj):
        if not (self.auth or (obj.get("title") and obj.get("txt"))):
            return None
        obj.update(self.base_filter)
        if not obj.get("title"):
            obj["title"] = obj["txt"][0:20]
        if not obj.get("txt"):
            obj["txt"] = obj["title"]
        _d = Note(**obj)
        return _d.save()

    def get_note_history(self, id):
        note = Note.objects.filter(auth=self.auth, id=id, **self.base_filter)
        if note:
            return note.first().history()
        else:
            return []

    def get_tags(self, with_count=True):
        # TODO: 增加查询条件
        # Note:tag 存储方式： ","分割的字符串： Tag1,tag2
        # 返回方式： [(tag, count)]
        tags = []
        with connections["default"].cursor() as cursor:
            sql = "select unnest(string_to_array(tag, ',')) as tags, count(1) from note_note group by tags"
            cursor.execute(sql)
            if with_count:
                tags = [(r[0], r[1]) for r in cursor.fetchall()]
            else:
                tags = [r[0] for r in cursor.fetchall()]
        return tags
