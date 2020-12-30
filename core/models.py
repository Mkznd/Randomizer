from django.db import models


# Create your models here.

class FeatManager(models.Manager):
    """Manages creation of feats"""

    def create_feat(self, text: str, tags: list):
        """Creates a feat with text and tags"""
        if type(tags) == str:
            raise ValueError("Tags must be provided in a form of a list, not a string")

        if not text:
            raise ValueError("Feat must have a text")

        if not tags:
            raise ValueError("Feats must have a set of tags")

        tags = ','.join(sorted(set(tags)))
        feat = self.model(text=text, tags=tags)

        feat.save(using=self._db)

        return feat


class Feat(models.Model):
    """Representation of any feat in the db, has text and tags"""

    text = models.CharField(max_length=255)

    tags = models.TextField()

    objects = FeatManager()
