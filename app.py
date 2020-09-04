from flask import Flask, jsonify, request, abort, make_response

from src.utils import get_artist_name_formated
from src.dynamo_controller import get_top_songs, get_info_cache
from src.redis_controller import clean_cache

app = Flask(__name__)


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error=str(e)), 404)


@app.route('/songs/<artist>', methods=['GET'])
def get_songs(artist: str):
    use_cache = request.args.get('cache', True)

    artist_name = get_artist_name_formated(artist)

    if use_cache and use_cache not in ['false', 'False']:
        response = get_info_cache(artist_name)

    else:
        clean_cache()

        try:
            response = get_top_songs(artist_name)
        except ValueError as err:
            abort(404, description=err)

    return jsonify(response)


if __name__ == '__main__':
    app.run()
