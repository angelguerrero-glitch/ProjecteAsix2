from shodan import Shodan

api = Shodan('oelxCyCDvzlcHmi3TVVVvMKznkwWQMoc')

# Lookup an IP
ipinfo = api.scan_internet('20','ftp')
print(ipinfo)
