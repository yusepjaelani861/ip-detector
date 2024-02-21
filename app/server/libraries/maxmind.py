import geoip2.database

class MaxMind:
    def __init__(self):
        self.reader_city = geoip2.database.Reader('server/libraries/GeoLite2-City.mmdb')
        self.reader_country = geoip2.database.Reader('server/libraries/GeoLite2-Country.mmdb')
        self.reader_asn = geoip2.database.Reader('server/libraries/GeoLite2-ASN.mmdb')

    def get_location(self, ip):
        try:
            city = self.reader_city.city(ip)
            country = self.reader_country.country(ip)
            asn = self.reader_asn.asn(ip)
            return {
                "status": "success",
                "ip": ip,
                "country": (
                    country.country.names["en"]
                    if country.country.names.get("en")
                    else ""
                ),
                "countryCode": (
                    country.country.iso_code if country.country.iso_code else ""
                ),
                "region": (
                    city.subdivisions.most_specific.iso_code
                    if city.subdivisions.most_specific.iso_code
                    else ""
                ),
                "regionName": (
                    city.subdivisions.most_specific.names["en"]
                    if city.subdivisions.most_specific.names.get("en")
                    else ""
                ),
                "city": city.city.names["en"] if city.city.names.get("en") else "",
                "zip": city.postal.code if city.postal.code else "",
                "lat": city.location.latitude if city.location.latitude else "",
                "lon": (city.location.longitude if city.location.longitude else ""),
                "timezone": (
                    city.location.time_zone if city.location.time_zone else ""
                ),
                "isp": (
                    asn.autonomous_system_organization
                    if asn.autonomous_system_organization
                    else ""
                ),
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def close(self):
        self.reader_city.close()
        self.reader_country.close()
