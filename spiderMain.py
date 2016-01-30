#coding:utf-8
#总控程序
import urlManager,htmlDownloader,htmlParser,htmlOutputer
class SpiderMain(object):
	def __init__(self):
		self.urls = urlManager.UrlManager()
		self.downloader = htmlDownloader.HtmlDownloader()
		self.parser = htmlParser.HtmlParser()
		self.outputer = htmlOutputer.HtmlOutputer()
	def craw(self,root_url):
		count = 1
		self.urls.add_new_url(root_url)
		 #将入口url传给url管理器
		while self.urls.has_new_url():
		 #循环爬取url
			try:#异常捕获
				new_url = self.urls.get_new_url()		
				#从url管理器中取出一个新的url
				print 'craw No.%d : %s'%(count,new_url)
				#打印输出爬取的url
				html_cont = self.downloader.download(new_url)
				#将新url中的代码加载到变量里
				new_urls,new_data  = self.parser.parse(new_url,html_cont) 	
				#从新url中获取其指向的url集合和数据
				self.urls.add_new_urls(new_urls) 
				#将url集合放入url管理器中
				self.outputer.collect_data(new_data)				
				#将数据放入outputer中进行处理
				if(count == 50):
					break;
				#最多爬取1000个页面
				count = count + 1
			except:
				print 'craw falied'
		self.outputer.output_html()
		#输出处理好的数据
if __name__ =="__main__":	
	root_url = "http://baike.baidu.com/view/21087.htm"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)
