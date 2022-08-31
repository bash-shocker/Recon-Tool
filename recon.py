import os
import subprocess
import urllib.request

def connect(host='http://google.com'):
	try:
		urllib.request.urlopen(host) #Python 3.x
		return True
	except:
		return False

print("Reconing Started..." if connect() else "Please check your connectivity")

def ping(url): #To check whether the host is up or down
	response = subprocess.run(["ping","-c","1", url], stdout=subprocess.DEVNULL)
	if response.returncode == 0:
		pingstatus = "Network is active"
	else:
		pingstatus = "Host Unreachable"
	print(pingstatus)
		


def recon(url):
	
	cmd1 = 'subfinder -d '+url+' -o .temp/subfinder.txt >/dev/null 2>&1'
	cmd2 = 'python3 /home/advaith/Sublist3r/sublist3r.py -d '+url+' -e baidu,yahoo,google,bing,ask,netcraft,threatcrowd,ssl,passivedns -o .temp/sublist3r.txt >/dev/null 2>&1'
	cmd3 = 'findomain -t '+url+'| sort -u | tee -a .temp/findomain.txt >/dev/null 2>&1'
	cmd4 = 'assetfinder --subs-only '+url+' | tee -a .temp/assetfinder.txt >/dev/null 2>&1'
	#cmd5 = 'amass enum -passive -d '+url+' -o .temp/amass.txt >/dev/null 2>&1'
	cmd6 = 'cat .temp/*.txt | sort -u | grep -i '+url+' | tee -a all.txt >/dev/null 2>&1'
	cmd7 = 'cat all.txt| httpx -silent -ports 80,443,3000,8080,8000,8081,8008,8888,8443,9000,9001,9090 | tee -a alive.txt >/dev/null 2>&1'
	print('Running Subfinder..')
	os.system(cmd1)
	print('Running Sublister..')
	os.system(cmd2)
	print('Running Findomain..')
	os.system(cmd3)
	print('Running assetfinder..')
	os.system(cmd4)
	#print('Running AMASS..')
	#os.system(cmd5)
	os.system(cmd6)
	print('Scanning alive subdomains')
	os.system(cmd7)
	cmd8 = 'cat alive.txt'
	print("-----------------Here are the alive subdomains for the target--------------\n\n",url)
	os.system(cmd8)
	cmd9 = 'cat alive.txt | aquatone -out /home/advaith/Desktop/Recon/aquatone/'+url+'>/dev/null 2>&1'
	print('Running Aquatone to capture the alive subdomains')
	os.system(cmd9)
	
url_in = input("Enter the URL: ")
ping(url_in)
recon(url_in)
