# swagger
from drf_yasg import openapi

#########################################################
#                                                       #
#                      Request                          #
#                                                       #
#########################################################

content_create_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='title of the content'),
        'content_type': openapi.Schema(type=openapi.TYPE_STRING, description='type of the content [pdf, video, test]'),
        'file_path': openapi.Schema(type=openapi.TYPE_FILE, description='the pdf or video file')
    },
    required=['title', 'content_type']
)


#########################################################
#                                                       #
#                      Response                         #
#                                                       #
#########################################################


content_create_respons_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_INTEGER, description='the unit id'),
        "title": openapi.Schema(type=openapi.TYPE_STRING, description='the unit title'),
        "order": openapi.Schema(type=openapi.TYPE_INTEGER, description='the unit order in the whole course perspective'),
        "state": openapi.Schema(type=openapi.TYPE_STRING, description='the unit current state'),
        "is_video": openapi.Schema(type=openapi.TYPE_BOOLEAN, description='determine weather the content is video'),
        "is_pdf": openapi.Schema(type=openapi.TYPE_BOOLEAN, description='determine weather the content is pdf'),
        "is_test": openapi.Schema(type=openapi.TYPE_BOOLEAN, description='determine weather the content is test')
    }
)

unit_retrive_list_response_body = openapi.Schema(
    type=openapi.TYPE_ARRAY,
    items=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(type=openapi.TYPE_INTEGER, description='the unit id'),
            "title": openapi.Schema(type=openapi.TYPE_STRING, description='the unit title'),
            "order": openapi.Schema(type=openapi.TYPE_INTEGER, description='the unit order in the whole course perspective'),
            "contents": openapi.Schema(
                type=openapi.TYPE_ARRAY, 
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    # TODO
                ), 
            ),
        }
    )
)
