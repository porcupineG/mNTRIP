from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch
import base64

login = 'mNTRIPUser'
password = 'mNTRIPPassword'
basic_auth = base64.b64encode(login + ':' + password)

rtcm_data = {'MNTRIPSTR0': ['test0', 'test1'] }
rtcm_data_it = {'MNTRIPSTR0': 0 }

class CAS(db.Model):
    host = db.StringProperty(multiline=False)
    port = db.IntegerProperty()
    identifier = db.StringProperty(multiline=False)
    operator = db.StringProperty(multiline=False)
    nmea = db.IntegerProperty()
    country = db.StringProperty(multiline=False)
    latitude = db.FloatProperty()
    longitude = db.FloatProperty()
    fallback_host = db.StringProperty(multiline=False)
    fallback_port = db.IntegerProperty()
    misc = db.StringProperty(multiline=False)

class NET(db.Model):
    identifier = db.StringProperty(multiline=False)
    operator = db.StringProperty(multiline=False)
    authentication = db.StringProperty(multiline=False)
    fee = db.StringProperty(multiline=False)
    webnet = db.StringProperty(multiline=False)
    webstr = db.StringProperty(multiline=False)
    webreg = db.StringProperty(multiline=False)
    misc = db.StringProperty(multiline=False)

class STR(db.Model):
    mountpoint = db.StringProperty(multiline=False)
    identifier = db.StringProperty(multiline=False)
    format = db.StringProperty(multiline=False)
    format_details = db.StringProperty(multiline=False)
    carrier = db.IntegerProperty()
    nav_system = db.StringProperty(multiline=False)
    network = db.StringProperty(multiline=False)
    country = db.StringProperty(multiline=False)
    latitude = db.FloatProperty()
    longitude = db.FloatProperty()
    nmea = db.IntegerProperty()
    solution = db.IntegerProperty()
    generator = db.StringProperty(multiline=False)
    compr_encryp = db.StringProperty(multiline=False)
    authentication = db.StringProperty(multiline=False)
    fee = db.StringProperty(multiline=False)
    bitrate = db.IntegerProperty()
    misc = db.StringProperty(multiline=False)

def initCAS():
    cas = CAS().all()
    for d in cas.fetch(None):
        d.delete()
        
    d = CAS();
    d.country = 'POL'
    d.fallback_host = '0.0.0.0'
    d.fallback_port = 0
    d.host = 'mntripcaster.appspot.com'
    d.identifier = 'mNTRIPCaster/0.1'
    d.latitude = 52.21901
    d.longitude = 21.01188
    d.misc = 'none'
    d.nmea = 0
    d.operator = 'IRE PW'
    d.port = 80
    d.put()

def initNET():
    net = NET().all()
    for d in net.fetch(None):
        d.delete()
        
    d = NET();
    d.authentication = 'B'
    d.fee = 'N'
    d.identifier = 'IRE PW'
    d.misc = 'none'
    d.operator = 'IRE PW'
    d.webnet = 'mntripcaster.appspot.com'
    d.webreg = 'p.czerepaniak@gmail.com'
    d.webstr = 'none'
    d.put()
    
def initSTR():
    
    stre = STR().all()
    for d in stre.fetch(None):
        d.delete()
        
    d = STR();
    d.authentication = 'B'
    d.bitrate = 5000
    d.carrier = 1
    d.compr_encryp = 'none'
    d.country = 'POLAND'
    d.fee = 'N'
    d.format = 'RTCM 3'
    d.format_details = 'none'
    d.generator = 'mNTRIPServer'
    d.identifier = 'Warsaw'
    d.latitude = 52.21901
    d.longitude = 21.01188
    d.misc = 'none'
    d.mountpoint = 'mntripstr0'
    d.nav_system = 'GPS'
    d.network = 'IRE PW'
    d.nmea = 0
    d.solution = 0
    d.put()    

def sourctable():
    s = ""
    
    cas = CAS().all()
    for d in cas.fetch(None):
        s += 'CAS' + ';'
        s += d.host + ';'
        s += str(d.port) + ';'
        s += d.identifier + ';'
        s += d.operator + ';'
        s += str(d.nmea) + ';'
        s += d.country + ';'
        s += str(d.latitude) + ';'
        s += str(d.longitude) + ';'
        s += d.fallback_host + ';'
        s += str(d.fallback_port) + ';'
        s += d.misc
        s += '\n\r'
        
    net = NET().all()
    for d in net.fetch(None):
        s += 'NET' + ';'
        s += d.identifier + ';'
        s += d.operator + ';'
        s += d.authentication + ';'
        s += d.webnet + ';'
        s += d.webstr + ';'
        s += d.webreg + ';'
        s += d.misc 
        s += '\n\r'
    
    stre = STR().all()
    for d in stre.fetch(None):
        s += 'STR' + ';'
        s += d.mountpoint + ';'
        s += d.identifier + ';'
        s += d.format_details + ';'
        s += str(d.carrier) + ';'
        s += d.nav_system + ';'
        s += d.network + ';'
        s += d.country + ';'
        s += str(d.latitude) + ';'
        s += str(d.longitude) + ';'
        s += str(d.nmea) + ';'
        s += str(d.solution) + ';'
        s += d.generator + ';'
        s += d.compr_encryp + ';'
        s += d.authentication + ';'
        s += d.fee + ';'
        s += str(d.bitrate) + ';'
        s += d.misc
        s += '\n\r'
    
    s += 'ENDSOURCETABLE\n\r'
    
    return s


