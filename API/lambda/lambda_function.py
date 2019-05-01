import boto3
from bs4 import BeautifulSoup
from datetime import datetime
from urllib import request
from difflib import SequenceMatcher
import json
import os
import re

from model.fuustlib import ArticleData

fuyuka_blog_url = os.environ['fuyuka_blog_url']
reading_start_day = datetime.strptime(
    os.environ['reading_start_day'],
    '%Y-%m-%d %H:%M:%S')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    if event.get('requestContext').get('httpMethod') == 'POST':
        res = dict(result="post event.")
        print("Post event!!")
    else:
        action_type = event.get('queryStringParameters').get('Action')
        if action_type == "GetList":
            res = load_article_data()
        elif action_type == "ScrapingData":
            get_scraping_data()
            res = dict(result="Done Scraping.")
        else:
            res = dict(result="whats doing?")

    return respond(None, res=res)


def load_article_data():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('fuustagram-article')

    load_set = table.scan()
    print(load_set)
    return load_set.get('Items')


def registry_article(articles):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('fuustagram-article')

    for article in articles:
        try:
            table.put_item(Item={
                'post_number': article.post_number,
                'post_datetime': article.post_datetime,
                'image_list': article.image_list,
                'content': article.content,
                'hash_tag': article.hash_tag
            })
        except Exception as e:
            print(f"put item error: {str(e)}")


def get_scraping_data():
    print('---------scraping blog article--------')
    max_read_pages = 8

    fuustagram_data_list = []

    for page in range(max_read_pages):
        if page > 0:
            target_url = fuyuka_blog_url + f'&page={page}'
        else:
            target_url = fuyuka_blog_url
        fuusta_list = get_fuustagram_article(target_url)

        _picking_data, _is_read_end = analyze_article_data(fuusta_list)

        if _picking_data:
            fuustagram_data_list += _picking_data
        if _is_read_end:
            break
    registry_article(fuustagram_data_list)


def analyze_article_data(article_list):
    result_list = []
    is_read_end = False

    # steel prof icon
    if len(article_list) > 0 and '.jpg' in article_list[0]:
        result_list.append(
            ArticleData(
                dict(image_list=[article_list[0]],
                     post_number="0",
                     post_datetime="&profile",
                     content=[],
                     hash_tag=[])))
        article_list.remove(article_list[0])

    for article in article_list:
        if is_read_end:
            break
        # get fuustagram information
        title = re.search(r'[a-z]*.[#|＃][0-9]*',
                          article.find('h3').text).group(0)
        post_number = re.search(r'[0-9]+', title).group(0)
        img_url_list = [img.get('src') for img in article.find_all('img')]
        _time_tag = article.find('div', class_='box-bottom')
        date_time = _time_tag.find('li', class_='').text.strip()
        _post_date = datetime.strptime(date_time, '%Y/%m/%d %H:%M')
        _article_body = article.find('div', class_='box-article')
        _content_lines = _article_body.text.split('\n')
        body_rows = []
        hash_tags = []
        for row in _content_lines:
            if (row + 'avoid None')[0] in ('#', '＃'):
                hash_tags.append(row[1:])
            elif row.strip() != '':
                body_rows.append(row)
        data_set = dict(image_list=img_url_list,
                        post_number=post_number,
                        post_datetime=date_time,
                        content=body_rows,
                        hash_tag=hash_tags)
        result_list.append(ArticleData(data_set))

        is_read_end = _post_date < reading_start_day
    return result_list, is_read_end


def get_fuustagram_article(url):
    response = request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")

    result_list = []

    # get profile icon
    if "&page=" not in url:
        profile = soup.find('div', attrs={"class": "box-profile"})
        prof_icon_url = profile.find('img').get('src')
        result_list.append(prof_icon_url)

    # get article
    articles = soup.find_all('article')
    for article in articles:
        _title = re.search(r'[a-z]*.[#|＃][0-9]*', article.find('h3').text)
        if not _title:
            continue

        match_ratio = SequenceMatcher(
            None, _title.group(0).lower(), 'fuustagram').ratio()
        if match_ratio < 0.65:
            continue

        result_list.append(article)

    return result_list
