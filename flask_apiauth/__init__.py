# -*- coding: utf-8 -*-
__author__ = 'patrickz'

from functools import wraps

from flask import _request_ctx_stack as stack, jsonify


class ApiAuth(object):
    def __init__(self, app):
        self.app = app
        self.keys = app.config.get('API_AUTH_KEYS', None)

    def auth_required(self):
        def _deco(func):
            @wraps(func)
            def _sd(*args, **kwargs):
                ctx = stack.top
                req = ctx.request
                key = req.args.get('key', None)
                if key in self.keys:
                    return func(*args, **kwargs)
                else:
                    return jsonify({'result': False, 'error': 'Not Authorized'}), 401
            return _sd
        return _deco

