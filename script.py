import jwt
import json

secret_key = 'dev'


def token_check(environ, start_response):
    token = environ['HTTP_AUTHORIZATION']
    headers = [('Content-Type', 'application/json')]

    try:
        payload = jwt.decode(token, secret_key, algorithms='HS256')
    except jwt.exceptions.DecodeError:
        status = '401'
        body = {'code': '200', 'msg': '유효하지 않은 토큰'}
        start_response(status, headers)
        response = [json.dumps(body).encode('utf-8')]
        return response

    except jwt.exceptions.ExpiredSignatureError:
        status = '401'
        body = {'code': '201', 'msg': '만료된 토큰'}
        start_response(status, headers)
        response = [json.dumps(body).encode('utf-8')]
        return response

    headers.append(('user_id', str(payload['user_id'])))
    headers.append(('nickname', payload['nickname'].encode('utf-8').decode('iso-8859-1')))
    status = '200'
    start_response(status, headers)
    response = ['success'.encode('utf-8')]
    return response
