# ceasa_scrapper
A web scrapper for analysis of CEASA-RS food items price history

CEASA-RS prices are [available online](http://www.ceasa.rs.gov.br/cotacao.php), with historical information available.

Each day the prices of different products are internally collected, and a daily report is generated.

There reports are published in this format:
```
http://www.ceasa.rs.gov.br/sis/files/DD-MM-YYYY.html
```

Here is a (at edit time) [recent report](http://www.ceasa.rs.gov.br/sis/files/27-03-2018.html)


This small project intends to automatically scrape the prices from at least the previous year, to eventually build some analysis of the data set.

The python environment is managed through [pipenv](https://docs.pipenv.org/#install-pipenv-today).

To install this project:
```bash
$ git clone https://github.com/thiagoeh/ceasa-rs_scrapper.git
$ cd ceasa-rs_scrapper
$ pipenv install
```

