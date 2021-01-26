# -*- coding: utf-8 -*-
import scrapy
import re
from project.items import ProjectItem

class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/090200,000000,0000,32,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']
    # start_url = 'https://careers.tencent.com/search.html?index='


    def parse(self, response):
        #提取每个response的数据
        node_list = response.xpath("//div[@class='dw_table']/div[@class='el']")
        total_page_pig = response.xpath("//span[@class = 'td']/text()")
        #正则表达式提取页数
        pattern1 = re.compile(r"(?<=共).+?(?=页，)")#我们在编译这段正则表达式
        matcher1 = re.search(pattern1,r""+str(total_page_pig))#在源文本中搜索符合正则表达式的部分
        total_page = (matcher1.group(0))#页数
        print(total_page)

        for node in node_list:
            # 新建一个item
            item = ProjectItem()
            print('进入！！')
            item['position_name'] = node.xpath("./p/span/a/@title").extract()[0]#返回list中的第一个元素  职位
            item['posttion_place'] = node.xpath("./span[1]/a/text()").extract()[0]#公司
            item['posttion_led'] = node.xpath("./span[2]/text()").extract()[0]#地点
            if len(node.xpath("./span[3]/text()")):
                item['position_department'] = node.xpath("./span[3]/text()").extract()[0]#薪资
            else:
                item['position_department'] = '空'
            item['positon_time'] = node.xpath("./span[4]/text()").extract()[0]#时间
            item['position_info'] = node.xpath("./span[1]/a/@href").extract()[0]#网址
            print('1')
            yield item

        # s = (response.xpath("//li[@class='bk']/a/@href")).extract()[0]

        # print('\n\n\n\n\n\n',type(s),'\n',s,'\n\n\n\n\n\n\n')

        # s = (response.xpath("//li[@class='bk']/a/@href")).extract()[1]

        # print('\n\n\n\n\n\n',type(s),'\n',s,'\n\n\n\n\n\n\n')

        #打印当前页数
        print('\n\n\n\n\n\n',str(response.xpath("//div[@class = 'p_in']/ul/li[@class='on']/text()").extract()[0]),'\n\n\n\n\n\n\n')

        # #判断当前页是不是最后一页
        if str(response.xpath("//div[@class = 'p_in']/ul/li[@class='on']/text()").extract()[0]) != total_page:
            if str(response.xpath("//div[@class = 'p_in']/ul/li[@class='on']/text()").extract()[0]) == '1':
                url = (response.xpath("//li[@class='bk']/a/@href")).extract()[0]
                yield scrapy.Request(url,callback = self.parse)
            else:
                url = (response.xpath("//li[@class='bk']/a/@href")).extract()[1]
                # print('\n\n\n\n\n',url,'\n\n\n\n\n\n')
                yield scrapy.Request(url,callback = self.parse)



# -*- coding: utf-8 -*-
# import scrapy

# import re
# from project.items import DemoItem

# class ItcastSpider(scrapy.Spider):
#     name = '51job'
#     #允许域,可以是多个
#     allowed_domains = ['http://www.itcast.cn']
    
#     #scrapy 开始发起请求的地址
#     start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

#     def parse(self, response):

#         html = response.text
#         reg =r'<img data-original="(.*?)">.*?<div class="li_txt">.*?<h3>(.*?)</h3>.*?<h4>(.*?)</h4>.*?<p>(.*?)</p>'
#         infos = re.findall(reg,html,re.S)

#         for img,name,grade,talk in infos:
#             item = DemoItem()
#             item['name'] = name
#             item['grade'] = grade
#             item['info'] = talk
#             item['img'] = self.allowed_domains[0] + img
#             #这里是用的yield 而不是return
            # yield item

