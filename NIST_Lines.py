from bs4 import BeautifulSoup
import requests
import pandas as pd
import io
import re
import matplotlib.pyplot as plt
import warnings
from pandas.core.common import SettingWithCopyWarning

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)



class Lines_LIBS(object):

    def __init__(self, element, low_w, upper_w, strongLines=True, first_sp=True):

        self.element = element
        self.low_w = low_w
        self.upper_w = upper_w
        self.data_frame = pd.DataFrame()

        self.retrieve_data()

        self.clean_intensity()

        if strongLines:
            self.filter_strong_lines()

        self.filter_nan_values()
        self.reset_index()
        self.filter_columns()

        if first_sp:
            self.filter_sp()

    def retrieve_data(self):
        site = "https://physics.nist.gov/cgi-bin/ASD/lines1.pl?spectra={}&limits_type=0&low_w={}&upp_w={}&unit=1&submit=Retrieve+Data&de=0&format=3&line_out=0&remove_js=on&en_unit=0&output=0&bibrefs=1&page_size=15&show_obs_wl=1&show_calc_wl=1&unc_out=1&order_out=0&max_low_enrg=&show_av=2&max_upp_enrg=&tsb_value=0&min_str=&A_out=1&intens_out=on&max_str=&allowed_out=1&forbid_out=1&min_accur=&min_intens=&conf_out=on&term_out=on&enrg_out=on&J_out=on"
        site = site.format(self.element, self.low_w, self.upper_w)
        respond = requests.get(site)
        soup = BeautifulSoup(respond.content, 'lxml')
        html_data = soup.get_text()
        html_data = html_data.replace('"', "")
        data = io.StringIO(html_data)
        self.data_frame = pd.read_csv(data, sep="\t")

    def clean_intensity(self):

        for i in range(len(self.data_frame['intens'])):
            self.data_frame['intens'].iloc[i] = re.sub('[^0-9]', '', str(self.data_frame['intens'].iloc[i]))

        self.data_frame = self.data_frame[self.data_frame['intens'] != '']
        self.data_frame['intens'] = pd.to_numeric(self.data_frame['intens'])

    def filter_strong_lines(self, value=10 ** 2):
        # strength line gA > 10**8
        self.data_frame = self.data_frame[self.data_frame['intens'] > value]

    def filter_nan_values(self, column='obs_wl_air(nm)'):
        self.data_frame = self.data_frame[self.data_frame[column] > 0]

    def reset_index(self):
        self.data_frame.reset_index(inplace=True, drop=True)

    def filter_columns(self):
        if self.element != 'H':
            self.data_frame = self.data_frame[['element', 'sp_num', 'obs_wl_air(nm)', 'intens', 'gA(s^-1)']]
        else:
            self.data_frame = self.data_frame[['obs_wl_air(nm)', 'intens', 'gA(s^-1)']]

    def filter_line(self, line, count):
        return pd.DataFrame(
            self.data_frame.iloc[(self.data_frame['obs_wl_air(nm)'] - line).abs().argsort()[:count]].sort_values(
                by=['intens'], ascending=False).iloc[0]).transpose()

    def filter_sp(self, sp=1):
        self.data_frame = self.data_frame[self.data_frame['sp_num'] == 1]


if __name__ == '__main__':
    line = Lines_LIBS('Ar', 200, 940, strongLines=False, first_sp=False)
    print(line.data_frame)