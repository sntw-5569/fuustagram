from importlib import import_module
import os
from pathlib import Path
import sys
from unittest import main, TestCase

sys.path.append(str(Path(os.path.dirname(__file__)).parents[0]))
sc = import_module('scraping_content')


class TestScrapingContent(TestCase):
    def test_get_fuustagram_article(self):
        test_page = Path(os.path.dirname(__file__)) / 'store' / 'scraping.html'
        articles = sc.get_fuustagram_article(f'file://{str(test_page)}')
        print(articles)
        self.assertEqual(1, len(articles))

    def test_analyze_article_data(self):
        test_page = Path(os.path.dirname(__file__)) / 'store' / 'scraping.html'
        articles = sc.get_fuustagram_article(f'file://{str(test_page)}')
        article_data_list, is_end = sc.analyze_article_data(articles)
        self.assertFalse(is_end)
        self.assertEqual(article_data_list[0].post_number, '11')


if __name__ in '__main__':
    main()

