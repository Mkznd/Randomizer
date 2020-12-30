from django.test import TestCase

# Create your tests here.
from core.models import Feat


class ModelTests(TestCase):
    """Tests for models"""

    def test_create_feat(self):
        """Tests if feat is created successfully"""

        params = {
            'text': 'sas',
            'tags': ['human', 'name']
        }

        feat = Feat.objects.create_feat(**params)

        exists = Feat.objects.filter().exists()

        self.assertTrue(exists)
        self.assertEqual('human,name', feat.tags)

    def test_create_feat_with_str_fails(self):
        """Tests if creating a feat with a string for tags fails"""

        params = {
            'text': 'sas',
            'tags': 'human name'
        }

        with self.assertRaises(ValueError):
            feat = Feat.objects.create_feat(**params)

    def test_create_feat_blank_name_fails(self):
        """Tests if creating a feat with blank text fails"""

        params = {
            'text': '',
            'tags': ['human', 'name']
        }

        with self.assertRaises(ValueError):
            feat = Feat.objects.create_feat(**params)

    def test_create_feat_blank_tags_fails(self):
        """Tests if creating a feat with blank text fails"""

        params = {
            'text': 'sas',
            'tags': []
        }

        with self.assertRaises(ValueError):
            feat = Feat.objects.create_feat(**params)
