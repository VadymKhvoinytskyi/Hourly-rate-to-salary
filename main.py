import datetime
import pandas
import json


def get_config_file(filename) -> dict:
    with open(filename, 'r', encoding='UTF-8') as input_file:
        data = json.load(input_file)
    return data


def calculate_earned_totally(data) -> float:

    def get_start_date(data):
        start_year = data['start_year']
        start_month = data['start_month']
        start_day = data['start_day']
        start = datetime.date(start_year, start_month, start_day)
        return start

    def get_end_date(data):
        end_year = data['end_year']
        end_month = data['end_month']
        end_day = data['end_day']
        end = datetime.date(end_year, end_month, end_day)
        return end

    def get_hourly_rate(data) -> float:
        hourly_rate = 0
        if data['hourly_rate'] > 0:
            hourly_rate = data['hourly_rate']
        else:
            raise 'Hourly rate is not defined'
        return hourly_rate

    start = get_start_date(data)
    end = get_end_date(data)
    start_weekday = start.weekday()
    hourly_rate = get_hourly_rate(data)

    earned_totally = 0
    work_period = pandas.date_range(start, end)
    for i, work_day in enumerate(work_period, start=start_weekday):
        weekday = i % 7
        day_hours = data['weekday'][str(weekday)]['hours']
        earned_totally += day_hours * hourly_rate
    return earned_totally - data['missed_hours'] * hourly_rate


def get_payment_remaining(earned_totally, data) -> float:
    return earned_totally - data['paid']


def create_output_dict(currency, earned_totally, paid, payment_remaining):
    pass
    # return output_dict


def push_to_json(filename, dict):
    pass


def main() -> None:
    data = get_config_file('rate-schedule.json')
    earned_totally = calculate_earned_totally(data)
    payment_remaining = get_payment_remaining(earned_totally, data)
    # print('Earned totally', earned_totally, data['currency'])
    print('Payment remaining', payment_remaining, data['currency'])


if __name__ == '__main__':
    main()

