from __future__ import print_function

import re

from stemming.porter2 import stem


def process_email(email_contents):
    email_contents = email_contents.lower()
    email_contents = re.sub(r'<[^<>]+>', ' ', email_contents)
    email_contents = re.sub(r'\d+', 'number', email_contents)
    email_contents = re.sub(r'(http|https)://[^\s]*', 'httpaddr', email_contents)
    email_contents = re.sub(r'[^\s]+@[^\s]+', 'emailaddr', email_contents)
    email_contents = re.sub(r'[$]+', 'dollar', email_contents)
    print('==== Processed Email ====')
    words = [stem(word) for word in re.findall(r"\w+", email_contents)]
    print(' '.join(words))
    return []


if __name__ == '__main__':
    file_contents = open('../../octave/mlclass-ex6/emailSample1.txt', 'r').read()
    word_indices = process_email(file_contents)
    print('Word indices:\n%s' % word_indices)
