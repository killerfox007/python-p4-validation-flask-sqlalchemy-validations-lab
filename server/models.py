from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('name')
    def validate_name(self,key,name):
        if not name:
            raise ValueError("need name")
        elif Author.query.filter_by(name=name).first():
                raise ValueError("name taken")
        return name
    @validates('phone_number')
    def validate_phone_number(self,key,phone):
        if not len(phone) == 10:
            raise ValueError
        elif not phone.isnumeric():
            raise ValueError
        return phone
    

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates('content')
    def validate_content(self,key,content):
        if not len(content) >= 250:
            raise ValueError
        return content 

    @validates('summary')
    def validate_summary(self,key,summary):
        if len(summary) > 250:
            raise ValueError
        
        return summary 
    @validates('category')
    def validate_category(self,key,category):
        if "Fiction" not in category or "Non-Fiction" not in category:
            raise ValueError
        return category
    
    @validates('title')
    def validate_title(self,key,title):
        title_check = ["Won't Believe","Secret","Top","Guess"]
        if not any([tc in title for tc in title_check]):
            raise ValueError
        return title
    
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
