from rest_framework.response import Response


class SuccessResponse(Response):
    def __init__(self, data=None, status=None, template_name=None, headers=None,
                 exception=False, content_type=None, data_count=None):

        response = {}
        if data is not None:
            response.update({
                'data': data
            })

        if data_count is not None:
            response.update({
                'count': data_count
            })

        response.update({
            'status': 1
        })

        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        data = response
        super(SuccessResponse, self).__init__(data, status, template_name, headers, exception, content_type)