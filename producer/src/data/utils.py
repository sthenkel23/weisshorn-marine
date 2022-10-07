from datetime import datetime


def transform_time(date: str) -> datetime.date:
    
    """_summary_

    :return: _description_
    :rtype: _type_
    """
    
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M')
