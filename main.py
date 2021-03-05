from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

videos = {'0101': {'data': 'exists'} }


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        print(request.form)
        return request.form['likes']


api.add_resource(Video, '/video/<int:video_id>')

if __name__ == '__main__':
    app.run(debug=True)