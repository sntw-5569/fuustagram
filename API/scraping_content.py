from bs4 import BeautifulSoup
from datetime import datetime
from urllib import request
from difflib import SequenceMatcher
import re
import json

from model.fuustlib import ArticleData

fuyuka_blog_url = 'http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&ct=08'
reading_start_day = datetime(year=2019, month=2, day=21)


def get_scraping_data():
    print('-----------------')
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
    write_file([t.to_dict() for t in fuustagram_data_list])


# v---- method is local run only ----v
def write_file(data_list):
    with open('post_data.json', 'w', encoding='utf-8') as wf:
        json.dump(dict(posts=data_list), wf)


def read_json():
    with open('post_data.json', 'r', encoding='utf-8') as rf:
        read_data = json.load(rf)

    return read_data
# ^---- method is local run only ----^


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


if __name__ == "__main__":
    get_scraping_data()
