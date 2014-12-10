#! /usr/bin/env python
# coding:utf-8

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
import os
import urllib
import covconv
import wrapper

BASEDIR = os.path.dirname(os.path.abspath(__file__))

def covconvAPI(environ, start_response):    
    method = environ.get('REQUEST_METHOD')

    if method == 'GET':
        #read html
        html_path = os.path.join(BASEDIR, 'covconv.html')
        file = open(html_path, 'r')
        html = file.read()
        file.close()
        
        #HTTP responce section
        setup_testing_defaults(environ)
        
        status = '200 OK'
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)
        
        return [html.encode('utf-8')]

    elif method == 'POST':
        # get first query
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        data = environ['wsgi.input']
        query = data.read(content_length).decode('utf-8')
        values = urllib.parse.parse_qsl(query)[0]

        #if exist key of ja_JP
        if values[0] == 'ja_JP':
            xml_success = 'true'
            kv_JP = values[1]

            #convert to kovlang
            kv_JP = covconv.covconv(kv_JP) #covconvLite engine
            kv_JP = wrapper.kovlive(kv_JP) #kovlive engine
            xml_covlang = kv_JP

        else:
            xml_success = 'false'
            xml_covlang = 'Error: input data is "null".'
        
        #make a XML
        xml = '<covconv><success>' + xml_success + '</success><covlang>' + xml_covlang + '</covlang></covconv>'

        #HTTP responce section
        setup_testing_defaults(environ)

        status = '200 OK'
        headers = [('Content-type', 'text/xml; charset="UTF-8"')]
        start_response(status, headers)

        return [xml.encode('utf-8')]

    else:
        #HTTP responce section
        setup_testing_defaults(environ)

        status = "418 I'm a teapot"
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)

        return ['covconvAPI is only accept GET or POST. another method are not acceptable. more information to "GET" this page.'.encode('utf-8')]


#test
if __name__ == '__main__':
    print('server start on port 65534')
    server = make_server('', 65534, covconvAPI)
    server.serve_forever()
