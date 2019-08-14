import requests
from lxml import etree
import io
import sys

proxies = { "http": "http://142.93.130.169:8118", "https": "http://31.220.51.173:80" } 
headers={
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'accept-encoding':'gzip, deflate, sdch, br',
'cache-control':'max-age=0',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
'Referer': 'https://www.google.com.hk/',
# 'cookie':'CGIC=Ikp0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLCovKjtxPTAuOA; SID=KgeBnFcdFMfz0SwJHHVKbMa2sF-lI_I3EHJEl92RvbyOu9Tf1O7-uCH8NQDbCvaqW1d0hg.; HSID=Ah4Y1SfJfk8UzaTuU; SSID=AyFrWXkdAebwZMIt_; APISID=OqhM7NJHDR7S_GsR/AkuLK0B0biNyCToBn; SAPISID=ELp99bQZXYfWr_0h/A1ut2JjznbaN1b_xT; OGP=-19011552:; OGPC=19008563-30:19011552-2:19012637-1:; ANID=AHWqTUlae_1ExWmSL60gJWAkXGcgtmsPwncYgCN3s9Wj_vgTI1t3vKjx4VmULqNk; NID=188=mK_2AUlixZ6Pay24bGKKefAP_3unqheg9EgpIXTmJK-akWB9ToEU6fQcx_yGGSGjblNTHFmyI7V2RlgPWqdI7un1z5zjQq5_DbCQ6cUXEDAW8Pcfq6gyU9uX6CiZtqUnXN--gebTtZrXTjv4EdAs4EdpetTFp4OKZMRgePibrBO3nwdunYE0RKNWK489ZcrljcN0JWhQ-sSB9uBq_XNUDzEwHC6C0zMMsPYdELwuHvDO_GSfhatk3rpaIve6RHU4h4909EZnXd1mHaDHGQnS6AQNzR96SHvIMD-8XSPdrOzCOMVlfqh_8kOtqa74BMfRoONV1OHLXy31dA; GOOGLE_ABUSE_EXEMPTION=ID=02d9c3b54289a8a2:TM=1564175803:C=r:IP=96.63.216.227-:S=APGng0uH2mEgLV5ZCgywuqH3HFOYunCS_w; SEARCH_SAMESITE=CgQIt40B; DV=o7sorB65u5xcANEH2apbUwbB3_sCw9Zr-7HKiqBcEQEAAABujNX5PDCxRwAAAKTFK4G1nWhIEwAAAESwePdsYFXYMfETAA; 1P_JAR=2019-07-26-21'

}
# proxies=proxies
r=requests.get('https://www.google.com.hk/search?q=inurl:php?id= -site:stackoverflow.com -site:php.net intext:政府&lr=lang_zh-CN&num=5000',headers=headers,)
# print(r.headers)
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# replace(u'\ufffd',u'')
# print(r.text.encode('utf-8').decode('utf-8'))
e=etree.HTML(r.text)
# print(e.xpath('//div/node()'))
name=e.xpath('//h3[@class="LC20lb"]/node()')
url=e.xpath('//cite[@class="iUh30"]/node()')
print(name)
print(url)
filename='政府.txt'
with open(filename,'w',encoding='utf-8') as f:
	for i in url:
		f.write(i+'\n')
# print(name)
# print(url)