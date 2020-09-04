from flask import Flask, jsonify, request, abort, make_response

from src.utils import get_artist_name
from src.dynamo_controller import get_top_songs

app = Flask(__name__)

'''
TODO: [X] Tratar os retornos da api, retornando erro 404 ou 400
      [] Salvar informaçoes novas no redis (por 7 dias)
      [] Buscar informações pelo redis
      [] Caso "cache" falso, limpar os dados do redis, e realizar busca no banco
'''


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error=str(e)), 404)


@app.route('/songs/<artist>', methods=['GET'])
def get_songs(artist: str):
    use_cache = request.args.get('cache', True)

    artist_name = get_artist_name(artist)

    try:
        response = get_top_songs(artist_name)
    except ValueError as err:
        abort(404, description=err)

    return jsonify(response)


if __name__ == '__main__':
    app.run()
