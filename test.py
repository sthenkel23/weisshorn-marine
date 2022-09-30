s="2022-09-21 21:21:32.703091"
from datetime import date, datetime


date_time_str = '2018-06-29 08:15:27.243860'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')


def transform_time(date: str) -> datetime.date:
    
    """_summary_

    :return: _description_
    :rtype: _type_
    """
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M')


doc = transform_time(date_time_str)

print(doc)