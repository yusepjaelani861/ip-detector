import geoip2.database

class MaxMind:
    def __init__(self):
        self.reader_city = geoip2.database.Reader('server/libraries/GeoLite2-City.mmdb')
        self.reader_country = geoip2.database.Reader('server/libraries/GeoLite2-Country.mmdb')

    def get_location(self, ip):
        try:
            city = self.reader_city.city(ip)
            country = self.reader_country.country(ip)
            return {
                'status': 'success',
                'ip': ip,
                'country': country.country.names['en'],
                'countryCode': country.country.iso_code,
                'region': city.subdivisions.most_specific.iso_code,
                'regionName': city.subdivisions.most_specific.names['en'],
                'city': city.city.names['en'],
                'zip': city.postal.code if city.postal.code else "",
                'lat': city.location.latitude if city.location.latitude else "",
                'lon': city.location.longitude if city.location.longitude else "",
                'timezone': city.location.time_zone if city.location.time_zone else "",    
            }
        except:
            return {
                'status': 'not found',
                'ip': ip,
                'country': "",
                'countryCode': "",
                'region': "",
                'regionName': "",
                'city': "",
                'zip': "",
                'lat': "",
                'lon': "",
                'timezone': "",    
            }
            
    def close(self):
        self.reader_city.close()
        self.reader_country.close()
        
# Path: app/main.py