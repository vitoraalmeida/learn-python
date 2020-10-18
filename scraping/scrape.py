import os
import sys
import requests
import datetime
import pandas as pd
from requests_html import HTML


BASE_DIR = os.path.dirname(__file__)


def url_to_txt(url, filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{year}.html", 'w') as f:
                f.write(html_text)
        return html_text
    return None


def parse_and_extract(url, name='2020'):
    html_text = url_to_txt(url)
    if html_text == None:
        return False
    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table"
    r_table = r_html.find(table_class)
    table_data = []
    header_names = []
    if len(r_table) == 0:
        return False

    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]
    header_cols = header_row.find("th")
    header_names = [x.text for x in header_cols]

    for row in rows[1:]:
        #print(row.text)
        cols = row.find("td")
        row_data = []
        for i, col in enumerate(cols):
            #print(i , col.text, '\n\n')
            row_data.append(col.text)
        table_data.append(row_data)

    path = os.path.join(BASE_DIR, 'data')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join('data', f'{name}.csv')
    df = pd.DataFrame(table_data, columns=header_names)
    df.to_csv(filepath, index=False)
    return True


def run(start_year=None, years_ago=0):
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert len(str(start_year)) == 4

    for i in range(0, years_ago + 1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        finished = parse_and_extract(url, name=str(start_year))
        if finished:
            print(f"Finished {start_year}")
        else:
            print(f"{start_year} not finished")

        start_year -= 1


if __name__ == "__main__":
    try:
        start = int(sys.argv[1])
    except:
        start = None
    try:
        count = int(sys.argv[2])
    except:
        count = 0
    run(start_year=start, years_ago=count)

