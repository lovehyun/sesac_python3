url = "서울지하철공모전.com"
print(url.encode('idna').decode())

punny = 'xn--ob0bv3xt3eeogrvbb5dh7gf4u.com'
print(punny.encode().decode('idna'))
