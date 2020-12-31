from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

from core.models import Feat
from feat import serializers


class FeatListView(generics.ListAPIView):
    """Lists all feats and does search for feats"""

    serializer_class = serializers.FeatSerializer
    queryset = Feat.objects.all()

    def get_queryset(self):
        """Gets specific feats which have certain tags"""

        tags_ = self.kwargs['tags'].split(',')
        feats = Feat.objects.all()
        for tag in tags_:
            feats = feats.filter(tags__icontains='human')

        return feats
