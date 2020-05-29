
from .. import db
import datetime


class Todo(db.Model):
    """ Todo Model """
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=False, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    completion_status = db.Column(db.Boolean, nullable=False, default=False)
    due_date = db.Column(db.DateTime, nullable=False)
    completion_date = db.Column(db.DateTime, nullable=False)
    file_url = db.Column(db.String(255), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return "<Todo '{}'>".format(self.title)
