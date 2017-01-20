# coding=utf-8
from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from bookworm.services.wordservice import word_tokenize


class BookWormThaiReaderTestCase(TestCase):
    def setUp(self):
        pass

    def test_tokenize_thais(self):
        txt = u'ทดลองระบบตัดคำไทย'
        word_tokenize(txt)
        txt = u'I don\'t like pop music'
        word_tokenize(txt)
