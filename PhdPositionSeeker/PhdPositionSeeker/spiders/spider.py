from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from PhdPositionSeeker.items import PhdpositionseekerItem

class PhdPositionSeeker(CrawlSpider):
    name = "seeker"
    start_urls = ['http://www.wis.ewi.tudelft.nl/vacancies/']
    
    def parse(self, response):
    	item = PhdpositionseekerItem()
    	selector = Selector(response)

    	title_path = "//h4[contains(@style,'line-height: normal;')]//strong"
    	content_path = "//h4[contains(@style,'line-height: normal;')]/following-sibling::p"

    	titles = selector.xpath(title_path)
    	for title in titles:
    		position_title = title.xpath(title_path + "/text()").extract()
    		item['title'] = position_title

    	contents = selector.xpath(content_path)
    	for content in contents:
    		position_content = content.xpath(content_path + "/text()").extract()
    		item['content'] = position_content

    	yield item
        