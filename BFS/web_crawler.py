# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        urls = []

        crawled = deque()
        crawled.append(startUrl)
        hostname = startUrl.split('/')[2]

        while crawled:
            url = crawled.pop()
            curr_hostname = url.split('/')[2]
            if url in urls or hostname != curr_hostname:
                continue

            urls.append(url)
            urls_to_crawl = htmlParser.getUrls(url)

            for url in urls_to_crawl:
                crawled.append(url)

        return urls
