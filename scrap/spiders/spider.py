import scrapy


class PySpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        urls=['https://pypi.org/']


        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


        # return super().start_requests()()

    def parse(self, response):
        page=response.url.split("/")[-0]
        filename=f'pyp-{page}.html'


        with open (filename,'wb')as f:
            f.write(response.body)
        self.log(f'saved file{filename}')    


        # return super().parse(response)    