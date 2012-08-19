# -*- coding: utf-8 -*-

"""

    
    ~~~~~~~~~~~~~~

    Short description of what's contained in the file

"""
from django.core.urlresolvers import reverse
from django.test.testcases import TestCase

__docformat__ = 'restructuredtext en'


class UnauthorizedRedirectedClassTake(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('class_take',
                                                args={'0',}))

    def test_response(self):
        self.assertEquals(self.response.status_code, 302)
        self.assertIn('/accounts/signin/?next=/class/0/take',
                      self.response['location'])