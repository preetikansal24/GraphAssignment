import json

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view

from graph.models import Nodes, Links, GraphLinks, Graph


@api_view(['GET', 'POST'])
def graph(request):
    if request.method == 'GET':
        print "in get"
        return HttpResponse("datahdjfhdfhg")
    if request.method == 'POST':
        post_data = json.loads(request.body)
        nodes = post_data.get("nodes")
        edges = post_data.get("edges")
        graph_name = post_data.get("graphName")
        graph = Graph(name=graph_name)
        graph.save()
        for link in edges:
            graph_link = GraphLinks(graph_id=graph.id, link_id=link.get("id"))
            graph_link.save()
        response = HttpResponse(json.dumps({"key": "value", "key2": "value"}))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response


@api_view(['POST'])
def create_node(request):
    post_data = json.loads(request.body)
    node = Nodes.objects.filter(name=post_data.get("label"))
    if not node:
        node = Nodes(name=post_data.get("label"))
        node.save()
    else:
        node = node.first()
    response = HttpResponse(json.dumps({"id": node.id, "label": node.name}))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


@api_view(['POST'])
def create_edge(request):
    post_data = json.loads(request.body)
    edge = Links.objects.filter(from_node_id=post_data.get("from"), to_node_id=post_data.get("to"))
    if not edge:
        edge = Links(from_node_id=post_data.get("from"), to_node_id=post_data.get("to"))
        edge.save()
    else:
        edge = edge.first()
    response = HttpResponse(json.dumps({"id" : edge.id, "from": str(edge.from_node_id), "to": str(edge.to_node_id)}))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

