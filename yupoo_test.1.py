import re
import requests
import os

SID = ''



def save_urls2file(urls=None):
    with open('urls.txt','a') as f:
        if urls == None:
            pass
        elif type(urls) is str:
            f.write(urls)
            f.write("\n")
        elif type(urls) is list:
            for strs in urls:
                f.write(strs)
                f.write("\n")
        else:
            pass

def sid_test(SID=None):
    r = requests.get('http://www.yupoo.com/account/', allow_redirects=False, cookies={
        'sid': SID,
    })
    globals API, UID
    
    if r.status_code != 200:
        print('wrong SID')
        return status1 = "wrong_sid", API = 0, UID = 0
        #exit()
    else:
        api_regex = re.search(r',apiKey: \'(.+)\',apiSecret:.+,user: {id: (\d+),username:', r.text)
        if api_regex is None:
            print('no KEY and UID')
            return status1 = "nokeyanduid", API = 0, UID = 0
            #exit()
        else:
            API = api_regex.group(1)
            UID = api_regex.group(2)
            return status1 = "ok", API, UID


def requestsget(method1=None, kind1=None, id1=None):
    para = {
        'format': 'json',
        'api_key': API,
        'ypp': 1,
    }
    para['method'] = method1
    para[kind1] = id1
    r = requests.get('http://www.yupoo.com/api/rest/', params=para
    }, cookies={
        'sid': SID,
    })
    return r.json()


def get_photo_url(pid):
    data = requestsget('yupoo.photos.getInfo', 'photo_id',pid)

    if data['stat'] == 'ok':
        photo = data['photo']
        url = 'http://photo.yupoo.com/' + \
              photo['bucket'] + '/' + photo['key'] + '/' + photo['secret'] + '.' + photo['originalformat']
        title = photo['title'] + '.' + photo['originalformat']
    else:
        print('# API stat:', data['stat'])
        url = title = ''

    return url, title


def get_all_albun_photo():
    data = requestsget('yupoo.albums.getList', 'user_id', UID)

    if data['stat'] == 'ok':
        for album in data['albums']:
            print('#', album['title'], album['photos'])
            data = requestsget('yupoo.albums.getPhotos', 'album_id', album['id'])

            if data['stat'] == 'ok':
                for photo in data['album']['photos']:
                    url, fn = get_photo_url(photo['id'])
                    print(url)
                    save_urls2file(url)
                    print('  out=' + album['title'] + '/' + fn)
            else:
                print('# API stat:', + data['stat'])

    else:
        print('# API stat:', data['stat'])




if __name__ == "__main__":
    #urls = "我爱你中国"
    #urls = ["我爱你中国","什么鬼","喔喔"]
    #save_urls2file(urls)
    get_all_albun_photo()