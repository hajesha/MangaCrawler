import scrapy

class MangaCrawler(scrapy.Spider):
    name = "mangacrawler"
    def start_requests(self):

        url = 'https://mangadex.org/titles'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for manga in response.css('div.manga-entry'):
            dictionary = {
                'title': manga.css('div.text-truncate a.manga_title::text').get(),
                # 'author': quote.css('small.author::text').get(),
                # 'tags': quote.css('div.tags a.tag::text').getall(),
            }
            print(dictionary.get('title'))
            yield dictionary
