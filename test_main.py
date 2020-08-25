from unittest import TestCase
import main
import lxml


class Test(TestCase):
    def test_extract_url2table(self):

        wiki_sample = 'https://en.wikipedia.org/wiki/List_of_Wikipedias'
        self.assertIsNotNone(main.extract_url2table(wiki_sample))
