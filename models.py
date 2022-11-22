"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class User(db.Model):
    __tablename__ = 'users'

    def __repr__(self):
        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} img_url={u.img_url}>"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False, unique=True)
    last_name = db.Column(db.String(20), nullable=False)
    img_url = db.Column(db.Text, default="https://e7.pngegg.com/pngimages/464/453/png-clipart-graphics-illustration-speech-bubble-blue-photography-thumbnail.png")
    post = db.relationship("Post", back_populates="user", cascade="all, delete")
        
    @property
    def fullname(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

class Post(db.Model):
    __tablename__ = 'posts'
    
    def __repr__(self) -> str:
        p = self
        return f"Post title={p.title} content={p.content} created_at={p.created_at} user={p.user.fullname}"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship('User', back_populates="post")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tags = db.relationship("Tag", secondary="posts_tags", backref="posts")
    
    @property
    def format_dt(self):
        return self.created_at.strftime("%b %d, %Y, %I:%M%p")
    
class  Tag(db.Model):
    __tablename__ = 'tags'
    def __repr__(self) -> str:
        t = self
        return f"Tag name={t.name}"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    

    
class  PostTag(db.Model):
    __tablename__ = 'posts_tags'
    def __repr__(self) -> str:
        pt = self
        return f"Tag name={pt.tag.name} Post title={pt.post.title}"
    
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    
