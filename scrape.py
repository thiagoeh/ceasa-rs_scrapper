import pandas as pd
import datetime
import logging


base_url = "http://www.ceasa.rs.gov.br/sis/files/"



def scrape(report_date: datetime.date) -> pd.DataFrame:
    scrape_url = base_url + report_date.strftime('%d-%m-%Y') + ".html"
    logging.info("Scrapping from: " + scrape_url)
    
    # pinning the parser as lxml; taking the first (and only) table
    quote = pd.read_html(scrape_url, thousands='', decimal=',', header=None, flavor='lxml')[0]
    
    # the table come with no headers in the HTML
    quote.columns = ["Product", "Unit", "UnitAmount", "PriceMax", "PriceUsual", "PriceMin"]

    return {report_date: quote}


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    report = scrape(datetime.date.today() - datetime.timedelta(1))
    print(report)