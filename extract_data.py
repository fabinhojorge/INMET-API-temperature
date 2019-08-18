#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Fabio Rodrigues Jorge
Email: fabinhojorgenet@gmail.com
Description: Web Crawler to extract information from BDMEP (INMET) database.
"""

import time
import sys
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from config import LOGIN, URL_TEMPLATE
from datetime import datetime
from station import Station


class InputError(Exception):
    """Exception raised for errors in the input."""
    pass


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
    time.sleep(5)
    return BeautifulSoup(_driver.page_source, 'html.parser')


def inmet_login(_driver):
    """This function navigates to the login page and do the login."""

    get_page(_driver, LOGIN['url'])

    _driver.find_element_by_name("mCod").send_keys(LOGIN['username'])
    _driver.find_element_by_name("mSenha").send_keys(LOGIN['password'])
    _driver.find_element_by_name("btnProcesso").click()


def get_url_pattern():
    """This function returns the URL pattern accordingly to the Template passed as system parameter."""

    if len(sys.argv) > 1:
        if sys.argv[1].upper() in URL_TEMPLATE.keys():
            print('TEMPLATE: ', sys.argv[1].upper())
            return URL_TEMPLATE[sys.argv[1].upper()]
        else:
            raise InputError('The template {0} don´t exist.'.format(sys.argv[1].upper()))

    print('TEMPLATE Default: MONTH')
    return URL_TEMPLATE['MONTH']


def load_station_numbers(_path):
    """It returns the list of stations."""

    with open(_path) as _file:
        _station_numbers = _file.readlines()
        _station_numbers = list(map(lambda x: x.replace("\n", ""), _station_numbers))

    return _station_numbers


if __name__ == '__main__':

    print(">> WebCrawler Started <<")

    count_success = 0
    count_error = 0
    station_list = []

    driver = init_webdriver_config(30)

    try:
        inmet_login(driver)

        url_pattern = get_url_pattern()

        station_numbers = load_station_numbers("./data/station_numbers.txt")

        start_date = "01/01/2018"
        end_date = datetime.now().strftime("%d/%m/%Y")

        for omm_code in station_numbers:
            url = url_pattern.format(omm_code=omm_code, start_date=start_date, end_date=end_date)
            soup = get_page(driver, url)

            soup_pre = soup.select('pre')

            if len(soup_pre) == 0:  # In case of an exception go to the next station
                continue

            if 'Não existem dados disponiveis' in soup_pre[0].text:
                count_error += 1
            else:
                content = soup_pre[0].text.split('--------------------')
                station = Station.parser(content[2])
                station.set_observation(Station.observation_parser(content[4]))
                station_list.append(station)
                count_success += 1

    except InputError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        print(">> WebCrawler Finished <<")
        print("SUCCESS: {0}\nERROR: {1}\nTOTAL: {2}".format(count_success, count_error, count_success + count_error))

    if len(station_list) == 0:
        print('No data collected. Exiting...')
        exit()

    print(">> Data Processing Started <<")

    data_header = list(filter(None, station_list[0].weather_observation_header.split(';')))
    header = Station.get_station_header() + data_header

    file_path = 'data/output_data.csv'
    with open(file_path, 'w', newline='\n', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', quotechar="'", quoting=csv.QUOTE_MINIMAL)

        writer.writerow(header)

        for station in station_list:
            for ob in station.weather_observation:
                row = station.get_station_information() + ob.split(';')
                writer.writerow(row)

        print('Saving the file {0} [...]'.format(file_path))

    print(">> Data Processing Finished <<")
