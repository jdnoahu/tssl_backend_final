from src.common import db, ma


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    category = db.Column(db.String(100), unique=False)
    creation_date = db.Column(db.String(100), unique=False)
    featured_image = db.Column(db.String(100), unique=False)
    content = db.Column(db.Text(), unique=False)
    tags = db.Column(db.String(144), unique=False)

    def __init__(self, title, category, creation_date, featured_image, content, tags):
        self.title = title
        self.category = category
        self.creation_date = creation_date
        self.featured_image = featured_image
        self.content = content
        self.tags = tags


class BlogSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'category', 'creation_date',
                  'featured_image', 'content', 'tags')
