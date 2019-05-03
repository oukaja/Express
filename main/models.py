from mongoengine import *
import datetime
connect(host='mongodb://localhost:27017/kolchipress')

class Articles(Document):
    journal = StringField(max_length = 50)
    title = StringField(required=True, max_length=200)
    author = StringField(max_length = 60)
    link = StringField(max_length = 500)
    photo = StringField(max_length = 500)
    publication = DateTimeField(default=datetime.datetime.utcnow)

    @queryset_manager
    def objects(doc_cls, queryset):
        # This may actually also be done by defining a default ordering for
        # the document, but this illustrates the use of manager methods
        return queryset.order_by('-publication')

