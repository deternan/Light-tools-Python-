'''
form from 'tutu0511'

private repository:
https://github.com/tutu0511/Patent/blob/main/Crawler.py
'''

from json import dump
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd
from tqdm import tqdm

def discussion(driver, soup):
    #放大視窗，因為旁邊的icon會擋住下一頁的按鈕
    driver.maximize_window()
    #滑鼠直接移到商品留言區
    target = driver.find_element_by_xpath('//*[@id="comment"]/div[1]/h3')
    #滾輪下滑，以便載入留言
    driver.execute_script("arguments[0].scrollIntoView();", target)
    #等待載入
    time.sleep(5)
    discussion_list = []
    star_level_list = []
    #判斷是否有下一頁
    next_page = True
    page = 1 #檢查現在印到第幾頁
    # for i in tqdm(range(1,10)): #測試用的迴圈
    while(next_page == True): #如果還有下一頁，則繼續迴圈
        print("page: ", page)
        star_list = []
        #抓取現在頁面的html
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        #找到每個評論div下的所有留言(有些會補充留言)
        tag_list = soup.findAll("div", class_= "comment-column")
        #找到留言的tag
        for tag in tag_list:
            # print(tag)
            discussion = tag.findAll('p', class_='comment-con')
            temp_discussion = []
            #把同一個人的留言合併成一個list
            for dis in discussion:
                temp_discussion.append(dis.getText())
            discussion_list.append(temp_discussion)
            # if(page == 2):
            #     print(temp_discussion)
        #找到現在頁面所有評價星等
        star = soup.findAll("div", class_ = "comment-star")
        #找到class中的"star數字的模板"
        star_list.append([level['class'][1] for level in star])
        #抓取"star數字"中的"數字"，此"數字"就是評價的星等等級
        for star in star_list:
            for number in star:
               star_level_list.append(number[-1])
        #抓取頁面那一排所有的值
        page_list = driver.find_elements_by_xpath('//*[@id="comment-0"]/div[12]/div/div/a')
        #最後一個是下一頁按鈕或最後一頁的按鈕
        if(page_list[-1].text == '下一页'):
            page_list[-1].click()
            page += 1
            next_page = True
        #如果是最後一頁，抓取最後一頁的資訊
        else:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            discussion = soup.findAll("p", class_= "comment-con")
            discussion_list.append([content.getText() for content in discussion])
            next_page = False
            break
        time.sleep(5)
    return discussion_list, star_level_list

#main
#載入driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://item.jd.com/100019034176.html")
soup = BeautifulSoup(driver.page_source, 'html.parser')
#所有評論list
discussion_list, star_level_list = discussion(driver, soup)
#將資料存進excel中
dicussion_output_list = []
star_output_list = []
#處理評論
# for dicussion in discussion_list:
for i in range(0, len(discussion_list)-1):
    dicussion_output_list.append(str(discussion_list[i]))

#處理星等
for star_level in star_level_list:
    star_output_list.append(star_level)
#將最終結果存成excel檔
df_star = pd.DataFrame(star_output_list, columns=['star(1~5)'])
df_dicussion = pd.DataFrame(dicussion_output_list, columns=['discussion'])
df = pd.concat([df_star, df_dicussion], axis=1)
df.to_excel('discussion.xlsx', index=False)
