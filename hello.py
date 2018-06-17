def app(environ, start_resonse):
  body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
  start_resonse('200 OK', [('Content-Type', 'text/plain')])
  return body