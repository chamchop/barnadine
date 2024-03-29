import pandas as pd
import requests

def get_ons_gdp():
    url = "https://www.ons.gov.uk/economy/grossdomesticproductgdp/timeseries/ihyq/qna"
    response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    df = pd.read_html(response.content)
    table = df[1]
    data = table.loc[:, ['Period', 'Value']]
    print(data)
    return data