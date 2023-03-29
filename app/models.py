from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) 
    # question의 id컬럼과 연결된다는 의미.
    # ondelete='CASCADE' >> 질문을 삭제하면 해당 질문에 달린 답변도 함께 삭제
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    # relationship : 참조할 모델명이다.
    # backref : 역참조 설정. 질문에 달린 답들을 참조할 수 있다.
    content = db.Column(db.Text(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)