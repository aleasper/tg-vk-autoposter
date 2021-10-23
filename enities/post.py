class Post:

    def __init__(self, text='', images=None):
        if images is None:
            images = []
        self.text = text
        self.images = images
