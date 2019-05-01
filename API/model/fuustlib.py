import json


class ArticleData:

    image_list = []
    post_number = ''
    post_datetime = ''
    content = []
    hash_tag = []

    def __init__(self, args=None):
        if args and type(args) == dict:
            self.image_list = args.get('image_list')
            self.post_number = args.get('post_number')
            self.post_datetime = args.get('post_datetime')
            self.content = args.get('content')
            self.hash_tag = args.get('hash_tag')

    def __eq__(self, other):
        return self.post_number == other.post_number

    def set_data(self, args):
        if type(args) == dict:
            self.image_list = args.get('image_list')
            self.post_number = args.get('post_number')
            self.post_datetime = args.get('post_datetime')
            self.content = args.get('content')
            self.hash_tag = args.get('hash_tag')

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        output = dict(post_number=self.post_number,
                      post_datetime=self.post_datetime,
                      image_list=self.image_list,
                      content=self.content,
                      hash_tag=self.hash_tag
                      )
        return output

