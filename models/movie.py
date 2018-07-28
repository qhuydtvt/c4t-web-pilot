from mongoengine import Document, StringField

class Movie(Document):
  title = StringField()
  image_url = StringField()
  link = StringField()
  casts = StringField()