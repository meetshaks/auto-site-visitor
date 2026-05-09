import urllib.request
import datetime

# 👇 তোমার URLs এখানে যোগ করো
URLS = [
    "http://atnghs.rf.gd/ping.php",
    "https://urlvisitor.byethost9.com/",
]

def visit_url(url):
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            status = response.getcode()
            print(f"✅ [{datetime.datetime.now()}] {url} → Status: {status}")
    except Exception as e:
        print(f"❌ [{datetime.datetime.now()}] {url} → Error: {e}")

if __name__ == "__main__":
    print(f"🚀 Auto Visitor started at {datetime.datetime.now()}")
    for url in URLS:
        visit_url(url)
    print("✅ Done!")
