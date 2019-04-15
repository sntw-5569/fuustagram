from bs4 import BeautifulSoup
from datetime import datetime
from urllib import request
from difflib import SequenceMatcher
import re

from model.fuustlib import ArticleData


def get_scraping_data():
    print('-----------------')
    fuyuka_blog_url = 'http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&ct=08'
    max_read_pages = 5

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
    print([t.post_number for t in fuustagram_data_list])


def analyze_article_data(article_list):
    result_list = []
    reading_start_day = datetime(year=2019, month=2, day=21)
    is_read_end = False

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

    articles = soup.find_all('article')
    result_list = []
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
