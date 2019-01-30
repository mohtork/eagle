from datetime import datetime
import requests
import OpenSSL
import ssl, socket


def url_uptime(url):
	url = requests.get(url)
	return url.status_code
	


def ssl_check(domain):
	cert=ssl.get_server_certificate((domain, 443))
	x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
	expireDate=datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
	return expireDate



