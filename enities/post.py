from consts.regexes import link_regex
import re


class Post:

    spam = False

    def __init__(self, text='', images=None, reply_to=None):
        if images is None:
            images = []
        self.reply_to = reply_to
        self.text = text
        self.images = images
        self.check_is_spam()

    def check_is_spam(self):
        self.spam = len(re.findall(link_regex, self.text)) > 0
        if not self.spam and self.reply_to:
            self.spam = self.reply_to.check_is_spam()
        return self.spam
