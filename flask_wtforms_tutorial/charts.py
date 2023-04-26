
import requests
from asyncio.log import logger
from cmath import log
from datetime import datetime
from datetime import date
import pygal


#Helper function for converting date
def convert_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()

def Query(symbol, chart_type, time_series, start_date, end_date):
    dateKeyList = []
    openValues = []
    highValues = []
    lowValues = []
    closeValues = []

    if chart_type == "1":
        chart = pygal.Bar()
    else:
        chart = pygal.Line()
    chart.title = 'Stock Data for ' + symbol + ': ' + str(start_date) + ' to ' + str(end_date)
    if time_series == "1":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+symbol+'&interval=60min&outputsize=full&apikey=TBV7EY1WFDG25BLY'
    elif time_series == "2":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+symbol+'&outputsize=full&apikey=TBV7EY1WFDG25BLY'
    elif time_series == "3":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+symbol+'&outputsize=full&apikey=TBV7EY1WFDG25BLY'
    else:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='+symbol+'&outputsize=full&apikey=TBV7EY1WFDG25BLY'
    r = requests.get(url)
    data = r.json()
    data.pop('Meta Data')
    dateList = data.values()
    for dictionary in dateList:
        for dateKey in dictionary:
            if time_series == "1":
                dateKey_dt = datetime.strptime(dateKey, "%Y-%m-%d %H:%M:%S")
            else:
                dateKey_dt = datetime.strptime(dateKey, "%Y-%m-%d")
            
            if start_date <= dateKey_dt.date() <= end_date:  
                dateKeyList.append(dateKey)
                openValues.append(float(dictionary[dateKey]['1. open']))
                highValues.append(float(dictionary[dateKey]['2. high']))
                lowValues.append(float(dictionary[dateKey]['3. low']))
                closeValues.append(float(dictionary[dateKey]['4. close']))
    dateKeyList.reverse()
    openValues.reverse()
    highValues.reverse()
    lowValues.reverse()
    closeValues.reverse()
    chart.x_labels = map(str, dateKeyList)
    chart.add('Open', openValues)
    chart.add('High',  highValues)
    chart.add('Low',      lowValues)
    chart.add('Close',  closeValues)
    chart.render_in_browser()
    return chart.render_data_uri()


