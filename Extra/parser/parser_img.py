import requests

def get_file(url):
    resp = requests.get(url, stream=True)

    return resp
    
def save_data(name, file_data):
    with open(name, 'wb') as file:
        for chunk in file_data.iter_content(4096):
            file.write(chunk)

def get_name(url):
    name = url.split('/')[-1]

    return name

def main():
    urls = ['http://s1.oboiki.net/uploads/images/others/2015/10/2f76354ffdfe3130c3efd1366353df15/varkraft-anduin-lotar_1920x1080.jpg',
       'http://s1.oboiki.net/uploads/images/others/2015/10/f566d6b2f6d1e13e3ef4b5b2f1d3e3fa/kotyara-morda-v-blizi_1920x1080.jpg',
       'http://s1.oboiki.net/uploads/images/others/2015/06/c2258ec79a3fab83b18426cbbc813feb/minony_1920x1080.jpg']

    for url in urls:
        save_data(get_name(url), get_file(url))

if __name__ == '__main__':
    main()