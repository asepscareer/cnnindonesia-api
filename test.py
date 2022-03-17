from lxml import html as _html
import requests as _requests
from src.utils import parse

_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

def query(url):
    datas = []
    try:
        page = _requests.get(url, headers=_headers)
        tree = _html.fromstring(page.content)
        news = tree.xpath(".//article")
        assert len(news) > 0

        data = []
        for i in news:
            try:
                title_ = i.xpath(".//h2[@class='title']/text()")
                
                link_ = list(i.iterlinks())[0][2]
                image_ = i.xpath(".//img/@src")
                type_ = i.xpath(".//span[@class='kanal']/text()")
                time_ = i.xpath(".//span[@class='date']/text()")
                data.append({
                    "judul": parse(title_),
                    "link": link_,
                    "gambar": parse(image_),
                    "tipe": parse(type_),
                    "waktu": parse(time_)
                    })
            except:
                pass

        datas.extend(data)
        print(datas)
        return datas
    except Exception:
        return datas

query("https://www.cnnindonesia.com/olahraga")

# def nasional(self):
#         return self.query("https://www.cnnindonesia.com/nasional")
# def internasional(self):
#         return self.query("https://www.cnnindonesia.com/internasional")