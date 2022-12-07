from bs4 import BeautifulSoup
from lxml import etree
import requests

urls = []
hrefs = []

from requests_html import HTMLSession




def GetIBBLinks():
    with open("source.txt") as file_in:
        for line in file_in:
            line = line.replace("\n","")
            urls.append(line)


def ExtractHTML():
    for url in urls:
        session = HTMLSession()
        web_page = url
        respone = session.get(web_page)
        page_html = respone.html
        divs_parent_to_h2 = page_html.xpath('//*[@id="embed-code-2"]')
        for element in divs_parent_to_h2:
            s = element.attrs["value"];
            hrefs.append(s)

def CreateWebPage():
    html_page = "<!DOCTYPE html>" \
                "<html>" \
                "<head><" \
                "title>Gallery</title>" \
                "</head>" \
                "<body>" \
                "BODYTEXT" \
                "</body>" \
                "</html>"
    bodytext = ""
    for href in hrefs:
        bodytext = bodytext + href + "<br>\n"

    html_page = html_page.replace("BODYTEXT", bodytext)
    with open('index.html', 'w') as my_data_file:
        my_data_file.write(html_page)

if __name__ == '__main__':
    GetIBBLinks()
    ExtractHTML()
    CreateWebPage()
    print("Done")
