import unittest
import utils.constants
from auth_factory import AuthFactory
from publisher_bot.publisher_bot import PublisherBot
from utils.memcached import Memcached as memcached


class TestPublisher(unittest.TestCase):
    """python -m unittest tests.test_publisher"""

    def __init__(self, *args, **kwargs):
        super(TestPublisher, self).__init__(*args, **kwargs)


    def setUp(self):
        self.auth = AuthFactory()
        self.publisher = PublisherBot(self.auth)


    def test_get_markets(self):
        markets = self.publisher.get_markets()
        self.assertEquals(type(markets), type([]))


    def test_load_markets(self):
        self.publisher.load_markets()
        self.assertIsNotNone(self.publisher.get_actual_market())

    def test_markets_sort(self):
        markets = [{'createdAt' : '2017-02-25T17:47:15.006939Z'}, \
                {'createdAt' : '2017-02-21T17:47:15.006939Z'}, \
                {'createdAt' : '2017-02-28T17:47:15.006939Z'}]

        sorted_markets = sorted(markets, cmp=self.publisher.sort_markets_by_createdAt)
        self.assertEquals(sorted_markets[0]['createdAt'], markets[2]['createdAt'])


if __name__=='__main__':
    unittest.main()
