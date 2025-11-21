# scrapy runspider filmscraper.py
import scrapy
import json
from scrapytutorial.items import ScrapytutorialItem

class FilmscraperSpider(scrapy.Spider):
    name = "filmscraper"
    allowed_domains = ["www.scrapethissite.com"]
    
    start_year = 2010
    end_year = 2015

    def start_requests(self):
        yield scrapy.Request(
            url = f"https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={self.start_year}",
            callback = self.parse, 
            cb_kwargs = {"year": self.start_year}
        )

    def parse(self, response, year):
        films = json.loads(response.text)
        for film in films:
            item = ScrapytutorialItem()
            item["year"] = year
            item["title"] = film.get("title")
            item["nominations"] = film.get("nominations")
            item["awards"] = film.get("awards")
            yield item

        next_year = year + 1

        if next_year <= self.end_year:
            next_url = f"https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={next_year}"
            yield response.follow(
                url=next_url,
                callback=self.parse,
                cb_kwargs={"year": next_year}
            )