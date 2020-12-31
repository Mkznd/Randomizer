from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


from core.models import Feat

# CREATE_FEAT_URL = reverse('feat:create')
LIST_ALL_FEAT_URL = reverse('feat:list')
LIST_HUMAN_FEAT_URL = reverse('feat:list', kwargs={'tags': 'Human'})


def create_sample_feat(text='sample feat', tags=None):
    if tags is None:
        tags = ['sample tag']
    return Feat.objects.create_feat(text=text, tags=tags)


class PublicFeatAPITests(TestCase):
    """Tests publicly available api requests"""

    def setUp(self) -> None:
        self.client = APIClient()

    def test_list_all_feats(self):
        """Tests listing all existing feats"""

        feat1 = create_sample_feat()
        params = {
            'text': 'sas',
            'tags': ['tag1', 'tag2']
        }
        feat2 = create_sample_feat(**params)

        response = self.client.get(LIST_ALL_FEAT_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['text'], feat1.text)
        self.assertEqual(response.data[1]['text'], feat2.text)
        self.assertEqual(response.data[0]['tags'], feat1.tags)
        self.assertEqual(response.data[1]['tags'], feat2.tags)

    def test_list_specific_feats(self):
        """Tests listing feats with specific tags"""

        feat1 = create_sample_feat()
        params = {
            'text': 'sas',
            'tags': ['Human', 'Hair Color']
        }
        feat2 = create_sample_feat(**params)
        params = {
            'text': 'sas2',
            'tags': ['Elf', 'Nose']
        }
        feat3 = create_sample_feat(**params)

        response = self.client.get(LIST_HUMAN_FEAT_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['text'], feat2.text)
        self.assertEqual(response.data[0]['tags'], feat2.tags)
