import urllib
import urllib2
import hashlib
import mimetypes
import requests

class odm (object):
    """
    login
    """
    def __init__(self, usr, passwd, uri = 'https://thusznet.tk'):
        self.usr = usr
        self.passwd = passwd
        self.uri = uri 
        self.cookie = 'hehexxxxheheh'

    def login(self):
        values = {'frmuser' : self.usr,
            'frmpass' : self.passwd,
            'login' : 'Enter'}
        headers = {'Accept-Encoding' : 'gzip,deflate',
                'Cookie' : 'PHPSESSID=' + self.cookie}
        data = urllib.urlencode(values)
        req = urllib2.Request(self.uri + '/index.php', data, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        #print the_page

    def logout(self):
        headers = {'Accept-Encoding' : 'gzip,deflate',
                'Cookie' : 'PHPSESSID=' + self.cookie}
        req = urllib2.Request(self.uri + '/logout.php', None, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        #print the_page

    def add(self, filename, description, comment=''):
        boundary = '---------------------------19218239114643244121791888480'
        headers = {'Accept-Encoding' : 'gzip,deflate',
                'Cookie' : 'PHPSESSID=' + self.cookie,
                'Content-Type' : 'multipart/form-data; boundary=' + boundary,
                'Referer' : self.uri + '/add.php'}
        #datal = 'Content-Type: multipart/form-data; boundary='+boundary + '\r\n'
        datal = '' + 'Content-Length: '
        datah = '--' + boundary + '\r\n' + '\r\n'
        datah = datah + 'Content-Disposition: form-data; name="i_value"' + '\r\n\r\n' + '0' + '\r\n'
        datah = datah + '--' + boundary + '\r\n'
        datah = datah + 'Content-Disposition: form-data; name="file[]"; filename="%s"' % filename + '\r\n'
        #datah = datah + '--' + boundary + '\r\n'
        filetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        datah = datah + 'Content-type: %s' % filetype + '\r\n' + '\r\n'
        #datah = datah + '--' + boundary + '\r\n'
        with open(filename, 'rb') as f:
            datah = datah + f.read() + '\r\n'
        datah = datah + '--' + boundary + '\r\n'
        namelst = ['file_owner' , 'file_department' , 'category',
            'department_permission[1]' , 'user_permission[1]' ,
            'description' , 'comment', 'submit']
        vallst = ['1' , '1' , '3', '1', '4', description , comment, 'Add Document']
        it = 0
        for name in namelst:
            datah = datah + '--' + boundary + '\r\n'
            datah = datah + 'Content-Disposition: form-data; name="%s"' % name + '\r\n' + '\r\n'
            datah = datah + vallst[it] + '\r\n'
            #datah = datah + '--' + boundary +  '\r\n'
            it = it + 1
        datah = datah + '--' + boundary + '--' +  '\r\n'
        datal = datal + str(len(datah)) + '\r\n'
        data = datal + datah
        req = urllib2.Request(self.uri + '/add.php', data, headers)
        response = urllib2.urlopen(req)
        retid = response.info().dict['refer']
        return retid
    def publish(self, fid):
        values1 = {'checkbox[]' : fid,
            'submit': 'commentAuthorize',
            'mode': '',
            'Docflag' : '-1'}
        values = {'to' : 'Author(s)',
            'subject' : '',
            'comments' : '',
            'checkbox' : fid ,
            'send_to_users[]' : 'owner',
            'submit' : 'Authorize'}
        headers = {'Accept-Encoding' : 'gzip,deflate',
                'Cookie' : 'PHPSESSID=' + self.cookie}
        data1 = urllib.urlencode(values1)
        req1 = urllib2.Request(self.uri + '/toBePublished.php', data1, headers)
        response1 = urllib2.urlopen(req1)
        data = urllib.urlencode(values)
        req = urllib2.Request(self.uri + '/toBePublished.php', data, headers)
        response = urllib2.urlopen(req)
        #print the_page

