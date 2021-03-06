from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://malami:78z433XMn@localhost/restapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

videos = {'0101': {'data': 'exists'} }

video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help= "Name of the video is required", required=True)
video_put_args.add_argument('likes', type=int, help= "Number of likes of the video", required=True)
video_put_args.add_argument('views', type=int, help= "Number of views", required=True)


def abort_if_not_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find the video")


def abort_if_exists(video_id):
    if video_id in videos:
        abort(409, message="Video with this ID already exists.")


class Video(Resource):
    def get(self, video_id):
        abort_if_not_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_not_exist(video_id)
        del videos[video_id]
        return '', 204


api.add_resource(Video, '/video/<int:video_id>')

if __name__ == '__main__':
    app.run(debug=True)