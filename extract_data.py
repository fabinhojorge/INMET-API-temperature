#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Fabio Rodrigues Jorge
Email: fabinhojorgenet@gmail.com
Description: Web Crawler to extract information from BDMEP (INMET) database.
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
from config import LOGIN
from datetime import datetime
from station import Station
# import csv


def init_webdriver_config(impl_delay=30):
    """Function to set the configuration of the Selenium web Driver."""

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    chrome_driver = webdriver.Chrome(chrome_options=chrome_options)
    chrome_driver.implicitly_wait(impl_delay)
    return chrome_driver


def get_page(_driver, _url):
    """Helper function that navigates and returns an BeautifulSoup page."""
    _driver.get(_url)
    time.sleep(3)
    return BeautifulSoup(_driver.page_source, 'html.parser')


def inmet_login(_driver):
    """This function navigates to the login page and do the login."""

    get_page(_driver, LOGIN['url'])

    _driver.find_element_by_name("mCod").send_keys(LOGIN['username'])
    _driver.find_element_by_name("mSenha").send_keys(LOGIN['password'])
    _driver.find_element_by_name("btnProcesso").click()


def load_station_numbers(_path):
    """It returns the list of stations."""
    _f = open(_path)
    _station_numbers = _f.readlines()
    _station_numbers = list(map(lambda x: x.replace("\n", ""), _station_numbers))
    _f.close()
    return _station_numbers


def weather_station_parser(_data):

    ds = _data.split('\n')
    s = Station(ds[1][20:], ds[2][20:], ds[3][20:], ds[4][20:], ds[5], ds[6][20:])
    print(s)
    return s


def weather_observation_parser(_data):
    ds = _data.split('\n')
    ds = list(filter(None, ds))
    # header is ds[0]
    print(ds[0])
    print(*ds[1:], sep='\n')


# if __name__ == '__main__':

print(">> WebCrawler Started <<")

driver = init_webdriver_config(30)

# -- Login --
inmet_login(driver)


# -- Extract --
url_pattern = "http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt_mensal.php?&mRelEstacao={omm_code}" \
      "&btnProcesso=serie&mRelDtInicio={start_date}&mRelDtFim={end_date}&mAtributos={attributes}"

station_numbers = load_station_numbers("./data/station_numbers.txt")

start_date = "01/07/2000"
end_date = datetime.now().strftime("%d/%m/%Y")
# attributes = "1,,,,,,,,,,,,1,1,1,1,"
attributes = "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"

count_success = 0
count_error = 0

for omm_code in station_numbers[:4]:
    url = url_pattern.format(omm_code=omm_code, start_date=start_date, end_date=end_date, attributes=attributes)
    soup = get_page(driver, url)

    soup_pre = soup.select('pre')

    if 'Não existem dados disponiveis' in soup_pre[0].text:
        count_error += 1
    else:
        count_success += 1
        content = soup_pre[0].text.split('--------------------')

        station = weather_station_parser(content[2])
        weather_observation_parser(content[4])


# driver.quit()

print(">> WebCrawler Finished <<")
print("SUCCESS: {0}\nERROR: {1}\nTOTAL: {2}".format(count_success, count_error,
                                                    count_success + count_error))
