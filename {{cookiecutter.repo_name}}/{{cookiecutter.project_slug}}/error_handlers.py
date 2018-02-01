import json
import logging

from flask import Response, request

LOG = logging.getLogger(__name__)


def handle_validation_exception(exception):
    """
    Special case for scheming-flask validation exceptions.
    It includes a bit more info for client side debugging

    :param scheming_flask.SchemaValidationError exception:
    """
    _log_exception(exception, verbose=False)
    root_exc = exception.validation_exception
    details = {
        'cause': root_exc.message,
        'path': '.'.join(root_exc.absolute_path),
    }
    return _build_error_response(
        status_code=422,
        message="The request's schema was invalid",
        error_class='RequestValidationException',
        details=details)


def handle_generic_exception(exception):
    """
    The base exception handler for arbitrary exceptions
    Returns 500 errors with no information to avoid security issues

    :param Exception exception:
    """
    _log_exception(exception)
    return _build_error_response()


def handle_http_exception(exception):
    """
    Handle HTTPExceptions from werkzeug

    :param werkzeug.HTTPException exception:
    """
    status_code = getattr(exception, 'code', 500)
    if status_code >= 500:
        _log_exception(exception)
        resp = _build_error_response(status_code=status_code)
    else:
        _log_exception(exception, verbose=False)
        resp = _build_error_response(
            status_code=status_code,
            message=exception.description,
            error_class=exception.name)
    return resp


def _build_error_response(status_code=500, message='An Error has Occurred', error_class='ServerError', **extra):
    data = {'message': message, 'error_type': error_class}
    data.update(extra)
    return Response(json.dumps(data), status=status_code, content_type='application/json')


def _log_exception(exception, verbose=True):
    if verbose:
        LOG.exception(exception)
    LOG.error('Failing on route "%s": %s\nBody: %s', request.url, exception.name, request.get_data())
