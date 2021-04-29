from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, \
    Text, ARRAY, PickleType

db = SQLAlchemy()


class Show(db.Model):
    __tablename__ = 'show'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True, nullable=False)
    host = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    bio = Column(Text, nullable=True)
    image = Column(Text, nullable=True)
    tags = Column(ARRAY(Text), nullable=True)

    def __repr__(self):
        return '<Show %r>' % self.title


class Episode(db.Model):
    __tablename__ = 'episode'
    id = Column(Integer, primary_key=True)
    show_id = Column(Integer, ForeignKey('show.id'))
    title = Column(Text, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    image = Column(Text, nullable=True)
    tracklist = Column(ARRAY(PickleType), nullable=True)
