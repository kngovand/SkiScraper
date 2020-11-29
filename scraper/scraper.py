import requests

# Go to Winter Park mountain stats webpage
url = "https://www.winterparkresort.com/the-mountain/mountain-report"
x = requests.get(url)

# If python requests didn't work
if(x.status_code != 200):
    print("Invalid status code")
else:
    print(x.headers)
    print(x.content)