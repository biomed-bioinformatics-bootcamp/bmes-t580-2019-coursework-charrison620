import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')

def main():

    print_the_header()

    code = input("What zipcode do you want the weather (92701)? ")

    html = get_html_from_web(code)
    report = get_weather_from_html(html)

    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))



    #parse the HTML
    #display the forecast
    # print("Hello from main")


def print_the_header():
    print("--------------------------------")
    print("              WEATHER APP       ")
    print("--------------------------------")
    print()

def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    #print(response.status_code)
    #print(response.text[0:150])

    return response.text

def get_weather_from_html(html):
    cityCss = '.region-content-header h1'
    weatherConditionCss = '.condition-icon'
    weatherTempCss = '.wu-unit-temperature.wu-value'
    weatherScaleCss = '.wu-unit-temperature.wu-label'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_= 'region-content-header').find('h1').get_text()
    condition = soup.find(class_= 'condition-icon').get_text()
    temp = soup.find(class_= 'wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_= 'wu-unit-temperature').find(class_= 'wu-label').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_loc(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    #print(condition, temp, scale, loc)
    #return condition, temp, scale, loc
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report

def find_city_and_state_from_loc(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()

def cleanup_text(text):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()