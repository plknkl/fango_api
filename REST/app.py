import os
import json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models.models import Show, Episode
from models.models import db
from schemas.schemas import ShowSchema, EpisodeSchema

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.create_all()
    db.session.commit()

show_schema = ShowSchema()
episode_schema = EpisodeSchema()


def load_dummy_on_db():
    # Load dummy data ---------
    with open('dummy_data/shows.json') as f:
        shows = json.load(f)
    with open('dummy_data/episodes.json') as f:
        episodes = json.load(f)
    # -------------------------
    for show in shows:
        show = show_schema.load(show, session=db.session)
        db.session.add(show)
    for episode in episodes:
        episode = episode_schema.load(episode, session=db.session)
        db.session.add(episode)

    db.session.commit()


# Routes
@app.route('/reset', methods=['POST'])
def reset():
    if request.method == 'POST':
        r = request.json
        if 'password' in r.keys():
            if r['password'] == 'fangopass':
                with app.app_context():
                    db.drop_all()
                    db.create_all()
                    db.session.commit()
            else:
                return pass_needed()
        else:
            return pass_needed()

        return {'result': 'all clear'}, 200


@app.route('/load-dummy', methods=['POST'])
def load_dummy():
    if request.method == 'POST':
        r = request.json
        if 'password' in r.keys():
            if r['password'] == 'fangopass':
                with app.app_context():
                    db.drop_all()
                    db.create_all()
                    db.session.commit()

                    # with app.app_context():
                    load_dummy_on_db()

            else:
                return pass_needed()
        else:
            return pass_needed()

        return {'result': 'dummy loaded'}, 200


# SHOWS
@app.route('/shows', methods=['GET'])
def get_shows():
    shows = Show.query.all()
    return jsonify([show_schema.dump(x) for x in shows])


@app.route('/shows', methods=['POST'])
def add_show():
    r = request.json
    errors = show_schema.validate(r, session=db.session)
    if errors:
        return errors, 400

    show = show_schema.load(r, session=db.session)

    with app.app_context():
        db.session.add(show)
        db.session.commit()
    return request.json


@app.route('/shows/<show_id>', methods=['DELETE'])
def delete_show(show_id):
    show = Show.query.filter(Show.id == show_id)
    if show.scalar() is None:
        return {'result': 'show not found'}, 404

    # delete every episode
    episodes = Episode.query.filter(show_id == show_id).all()
    for episode in episodes:
        db.session.delete(episode)

    show.delete()
    db.session.commit()
    return {'result': f'{show_id} deleted'}, 200


@app.route('/shows/<show_id>')
def get_show(show_id):
    show = Show.query.get(show_id)
    return jsonify(show_schema.dump(show))
    

# EPISODES
@app.route('/shows/<show_id>/episodes', methods=['GET'])
def get_episodes(show_id):
    show = Show.query.get(show_id)
    if show:
        episodes = Episode.query.filter(Episode.show_id == show_id)
        return jsonify([episode_schema.dump(x) for x in episodes])
    return {}


@app.route('/episodes', methods=['POST'])
def add_episode():
    r = request.json
    errors = episode_schema.validate(r, session=db.session)
    if errors:
        return errors, 400

    episode = episode_schema.load(r, session=db.session)

    with app.app_context():
        db.session.add(episode)
        db.session.commit()
    return request.json


@app.route('/episodes/<id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.filter(Episode.id == id)
    if episode.scalar() is None:
        return {'result': 'episode not found'}, 404
    else:
        episode.delete()
    db.session.commit()
    return {'result': f'{id} deleted'}, 200
