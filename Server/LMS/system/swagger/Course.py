# swagger
from drf_yasg import openapi

#########################################################
#                                                       #
#                      Request                          #
#                                                       #
#########################################################

course_create_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the course'),
        'pref_description': openapi.Schema(type=openapi.TYPE_STRING, description='pref Description of the course'),
    },
    required=['name', 'pref_description']
)

course_publish_approve_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
)

#########################################################
#                                                       #
#                      Response                         #
#                                                       #
#########################################################


course_list_response_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='course id'),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the course'),
        'image': openapi.Schema(type=openapi.TYPE_FILE, description='image of the course'),
    },
)

course_retrive_response_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Course ID'),
        'company': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Company name'),
                'logo': openapi.Schema(type=openapi.TYPE_STRING, description='Company logo', nullable=True),
            },
        ),
        'admin_contract': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Admin contract ID'),
                'admin': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Admin ID'),
                        'user': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
                                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                            },
                        ),
                    },
                ),
                'joining_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Joining date', nullable=True),
                'company': openapi.Schema(type=openapi.TYPE_INTEGER, description='Company ID'),
            },
        ),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Course name'),
        'image': openapi.Schema(type=openapi.TYPE_STRING, description='Course image', nullable=True),
        'pref_description': openapi.Schema(type=openapi.TYPE_STRING, description='Course description'),
        'trainers': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Trainer ID'),
                    'trainer_contract': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Trainer contract ID'),
                            'trainer': openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Trainer ID'),
                                    'user': openapi.Schema(
                                        type=openapi.TYPE_OBJECT,
                                        properties={
                                            'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
                                            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                                        },
                                    ),
                                },
                            ),
                        },
                    ),
                },
            ),
        ),
        'units': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Unit ID'),
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Unit title'),
                'order': openapi.Schema(type=openapi.TYPE_INTEGER, description='Unit order'),
                'creation_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Creation date'),
                'contents': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT), description='Unit contents'),
            },
        ),
    },
)

course_delete_response_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Response message'),
    },
    example={
        'message': 'Course deleted'
    }
)

'''
    TODO:
    this swagger
'''

course_retrive_info_response_body = openapi.Schema(
    description='for presenting a specific course info page which present the whole information about the course and the additional resources',
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='course id'),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the course'),
        'pref_description': openapi.Schema(type=openapi.TYPE_STRING, description='pref Description of the course'),
        'image': openapi.Schema(type=openapi.TYPE_FILE, description='image of the course'),
        'company': openapi.Schema(type=openapi.TYPE_OBJECT, description='the company which have this course'),

    },
)