from flask import Flask, jsonify, request, abort

from src.utils import get_artist_name
from src.dynamo_controller import get_top_songs

app = Flask(__name__)

'''
TODO: [] Tratar os retornos da api, retornando erro 404 ou 400
      [] Salvar informaçoes novas no redis (por 7 dias)
      [] Buscar informações pelo redis
      [] Caso "cache" falso, limpar os dados do redis, e realizar busca no banco
'''

@app.route('/songs/<artist>', methods=['GET'])
def get_songs(artist: str):
    use_cache = request.args.get('cache', True)

    artist_name = get_artist_name(artist)

    response = get_top_songs(artist_name)

    return jsonify(response)

if __name__ == '__main__':
    app.run()