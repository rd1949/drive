import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import io

class APP_BO:
    def __init__(self):
        self.repository = ''


    def scrape_emails(self,domain):
        try:
            response = requests.get(domain)
            soup = BeautifulSoup(response.text, 'html.parser')
            emails = set()
            for link in soup.find_all('a', href=True):
                email = link.get('href')
                if email.startswith('mailto:'):
                    emails=email[7:]
                else:
                    email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', soup.text)
                    for mail in email:
                        if len(emails) == 1:
                            return emails
                        emails=mail
            return emails
        except:
            return []

    def search(self,domain):
        data = []
        emails = self.scrape_emails(domain=domain)
        data.append([domain, emails])
        df = pd.DataFrame(data, columns=['Name', 'email'])
        print(df.to_html())
        return df.to_html()

    def main(self,file):
        unparsedFile = file.read()
        dframe = pd.read_excel(unparsedFile)
        df = dframe.values.tolist()
        data = []
        for row in df:
            for domain in row:
                emails=self.scrape_emails(domain)
                data.append([domain,emails])
        df = pd.DataFrame(data, columns=['Name', 'email'])
        html = df.to_html()
        output = io.BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        output.seek(0)
        return output, html


if __name__ == '__main__':
    ur = APP_BO()
    print(ur.scrape_emails('https://www.livemint.com/Object/Uyx3KLeUKMSYmjl8xO3T3M/contactus.html'))

