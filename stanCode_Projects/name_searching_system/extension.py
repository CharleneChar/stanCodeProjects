"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        # Establish HTTP request
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features='html.parser')
        # Collect all targeted content under <td> tag in a list subclass
        # (PS soup.select('tbody td') may be an alternative)
        targets = soup.find('tbody').find_all('td')
        cleaned_data = []
        male_num = 0
        female_num = 0
        # Clear <td> tags in targets
        for target in targets[:len(targets)-2]:
            cleaned_data += [target.text]
        # Count male and female total number respectively
        for i in range(len(cleaned_data)):
            if (i + 1) % 5 == 3:
                m_num_ls = cleaned_data[i].split(',')
                m_num = ''
                for n in m_num_ls:
                    m_num += n
                male_num += int(m_num)
            elif (i + 1) % 5 == 0:
                f_num_ls = cleaned_data[i].split(',')
                f_num = ''
                for n in f_num_ls:
                    f_num += n
                female_num += int(f_num)
        print(f'Male Number: {male_num}')
        print(f'Female Number: {female_num}')


if __name__ == '__main__':
    main()