def InitSourcTable(self):
    initCAS()
    initNET()
    initSTR()

def TestMNTRIPSTR0Upload():
    urlfetch.fetch('http://mntripcaster.appspot.com/mntripstr0', 'chuj', urlfetch.POST, headers={'Ntrip-Version': 'Ntrip/2.0', 'Authorization': 'Basic ' + basic_auth})

class MNTRIPSTR0(webapp.RequestHandler):
    def post(self):
        try:
            if ((self.request.headers['Ntrip-Version'] == 'Ntrip/2.0') and (self.request.headers['Authorization'] == ('Basic ' + basic_auth))):

                self.response.headers.__delitem__('Ntrip-Version');
                self.response.headers.add_header('Ntrip-Version', 'Ntrip/2.0')
                                
                self.response.headers.__delitem__('Connection');
                self.response.headers.add_header('Connection', 'close')
                
                if (rtcm_data_it['MNTRIPSTR0'] == 0):
                    rtcm_data['MNTRIPSTR0'][1] = self.request.body
                    rtcm_data_it['MNTRIPSTR0'] = 1
                else:
                    rtcm_data['MNTRIPSTR0'][0] = self.request.body
                    rtcm_data_it['MNTRIPSTR0'] = 0
                                                            
            else:
                self.response.out.write("Ntrip protocol version not supported or unauthorized attempt.")
        except KeyError:
            self.response.out.write("Welcome to mNTRIPCaster.<BR>")
            self.response.out.write("To connect use NTRIP protocol version 2.0<BR>")
            self.response.out.write("For information contact p.czerepaniak@gmail.com<BR>")
            
    def get(self):
        try:
            if ((self.request.headers['Ntrip-Version'] == 'Ntrip/2.0') and (self.request.headers['Authorization'] == ('Basic ' + basic_auth))):

                self.response.headers.__delitem__('Ntrip-Version');
                self.response.headers.add_header('Ntrip-Version', 'Ntrip/2.0')
                
                self.response.headers.__delitem__('Cache-Control');
                self.response.headers.add_header('Cache-Control:', 'no-store, no-cache, max-age=0')
                
                self.response.headers.__delitem__('Pragma');
                self.response.headers.add_header('Pragma:', 'no-cache')
                
                self.response.headers.__delitem__('Content-Type');
                self.response.headers.add_header('Content-Type', 'gnss/data')
                
                self.response.headers.__delitem__('Connection');
                self.response.headers.add_header('Connection', 'close')
                
                self.response.out.write(rtcm_data['MNTRIPSTR0'][rtcm_data_it['MNTRIPSTR0']])    
                                        
            else:
                self.response.out.write("Ntrip protocol version not supported or unauthorized attempt.")
        except KeyError:
            self.response.out.write("Welcome to mNTRIPCaster.<BR>")
            self.response.out.write("To connect use NTRIP protocol version 2.0<BR>")
            self.response.out.write("For information contact p.czerepaniak@gmail.com<BR>")

class Caster(webapp.RequestHandler):
    
    def get(self):
        
        try:
            if (self.request.headers['Ntrip-Version'] == 'Ntrip/2.0'):
                
                self.response.headers.__delitem__('Ntrip-Version');
                self.response.headers.add_header('Ntrip-Version', 'Ntrip/2.0')
                
                self.response.headers.__delitem__('Ntrip-Flags');
                self.response.headers.add_header('Ntrip-Flags', '')
                
                self.response.headers.__delitem__('Content-Type');
                self.response.headers.add_header('Content-Type', 'gnss/sourcetable')
                
                self.response.headers.__delitem__('Connection');
                self.response.headers.add_header('Connection', 'close')
                
                self.response.out.write(sourctable())

            else:
                self.response.out.write("Ntrip protocol version not supported.")
        except KeyError:
            self.response.out.write("Welcome to mNTRIPCaster.<BR>")
            self.response.out.write("To connect use NTRIP protocol version 2.0<BR>")
            self.response.out.write("For information contact p.czerepaniak@gmail.com<BR>")
            
                                  
application = webapp.WSGIApplication([('/', Caster), ('/mntripstr0', MNTRIPSTR0)], debug=True)

def main():
        
    run_wsgi_app(application)


if __name__ == "__main__":
    main()
