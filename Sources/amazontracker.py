import requests
import smtplib
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from smtplib import SMTPException

URL = 'https://www.amazon.it/dp/B01N7UDIRG/?coliid=IUJAW1TWDNEF2&colid=USCD1GDNFBYM&psc=1&ref_=lv_ov_lig_dp_it'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'}
user = 'michele.angrisano@gmail.com'
password = 'vnrpoovgrpqgdlqm'


def check_price(URL, pprice):
    availibility = None
    try:
        page = requests.get(URL, headers=headers)
        page.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        title = soup.find(id="productTitle").get_text()
    except AttributeError as attr_err:
        print(f'Attribute Error occurred: {attr_err}')
        return
    price = int(soup.find(id="priceblock_ourprice").get_text()[:3])
    availibility = soup.find(id=availibility).get_text()
    for d in soup.findAll('div', attrs={'class': 'a-section a-spacing-top-micro'}):
        availibility = d.find('span', attrs={'class': 'a-size-medium a-color-state'}).get_text()
    if price < pprice:
        send_mail()

    print(title.strip())
    print(f'Price: {price}')
    print(availibility.strip())


def send_mail():
    try:
        # Connect to the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
    except SMTPException as smtp_err:
        print(f'SMTP error: {smtp_err}')
        return
    # Login to the server mail
    try:
        server.login(user, password)
        subject = 'Price fell down'
        body = 'Check the link: ' + URL
        msg = f'Subject: {subject}\n\n{body}'
    except SMTPException as smtp_err:
        print(f'Error login occurred: {smtp_err}')
        return
    # Send the mail
    try:
        server.sendmail(
            user,
            user,
            msg
        )
    except SMTPException as smtp_err:
        print(f'Send mail error: {smtp_err}')
        return
    print('Mail sent')
    # Quit the server
    server.quit()


check_price(URL, 800)
