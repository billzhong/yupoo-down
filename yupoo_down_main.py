import re
import requests
import os

SID = ''

class download_main():
    def __init__(self, SID):
        self.SID = SID
        self.API = ''
        self.UID = ''
        self.sid_test(SID)
        self.statusx = ''



    def save_urls2file(self, urls=None):
        with open('urls.txt','a') as f:
            if urls == None:
                pass
            elif type(urls) is str:
                f.write(urls)
                f.write("\n")
                self.statusx = "已经导出1条下载链接"
            elif type(urls) is list:
                for strs in urls:
                    f.write(strs)
                    f.write("\n")
                    self.statusx = "已经导出1条下载链接"
            else:
                pass

    def sid_test(self, SID=None):
        r = requests.get('http://www.yupoo.com/account/', allow_redirects=False, cookies={
            'sid': self.SID,
        })
        
        if r.status_code != 200:
            self.statusx = "wrong SID，请重新查找SID"
            print('wrong SID')
            status1 = "wrong_sid"
            self.API = 0 
            self.UID = 0
            #exit()
        else:
            api_regex = re.search(r',apiKey: \'(.+)\',apiSecret:.+,user: {id: (\d+),username:', r.text)
            if api_regex is None:
                self.statusx = "no KEY and UID，SID不对，查找不到对应的key和UID"
                print('no KEY and UID')
                status1 = "nokeyanduid"
                self.API = 0 
                self.UID = 0
                #exit()
            else:
                self.API = api_regex.group(1)
                self.UID = api_regex.group(2)
                status1 = "ok"
        return status1, self.API, self.UID


    def requestsget(self, method1=None, kind1=None, id1=None):
        para = {
            'format': 'json',
            'api_key': self.API,
            'ypp': 1,
        }
        para['method'] = method1
        para[kind1] = id1
        r = requests.get('http://www.yupoo.com/api/rest/', params=para
        , cookies={
            'sid': self.SID,
        })
        return r.json()


    def get_photo_url(self, pid):
        data = self.requestsget('yupoo.photos.getInfo', 'photo_id',pid)

        if data['stat'] == 'ok':
            photo = data['photo']
            url = 'http://photo.yupoo.com/' + \
                photo['bucket'] + '/' + photo['key'] + '/' + photo['secret'] + '.' + photo['originalformat']
            title = photo['title'] + '.' + photo['originalformat']
        else:
            self.statusx = "# API stat:" +  data['stat']
            print('# API stat:', data['stat'])
            url = title = ''

        return url, title


    def get_all_albun_photo(self, UID=None):
        data = self.requestsget('yupoo.albums.getList', 'user_id', self.UID)

        if data['stat'] == 'ok':
            for album in data['albums']:
                self.statusx = "相册" + album['title'] + str(album['photos']) + "张图"
                print('#', album['title'], album['photos'])
                data = self.requestsget('yupoo.albums.getPhotos', 'album_id', album['id'])

                if data['stat'] == 'ok':
                    for photo in data['album']['photos']:
                        url, fn = self.get_photo_url(photo['id'])
                        print(url)
                        self.save_urls2file(url)
                        self.statusx = "图片" + album['title'] + '/' + fn
                        self.statusx = url
                        print('  out=' + album['title'] + '/' + fn)
                else:
                    self.statusx = '# API stat:', + data['stat']
                    print('# API stat:', + data['stat'])

        else:
            self.statusx = '# API stat:', data['stat']
            print('# API stat:', data['stat'])




if __name__ == "__main__":
    #urls = "我爱你中国"
    #urls = ["我爱你中国","什么鬼","喔喔"]
    #save_urls2file(urls)
    idd = '2uhhesu5b7edsu62dvd89hcoe7'
    d = download_main(idd)
    d.get_all_albun_photo()