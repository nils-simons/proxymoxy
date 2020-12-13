import os
import sys
import requests
import urllib
import json
from lxml import html
from datetime import datetime
import proxymoxy_utils as pmu

pmu.clearConsole()
pmu.setWinTitle("ProxyMoxy v0.1")
pmu.printMainWinTitle()
workdir = os.getcwd()
proxy_type = pmu.getProxyType()
pmu.clearConsole()
pmu.printMainWinTitle()
proxy_file = pmu.getProxyFileName(proxy_type)
pmu.createProxyDir()
print("Starting...")
try:
	response = requests.get("https://raw.githubusercontent.com/IchBInHanz/proxymoxy/main/proxy_site_links/proxy_site_links.json")
except:
	pmu.trowError("Server are currently down or in maintenance.")
	exit()

rj = json.dumps(response.json())
fj = json.loads(rj)
res_array = fj["links"][proxy_type]
array_length = len(res_array)
for i in range(array_length):
	if res_array[i][0] == "txt":
		file = urllib.request.urlopen(res_array[0][1])
		pmu.writeToFileAsTxt(file, proxy_file)
	else:
		if res_array[i][0] == "html":
			if res_array[i][1] == "xpath":
				full_page = requests.get(res_array[i][3])
				tree = html.fromstring(full_page.content)
				res_proxies = tree.xpath(res_array[i][2] + "/text()")
				pmu.writeToFileAsHtml(str(res_proxies[0]), proxy_file)
print("Finished!")
input('Press ENTER to Exit...')
