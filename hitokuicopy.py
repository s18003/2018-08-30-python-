#!/usr/bin/python3
# Webマンガヒトクイの好きな回をダウンロードする

import requests, os, bs4


print("取得したい話数を入力してください")
wasuu = input()
url = 'http://comichitokui.web.fc2.com'   # 開始URL
os.makedirs('hitokui/' + wasuu + '話', exist_ok=True)   # ./hitokuiに保存する

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

# 先程指定した回を取得する
url = 'http://comichitokui.web.fc2.com/' + wasuu + '.html'

# ページをダウンロードする
print('ページをダウンロード中 {}...'.format(url))
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

for i in range(30):
    # コミック画像のURLを見つける
    comic_elem = soup.select('#main img')
    if comic_elem == []:
        print('コミック画像が見つかりませんでした。')
    else:
        comic_url = 'http://comichitokui.web.fc2.com/' + comic_elem[i].get('src')

        # 画像をダウンロードする
        print('画像ダウンロードしてるから待ってや {}...'.format(comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

    # 画像を./hitokui/n話に保存する
    image_file = open(
        os.path.join('hitokui/' + wasuu + '話', os.path.basename(comic_url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)


print('完了')
