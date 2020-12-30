from django.test import TestCase

# Create your tests here.
from django.urls import reverse

CREATE_FEAT_URL = reverse('feat:create')
LIST_FEAT_URL_HUMAN = reverse('feat:list', kwargs={'tags': ['human']})
LIST_FEAT_URL_ALL = reverse('feat:list')


class PublicFeatAPITests(TestCase):
    """Tests publicly available api requests"""

    def test_list_all_feats(self):
        """Tests listing all existing feats"""
        pass