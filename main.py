import os
import datetime as dt
import calendar
import requests
from dotenv import load_dotenv
import plotly
import plotly.plotly as py
import plotly.graph_objs as go


def get_news_feed(q, start_time, end_time):
    api_url = "https://api.vk.com/method/newsfeed.search"
    params = {
        "access_token": os.getenv("access_token"),
        "v": 5.92,
        "q": q,
        "start_time": start_time,
        "end_time": end_time
    }
    response = requests.post(api_url, data=params)
    return response.json()['response']


def generate_days_timestamps():
    days_before = []
    today = dt.datetime.utcnow()
    midnight = dt.time(0)
    today = dt.datetime.combine(today, midnight)
    for i in range(0, 7):
        yesterday = today - dt.timedelta(days=1)
        today_timestamp = calendar.timegm(today.utctimetuple())
        yesterday_timestamp = calendar.timegm(yesterday.utctimetuple())
        days_before.append((today.date(), today_timestamp, yesterday_timestamp))
        today = yesterday
    return days_before


def get_statistics(key_phraze, days):
    statistics = []
    for date, end_date, start_date in days:
        data = get_news_feed(key_phraze, start_date, end_date)
        statistics.append((date, data['count']))
    return statistics


def generate_plot(title, labels, values):
    data = [go.Bar(
        x=labels,
        y=values
    )]
    layout = {
        "title": title
    }
    py.plot({"data": data, "layout": layout}, filename='basic-line', auto_open=False)


if __name__ == '__main__':
    load_dotenv()
    plotly.tools.set_credentials_file(username=os.getenv("login"), api_key=os.getenv("api_key"))
    last_seven_days = generate_days_timestamps()
    statistics_data = get_statistics("Coca-cola", last_seven_days)
    print("Статистика собрана!")
    data_for_plot = list(zip(*statistics_data))
    generate_plot("График упоминаний Coca-cola в ВК", *data_for_plot)




