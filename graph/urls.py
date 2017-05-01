from django.conf.urls import url
import views as graph_view

urlpatterns = [
    # taxes
    url(r'^graph/?$', graph_view.graph),
    url(r'^node/?$', graph_view.create_node),
    url(r'^edge/?$', graph_view.create_edge)
]
