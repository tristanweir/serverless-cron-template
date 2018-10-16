#!/usr/bin/env python
from randomizer import Randomizer

url = 'https://raw.githubusercontent.com/mozilla/http-observatory-dashboard/master/httpobsdashboard/conf/sites.json'
random_site = Randomizer(url)

class TestRandomizer():
    def test_randomizer_string(self):
        assert isinstance(random_site.next(), basestring)

    def test_randomizer_fqdn(self):
        assert "." in random_site.next()

    def test_randomizer_random(self):
        result1 = random_site.next()
        result2 = random_site.next()
        assert result1 != result2
