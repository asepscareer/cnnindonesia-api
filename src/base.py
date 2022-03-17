from lxml import html as _html
from requests import get
from src.utils import parse, headers, base_url

class GetData():

    def query(self, url):
        data = []
        try:
            page = get(url, headers= headers)
            tree = _html.fromstring(page.content)
            news = tree.xpath(".//article")
            assert len(news) > 0

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
            return data
        except Exception:
            return data

    def index(self):
        return self.query(base_url)

    def nasional(self):
        return self.query("{}/nasional".format(base_url))

    def internasional(self):
        return self.query("{}/internasional".format(base_url))

    def ekonomi(self):
        return self.query("{}/ekonomi".format(base_url))

    def olahraga(self):
        return self.query("{}/olahraga".format(base_url))

    def teknologi(self):
        return self.query("{}/teknologi".format(base_url))

    def hiburan(self):
        return self.query("{}/hiburan".format(base_url))

    def social(self):
        return self.query("{}/gaya-hidup".format(base_url))

