#! /usr/bin/env python
# coding:utf-8

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
import os
import urllib
import covconv
import wrapper

BASEDIR = os.path.dirname(os.path.abspath(__file__))

def endpoint(environ, start_response):
    method = environ.get('REQUEST_METHOD')

    if method == 'GET':
        # get first query
        try:
            values = urllib.parse.parse_qsl(environ.get('QUERY_STRING'))[0]

        # query is missing
        except:
            #HTTP responce section
            setup_testing_defaults(environ)
            
            status = '200 OK'
            headers = [('Content-type', 'text/html')]
            start_response(status, headers)
            return [readHTML().encode('utf-8')] # return plain HTML


        #if exist key of value
        if values[0] == 'value':
            xml_success = 'true'
            xml_covlang = convert(values[1])

        else:
            xml_success = 'false'
            xml_covlang = 'Error: input data is "null".'

        
        #make a XML
        xml = buildXML(xml_success, xml_covlang)


        #HTTP responce section
        setup_testing_defaults(environ)

        status = '200 OK'
        headers = [('Content-type', 'text/xml; charset="UTF-8"')]
        start_response(status, headers)

        return [xml.encode('utf-8')]

    #other HTTP method
    else:
        #HTTP responce section
        setup_testing_defaults(environ)

        status = "418 I'm a teapot"
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)

        return ['covconvAPI is only accept "GET". another method are not acceptable. more information to "GET" this page (without args).'.encode('utf-8')]

def convert(ja_JP):
    kv_JP = ja_JP
    kv_JP = covconv.covconv(kv_JP) #covconvLite engine
    kv_JP = wrapper.kovlive(kv_JP) #kovlive engine
    return kv_JP

def readHTML():
    #read html
    html_path = os.path.join(BASEDIR, 'covconv.html')
    file = open(html_path, 'r')
    html = file.read()
    file.close()
    return html

def buildXML(xml_success, xml_covlang):
    #make a XML
    return '<?xml version="1.0" encoding="UTF-8" ?><covconv><success>' + xml_success + '</success><covlang>' + xml_covlang + '</covlang></covconv>'

#test
if __name__ == '__main__':
    print('server start on port 65534')
    server = make_server('', 65534, endpoint)
    server.serve_forever()
