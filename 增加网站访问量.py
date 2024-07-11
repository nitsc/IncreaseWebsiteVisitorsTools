from bs4 import BeautifulSoup
import requests
import random
import concurrent.futures
import time

# 定义请求头，模拟浏览器行为
user_agents = [
    # Chrome on Windows 10
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    # Firefox on Windows 10
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    # Safari on macOS
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    # Edge on Windows 10
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    # Opera on Windows 10
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 OPR/45.0.2552.898',
    # Internet Explorer 11 on Windows 10
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    # Chrome on Android
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
    # Firefox on Android
    'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0',
    # Samsung Internet on Android
    'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36',
    # Opera on Android
    'Mozilla/5.0 (Linux; Android 6.0; Lenovo K33a42 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Opera/50.2.2429.143960 Mobile Safari/537.36 OPR/46.2.2246.120624',
    # UC Browser on Android
    'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; BKL-AL00'
]

# 定义延迟时间列表
delay_times = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70
]

# 要访问的URL列表
# 获取用户输入的字符串
input_str = input("请输入一个由逗号分隔的URL列表(要刷的网站): ")
try:
    urls = [int(x) for x in input_str.split(',') if x.isdigit()] + [
       'https://nitsc.github.io/',
       'https://blog.csdn.net/zwa20110606/article/details/140216292?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22140216292%22%2C%22source%22%3A%22zwa20110606%22%7D',
       'https://www.douyin.com/user/self?modal_id=7388399844714482978',
       'https://zhuanlan.zhihu.com/p/707278812',
       'https://github.com/nitsc/Ni_2',
       'https://github.com/nitsc/IncreaseWebsiteVisitorsTools']
except ValueError as e:
    print(f"输入错误: {e}")

# 测试代理IP并访问URL
def visit_url_with_proxy(url):
    try:
        # 随机选择一个延迟时间
        delay = random.choice(delay_times)
        # 随机选择请求头
        headers = {
            'User-Agent': random.choice(user_agents)
        }
        # 访问URL
        response = requests.get(url, headers=headers, timeout=5)
        # 打印访问信息
        print(f'请求头: {headers["User-Agent"]} | 访问网址: {url} | 访问延迟: {delay}')
    except requests.RequestException as e:
        print(f'访问网址: {url} | 错误: {e}')

# 主函数
if __name__ == '__main__':
    while True:
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(urls)) as executor:
            # 创建一个任务列表
            futures = []
            for url in urls:
                # 提交任务到线程池
                future = executor.submit(visit_url_with_proxy, url)
                futures.append(future)
            
            # 等待所有任务完成
            for future in concurrent.futures.as_completed(futures):
                pass  # 可以在这里处理每个任务的结果，这里只是等待
