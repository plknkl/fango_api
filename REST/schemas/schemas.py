from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from models.models import Show, Episode


class ShowSchema(SQLAlchemySchema):
    class Meta:
        model = Show
        load_instance = True

    id = auto_field()
    title = auto_field()
    host = auto_field()
    description = auto_field()
    bio = auto_field()
    image = auto_field()
    tags = auto_field()


class EpisodeSchema(SQLAlchemySchema):
    class Meta:
        model = Episode
        load_instance = True

    id = auto_field()
    show_id = auto_field()
    title = auto_field()
    description = auto_field()
    image = auto_field()
    tracklist = auto_field()
