from django.db import models


# Create your models here.
from graph.models.abstract_model import Trackers


class Nodes(Trackers):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=False, default="", max_length=200, unique=True)

    @classmethod
    def create(cls, label):
        node = cls(name=label)
        # do something with the book
        return node


class Links(Trackers):
    id = models.AutoField(primary_key=True)
    from_node = models.ForeignKey(Nodes, blank=False, null=False, related_name="from_node")
    to_node = models.ForeignKey(Nodes, blank=False, null=False, related_name="to_node")
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('from_node', 'to_node')


class Graph(Trackers):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=False, default="", max_length=200)


class GraphLinks(Trackers):
    id = models.AutoField(primary_key=True)
    graph = models.ForeignKey(Graph, null=False, blank=False)
    link = models.ForeignKey(Links, null=False, blank=False)

    class Meta:
        unique_together = ('graph', 'link')
