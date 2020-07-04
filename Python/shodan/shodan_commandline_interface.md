# shodan commandline interface

## Installation
The **shodan** command-line interface(CLI)is packaged with the officail Python library for Shodan.

To install the new tool simply execute:
```
 easy_install shodan
```
Or if you're running an older version of the Shodan Python library and want to upgrade:
```
 easy_install shodan
```
Once the tool is installed you have to initialize the environment with your API key using ** shodan init **
```
 shodan init YOUR_API_KEY
```
You can get your API keys from your Shodan account page located at:
shodan[https://account.shodan.io/login?continue=https%3A%2F%2Faccount.shodan.io%2F]
Above is original advise!

But I installed shodan use pip:
```
 pip install shodan

Installing collected packages: XlsxWriter, click, click-plugins, colorama, idna, urllib3, certifi, chardet, requests, shodan
  The script chardetect is installed in '/home/pi/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  The script shodan is installed in '/home/pi/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed XlsxWriter-1.2.9 certifi-2020.6.20 chardet-3.0.4 click-7.1.2 click-plugins-1.1.1 colorama-0.4.3 idna-2.1
```
Though install successful but Shodan was not in the path,You can create a link for shodan to the path:
```
 cd /usr/bin
 
 ln /home/pi/.local/bin/shodan
```
## Command Overview

> Before use it you should init YOUR  API

The **Shodan** CLI has a lot of commands ,the most popular/common ones are documented below.For the full list of commands just run the tool without any arguments.
```
$ shodan

Usage: shodan [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  alert       Manage the network alerts for your account
  convert     Convert the given input data file into a different format.
  count       Returns the number of results for a search
  data        Bulk data access to Shodan
  domain      View all available information for a domain
  download    Download search results and save them in a compressed JSON...
  honeyscore  Check whether the IP is a honeypot or not.
  host        View all available information for an IP address
  info        Shows general information about your account
  init        Initialize the Shodan command-line
  myip        Print your external IP address
  org         Manage your organization's access to Shodan
  parse       Extract information out of compressed JSON files.
  radar       Real-Time Map of some results as Shodan finds them.
  scan        Scan an IP/ netblock using Shodan.
  search      Search the Shodan database
  stats       Provide summary information about a search query
  stream      Stream data in real-time.
  version     Print version of this tool.

```
### count
Returns the number of results for a search query.
Example
```
$ shodan count microsofte iis 6.0
319375
```
### download
Search Shodan and download the results into a file where each line is a JSON banner.For more information on what the banner contains check out:
```
$ shodan download microsoft-data microsoft iis 6.0
Search query:                   microsoft iis 6.0
Total number of results:        319375
Query credits left:             0
Output file:                    microsoft-data.json.gz
  [###---------------------------------]   10%  00:38:48
Notice: fewer results were saved than requested
Saved 100 results into file microsoft-data.json.gz
```
### host
See information about the host such as where it's located,what ports are open and which organization owns the IP.
```
$ shodan host  104.224.138.241
104.224.138.241
Hostnames:               104.224.138.241.16clouds.com
City:                    Phoenix
Country:                 United States
Organization:            IT7 Networks
Updated:                 2020-06-29T14:09:36.442604
Number of open ports:    3

Ports:
     21/tcp
     80/tcp nginx (1.16.1)
    443/tcp nginx (1.16.1)
        |-- SSL Versions: -SSLv2, -SSLv3, -TLSv1.3, TLSv1, TLSv1.1, TLSv1.2
```
### myip
Returns your Internet-facing IP address.
```
$ shodan myip
104.224.138.241
```
### parse
Use parse to analyze a file that was generated using the download command.It lets you filter out the fields that you're intrested in,covert the JSON to a CSV and is friendly for pipe-ing to other scripts.
```
$ shodan parse --fields ip_str,port,org --separator , microsoft-data.json.gz
81.2.194.178,80,INTERNET CZ, a.s.
156.231.206.141,80,IKGUL
211.149.157.119,80,China Telecom Sichuan
81.2.194.179,80,INTERNET CZ, a.s.
83.138.8.83,80,Sternforth Ltd.
23.231.195.81,80,Take 2 Hosting
81.2.194.181,80,INTERNET CZ, a.s.
45.201.91.211,80,IKGUL
108.187.124.244,80,Leaseweb USA
82.197.185.61,80,Init7 (Switzerland) Ltd.
202.101.233.22,80,China Telecom
223.6.115.79,80,Hangzhou Alibaba Advertising Co.,Ltd.
41.76.215.61,80,Afrihost
223.6.124.16,80,Hangzhou Alibaba Advertising Co.,Ltd.
223.6.128.113,80,Hangzhou Alibaba Advertising Co.,Ltd.
47.91.202.66,80,Alibaba
45.201.115.68,80,IKGUL
125.77.194.149,80,Xiamen
200.225.93.157,8181,Uol Diveo S.A.
223.7.237.13,80,Hangzhou Alibaba Advertising Co.,Ltd.
218.189.128.156,80,HGC Global Communications Limited
```
### search

This command lets you search Shodan and view the results in a terminal-friendly way.By default it will display the IP,PORT,HOSTNAMES and data.You can use the --fields parameter to print whichever banner fields you're interested in.

```
 $ shodan search --fields ip_str,port,org,hostnames  microsoft iis 6.0
217.113.29.211  80      GNC-Alfa CJSC
150.242.182.101 80      GITN (M) Sdn. Bhd.
23.235.172.242  80      Icidc Network
103.105.58.214  80      Kuaiyun Information Technology CO.Ltd.
175.41.27.28    80      NETSEC
104.210.153.192 80      Microsoft Azure
156.229.47.233  80      IKGUL
23.245.123.243  80      Enzu    243.123-245-23.rdns.scalabledns.com
5.196.134.163   80      OVH SAS merak-waf01.proxi.technology
45.201.71.77    80      IKGUL
194.87.238.209  80      JSC Mediasoft ekspert   mail.centr-spec.ru
76.12.30.109    80      HostMySite      www297.safesecureweb.com
216.152.229.121 80      Leaseweb USA
134.73.101.128  80      Global Frag Networks
180.168.68.154  80      China Telecom Shanghai
180.97.224.38   80      China Telecom jiangsu province backbone
220.130.180.148 83      HiNet   220-130-180-148.HINET-IP.hinet.net
47.91.202.66    80      Alibaba
125.65.77.14    80      China Telecom   14.77.65.125.broad.ls.sc.dynamic.163data.com.cn
154.85.140.92   80      DXTL Tseung Kwan O Service
170.178.165.76  80      Sharktech       butter-pul.lyanalysis.net
64.19.38.46     55553   Windstream Communications       64.19.38.46.nw.nuvox.net
125.77.194.149  80      Xiamen
212.58.2.31     80      Doruk Iletisim ve Otomasyon Sanayi ve Ticaret A.S.      web33.webkontrol.doruk.net.tr
112.121.189.92  80      NETSEC
62.48.169.158   80      MEO
59.124.104.52   80      HiNet   59-124-104-52.HINET-IP.hinet.net
```
### Getting a List of Top Website Hackers

```
$ shodan download --limit -1 hacked 'title:"hacked by"'
```
XxUsmQjmSzJDDHVd4W2vedZTAIHCZpDN































