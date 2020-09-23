import pyquery, os, sys, validators, subprocess

def main():
	add_to_client(confirm_magnets(get_url()))

#Gets valid url from user
def get_url():
	url = input("\nCopy and paste a url to scrape magnets from: ").strip()
	while validators.url(url) != True:
		url = input("\nInvalid url. Please enter a valid url i.e. \"https://google.com\": ").strip()
	return url

#Confirms that the provided url contains magnets and appends to confirmed magnet list
def confirm_magnets(url):
	pq = pyquery.PyQuery(url)
	confirmed = list()
	for a in pq.find('a'):
		href = a.get('href')
		if href and (href.startswith("magnet")):
			confirmed.append(href)
	if confirmed == []:
		quit("\nNo magnets found. Exiting...")
	return confirmed

#Adds magnet links to system's default torrent client
def add_to_client(magnets):
	for i in magnets:
		if sys.platform.startswith('linux'): #Linux
			os.system("xdg-open " + i)
		elif sys.platform.startswith('win32'): #Windows
			os.startfile(i)

main()
