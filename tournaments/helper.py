from pytz import timezone
import pytz
from datetime import datetime
import re


def parse_jpn_date(jpn_date_str: str, starts_at: str) -> datetime:
    """

    Parameters
    ----------
    jpn_date_str
    starts_at

    Returns
    -------
    datetime
        datetime in UTC timezone
    """

    match = re.match(r"(\d+)月(\d+)日.*", jpn_date_str)
    time = starts_at.split(':')
    jst = timezone('Asia/Tokyo')

    return jst\
        .localize(match.group(1), match.group(2), 1, int(time[0]), int(time[1]))\
        .astimezone(pytz.utc)


def is_event_registered(service, calendar_id, event_id):
    """
    Confirm if event is already registered or not.

    Parameters
    ----------
    service
    calendar_id
    event_id

    Returns
    -------
    bool:
        Confirmation result of event id

    """
    events = service.events().list(
        calendarId=calendar_id, q=f"id={event_id}")

    return True if len(events['items']) > 0 else False
