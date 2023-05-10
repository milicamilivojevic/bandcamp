# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface

class BandcampPipeline:

    def __init__(self):
        self.genres = set()
        self.wishlist = list()


    def process_item(self, item, spider):
        """
        Save all genres that are followed and all genres from wish list for calculation.
        """
        if item['type'] == 'wishlist':
            self.wishlist.append(item['data']['genre_id'])
        elif item['type'] == 'genres':
            self.genres.add(item['data']['genre_id'])
        return item

    def close_spider(self, spider):
        """
        When scraping is done. Calculate Reliability and print it.
        """
        count = 0
        for one in self.wishlist:
            if one in self.genres:
                count = count + 1
        reliability = (count/len(self.wishlist)) * 100
        spider.logger.info(f'Reliability: {reliability}')