from app import db
from datetime import datetime
import re
def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

class Post(db.Model):
    # властивості поста
    id = db.Column(db.Integer, primary_key=True)    # номер поста
    title = db.Column(db.String(140))               # Заголовок
    slug = db.Column(db.String(140), unique=True)   # людино зрозумілий рядок url
    body = db.Column(db.Text)                       # Текст поста
    created = db.Column(db.DateTime, default=datetime.now())

    # Конструктор класа
    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slag(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)