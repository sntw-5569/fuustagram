from importlib import import_module
import os
from pathlib import Path
import sys
from unittest import main, TestCase

sys.path.append(str(Path(os.path.dirname(__file__)).parents[1]))
ArticleData = import_module('model.fuustlib').ArticleData


class TestArticleData(TestCase):
    def test_no_set_article(self):
        article = ArticleData()
        self.assertEqual('', article.post_number)

    def test_set_article(self):
        contain_data = dict(post_number='100',
                            post_datetime='2016/04/06 00:46',
                            image_list=['http://cdn.keyakizaka46.com/files/14/images/common/logo.svg'],
                            content=['dummy text'],
                            hash_tag=['AAA', 'BBB', '🤟']
                            )
        article = ArticleData(contain_data)
        no_data = ArticleData()
        self.assertNotEqual(no_data, article)

    def test_output_json(self):
        contain_data = dict(post_number='100',
                            post_datetime='2016/04/06 00:46',
                            image_list=['http://cdn.keyakizaka46.com/files/14/images/common/logo.svg'],
                            content=['dummy text'],
                            hash_tag=['AAA', 'BBB', '🤟']
                            )
        article = ArticleData(contain_data)
        try:
            result = article.to_json()
        except Exception as e:
            result = None
        self.assertTrue(result, 'to_json has error.')


if __name__ == "__main__":
    main()
