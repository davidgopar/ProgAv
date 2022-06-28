#! ./venv/bin/python3.8
# -*- coding: utf-8 -*-
"""
Extensión de happiness para Tarea 12
DAVID GOPAR MORALES

Download world happiness time series from hedonometer project.
See https://hedonometer.org/timeseries/en_all/?from=2020-08-24&to=2022-02-23
Created on Tue Feb 24 15:35:23 2022

@author: Feliú Sagols
CDMX
"""

import csv
import requests
# import psycopg2
import datetime
# import pandas as pd

import loggers
TIMESERIES_DATABASE = "ts_db"

global LOGGER


# def last_available_date():
#     """
#     Returns the newest record base_date in happiness table
#     """
#     conn = psycopg2.connect("dbname=%s user=fsagols host=localhost" %
#                             TIMESERIES_DATABASE)
#     cur = conn.cursor()
#     cur.execute("""
#         select date_
#         from happiness
#         order by date_ desc
#         limit 1;
#         """)
#     date_ = cur.fetchone()[0]
#     conn.close()
#     return date_


# def get_happiness_ts(last_date, last_days):
#     """
#     Returns the happiness time series.
#
#     Parameters
#     ----------
#     last_date : datetime.pyi
#         Last base_date in the time period to download.
#     last_days:
#         Number of days previous to the last base_date to download.
#
#     Examples
#     --------
#     >>> get_happiness_ts(datetime.datetime(2022, 2, 26), 700)
#
#     Returns
#     -------
#         A dataframe with the time series.
#     """
#     conn = psycopg2.connect("dbname=%s user=fsagols host=localhost" %
#                             TIMESERIES_DATABASE)
#     cur = conn.cursor()
#     cur.execute(
#         """
#         select date_, happiness
#         from happiness
#         where date_ <= %(last_date)s
#         order by date_ desc limit %(last_days)s;
#         """, {
#             'last_date': last_date,
#             'last_days': last_days
#         })
#     answer = cur.fetchall()
#     answer.reverse()
#     answer = [[a[0], a[1]] for a in answer]
#     df = pd.DataFrame(data=answer, columns=['base_date', 'happiness'])
#     df.set_index('base_date', inplace=True)
#     return df


def download_happiness(start_date, records):
    """
    Download happiness records from the url below. Happiness records are stored
    into happiness database table.

    Parameters
    ----------
    start_date : datetime.pyi
        Initial downloading base_date.
    records : int
        Maximum number of records after start_date to download.
    """
    LOGGER.debug("Downloading happiness time series.")
    data_json = requests.get(
        'https://hedonometer.org/api/v1/happiness/?format=json&timeseries__'
        f'title=en_all&date__gte='
        f'{start_date.strftime("%Y-%m-%d")}&limit={records}')

    data = data_json.json()
    data = [[
        datetime.datetime.strptime(d['date'], "%Y-%m-%d"), d['frequency'],
        float(d['happiness'])
    ] for d in data['objects']]
    # conn = psycopg2.connect("dbname=%s user=fsagols host=localhost" %
    #                         TIMESERIES_DATABASE)
    LOGGER.info("Storing happiness time series.")
    # cur = conn.cursor()
    # cur.executemany(
    #     """
    #     insert into happiness
    #     values (%s, %s, %s)
    #     on conflict (date_)
    #     do nothing;
    #     """, data)
    # conn.commit()
    # conn.close()
    data = sorted(data, key=lambda l: l[0])

    with open('happ.txt', mode='w') as happ:
        happ_writer = csv.writer(happ, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        happ_writer.writerow(['date', 'frequency', 'happiness'])
        happ_writer.writerows((d for d in data))


def r_happiness(intervalo):
    lista = []
    for fechas in intervalo:
        with open('happ.txt', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            if len(fechas) == 3:
                salto = fechas[2]
            else:
                salto = 1
            ini = fechas[0]
            if len(fechas) >= 2:
                fin = fechas[1]
            else:
                fin = ini
            c = 0
            for row in csv_reader:
                if datetime.datetime.strptime(ini, '%Y-%m-%d') <=\
                        datetime.datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S') <= \
                        datetime.datetime.strptime(fin, '%Y-%m-%d'):
                    if c == 0:
                        lista.append(f' date {row["date"]}, happiness:, {row["happiness"]}')
                        c = salto
                    c -= 1
            lista.append('-'*50)
    return lista

if __name__ == "__main__":
    LOGGER = loggers.define_logger("happiness.log")
    date = datetime.datetime(2022, 1, 1)
    download_happiness(date, 5000)

for a in r_happiness([['2022-03-29', '2022-05-24', 3], ['2022-05-25'], ['2022-05-25', '2022-05-30', 2]]):
    print(a)
