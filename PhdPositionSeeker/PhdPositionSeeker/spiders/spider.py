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

    	titles = selector.xpath("//h4[contains(@style,'line-height: normal;')]//strong")
    	for title in titles:
    		position_title = title.xpath("//h4[contains(@style,'line-height: normal;')]//strong/text()").extract()
    		item['title'] = position_title

    	contents = selector.xpath("//h4[contains(@style,'line-height: normal;')]/following-sibling::p")
    	for content in contents:
    		position_content = content.xpath("//h4[contains(@style,'line-height: normal;')]/following-sibling::p/text()").extract()
    		item['content'] = position_content

    	yield item
        