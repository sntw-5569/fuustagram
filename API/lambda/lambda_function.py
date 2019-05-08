import boto3
from datetime import datetime
import json
import os


def respond(err, res=None):
    return {
        'statusCode': 400 if err else 200,
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Requested-With,X-Requested-By,X-Api-Key',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Origin': 'https://kyz.fuustagram.fun',
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    if event.get('requestContext').get('httpMethod') == 'POST':
        param = event.get('queryStringParameters')
        res = post_method_handler(param)
        print(f"    POST result: {res}")
    else:
        action_type = event.get('queryStringParameters').get('Action')
        if action_type == "GetList":
            res = load_article_data()
            print(f"    GetList: Load {len(res)} article.")
        else:
            res = dict(result="what's do it?")
            print(f"    UnknowAction: request unmatch action.")

    return respond(None, res=res)


def post_method_handler(param):
    if param.get('Action') == "LikeUpdate":
        post_param = json.loads(param.get('LikeState'))
        is_incl = post_param.get('IsLiked')
        key = post_param.get('Datetime')
        nmb = post_param.get('PostNumber')
        if is_incl:
            now_count = like_increment(key, nmb)
        else:
            now_count = like_decrement(key, nmb)
        return dict(Likes=now_count, IsInclement=is_incl)
    return dict(result="post method is unknown action.")


def get_liked_count(table, key, nmb):
    likekey = 'lk#' + key
    res = table.query(KeyConditions={
            'post_datetime': {
                'AttributeValueList': [likekey],
                'ComparisonOperator': 'EQ'
            },
            'post_number': {
                'AttributeValueList': [nmb],
                'ComparisonOperator': 'EQ'
            }
        }
    )
    
    items = res.get('Items')
    if items:
        count = int(items[0].get('liked'))
    else:
        count = 0
    
    return count


def like_increment(key, nmb):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('fuustagram-article')
    
    now_likes = get_liked_count(table, key, nmb)
    set_liked = str(now_likes + 1)
    table.put_item(Item={
                'post_number': nmb,
                'post_datetime': 'lk#' + key,
                'liked': set_liked
            })
    return set_liked


def like_decrement(key, nmb):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('fuustagram-article')
    
    now_likes = get_liked_count(table, key, nmb)
    set_liked = str(max(now_likes - 1, 0))
    table.put_item(Item={
                'post_number': nmb,
                'post_datetime': 'lk#' + key,
                'liked': set_liked
            })
    return set_liked


def load_article_data():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('fuustagram-article')
    
    load_set = table.scan()
    return load_set.get('Items')

