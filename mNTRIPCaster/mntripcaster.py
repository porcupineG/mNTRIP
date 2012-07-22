from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

ntrip_version = 'Ntrip/2.0'
ntrip_flags = 'st_filter,st_auth,st_match,st_strict'

class CAS(db.Model):
    host = db.StringProperty(multiline=False)
    port = db.StringProperty(multiline=False)
    identifier = db.StringProperty(multiline=False)
    operator = db.StringProperty(multiline=False)
    nmea = db.StringProperty(multiline=False)
    country = db.StringProperty(multiline=False)
    latitude = db.StringProperty(multiline=False)
    longitude = db.StringProperty(multiline=False)
    fallback_host = db.StringProperty(multiline=False)
    fallback_port = db.StringProperty(multiline=False)
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
    carrier = db.StringProperty(multiline=False)
    nav_system = db.StringProperty(multiline=False)
    network = db.StringProperty(multiline=False)
    country = db.StringProperty(multiline=False)
    latitude = db.StringProperty(multiline=False)
    longitude = db.StringProperty(multiline=False)
    nmea = db.StringProperty(multiline=False)
    solution = db.StringProperty(multiline=False)
    generator = db.StringProperty(multiline=False)
    compr_encryp = db.StringProperty(multiline=False)
    authentication = db.StringProperty(multiline=False)
    fee = db.StringProperty(multiline=False)
    bitrate = db.StringProperty(multiline=False)
    misc = db.StringProperty(multiline=False)
    

class Caster(webapp.RequestHandler):
    
    def get(self):
        
        
        try:
            if (self.request.headers['Ntrip-Version'] == ntrip_version):
                
                self.response.headers.add_header('Ntrip-Version', ntrip_version)
                self.response.headers.add_header('Ntrip-Flags', ntrip_flags)
                self.response.headers['Content-Type'] = 'gnss/sourcetable'
                
                self.response.out.write("Welcome to NTRIPCaster" + self.request.headers['Host'])
            else:
                self.response.out.write("Ntrip protocol version not supported")
        except KeyError:
            self.response.out.write("Welcome to mNTRIPCaster.\n")
            self.response.out.write("To connect use NTRIP protocol version 2.0\n")
            
                                  
application = webapp.WSGIApplication([('/.*', Caster)], debug=True)

def main():
        
    run_wsgi_app(application)


if __name__ == "__main__":
    main()
