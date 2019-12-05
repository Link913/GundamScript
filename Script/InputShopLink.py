from selenium import webdriver
import datetime
import time

def login():
    # 打开淘宝首页，通过扫码登录
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print(f"请尽快扫码登录")
        time.sleep(10)

def openShopLink(
    shopLink
):
    browser.get(shopLink)
    time.sleep(3)

def buy(times):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        
        # 降低能耗 减少CPU压力, 一秒轮询一次, 如果对电脑有自信可以调小一点
        time.sleep(1)

        # 对比时间，时间到的话就点击结算
        if now > times:
            
            # 点击结算按钮
            while True:
                try:
                    if browser.find_element_by_link_text("立即购买"):
                        browser.find_element_by_link_text("立即购买").click()
                        print("结算成功，准备提交订单")
                        break
                except:
                    pass
            # 点击提交订单按钮
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
                        print(f"抢购成功，请尽快付款")
                except:
                    print(f"再次尝试提交订单")
            time.sleep(0.01)

if __name__ == "__main__":

    # 自动打开Chrome浏览器
    browser = webdriver.Chrome("./chromedriver")
    # 设置浏览器最大化显示
    browser.maximize_window()

    # 登录淘宝
    login()

    # 打开商品链接 这里需要定制
    shopLinkUrl = "https://detail.tmall.com/item.htm?spm=a230r.1.14.13.47442910oY6Nn9&id=605963854527&cm_id=140105335569ed55e27b&abbucket=6&skuId=4243352472594"
    openShopLink(shopLinkUrl)

    # 请指定抢购时间，时间格式："2019-06-01 10:08:00.000"
    times = "2019-06-04 08:35:00.000"
    # 等待定时抢购时间 秒杀
    buy(times)