import uuid

import boto3
from boto3.dynamodb.conditions import Key, Attr

from src.request_manager import search_artist_id, search_top_songs

dynamo_client = boto3.resource('dynamodb').Table('Artist')


def get_top_songs(artist_name: str):
    response = dynamo_client.scan(
        FilterExpression=Attr('artist_name').eq(artist_name)
    )

    if (not response.get('Count', 0)):
        artist_id = search_artist_id(artist_name)
        songs = search_top_songs(artist_id)

        artist_info = {
            'transaction_id': str(uuid.uuid4()),
            'artist_name': artist_name,
            'artist_id': artist_id,
            'songs': songs
        }

        dynamo_client.put_item(
            Item=artist_info
        )

        return artist_info
    
    artist_info = response["Items"][0]
    artist_info['artist_id'] = int(artist_info['artist_id'])
    
    return artist_info
