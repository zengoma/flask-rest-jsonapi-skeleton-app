from flask_rest_jsonapi.exceptions import JsonApiException


def permission_manager(view, view_args, view_kwargs):
    pass  # comment out pass and add your permission logic here, throw 403 error on fail
    # raise JsonApiException(
    #     'source',
    #     'detail',
    #     title='Permission denied',
    #     status='403')
