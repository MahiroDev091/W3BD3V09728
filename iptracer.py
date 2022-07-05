import sys
import httpx
import colorama


class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET

class IPTracer:
	def __init__(self, ip):
		self.ip = ip

	@property
	def resp_url(self):
		try:
			resp = httpx.get(f"http://ip-api.com/json/{self.ip}?fields=status,reverse,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy,query,asname").json()

			info = Color.LG+"    [+] Target IP: " + resp['query'] + "\n" +Color.LG+ "    [+] Country: " + resp['continent'] + " " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['region'] + " " + "(" + resp['regionName'] + ")" + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] Zipcode: " + resp['zip'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone'] + "\n\n" +Color.LG+ "    [+] ISP: " + resp['isp'] + "\n" +Color.LG+ "    [+] ASN: " + resp['as'] + " " + resp['asname'] + "\n\n" +Color.LG+ "    [+] Mobile: " + str(resp['mobile']) + "\n" +Color.LG+ "    [+] VPN: " + str(resp['proxy'])+ "\n\n" +Color.LG+ "    [+] Google Map: https://www.google.com/maps/place/" + str(resp['lat']) + "," + str(resp['lon'])

			if resp['reverse'] == '':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
			else:
				return info

		except KeyError:
			return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
		except httpx.ConnectError:
			return Color.LR+"Error: Check your Internet Connection."

def main():
	print(Color.LB+"	Simple IPTracer Made By PanthX")
	while True:
		sys.stdout.write(Color.LC+"\n╔═══[ Your Target IP ]\n╚══> ");ip = input()	
		print(IPTracer(ip).resp_url)

if __name__ == "__main__":
	main()