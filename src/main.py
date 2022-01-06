import sys
import os
import re
import datetime as dt
from ticktick.oauth2 import OAuth2        # OAuth2 Manager
from ticktick.api import TickTickClient   # Main Interface
from dotenv import load_dotenv


def add_countdown_timer(title='(Anonymous Countdown Task)', time_string='300s'):
    """Add Countdown Timer

    Args:
        title (str, optional): Task title. Defaults to '(Anonymous Countdown Task)'.
        time_string (str, optional): Time string (5m3s, 0.5m, 30). Defaults to '300s'.
    """
    p = re.compile(r'((?P<minutes>\d+(\.\d+)?)m)?((?P<seconds>\d+(\.\d+)?))?')
    m = p.match(time_string)
    opt_minutes = m.group('minutes')
    opt_seconds = m.group('seconds')
    seconds = 0
    if opt_minutes:
        opt_minutes
        seconds += 60 * float(opt_minutes)
    if opt_seconds:
        seconds += float(opt_seconds)

    t = dt.datetime.now() + dt.timedelta(seconds=seconds)
    task = client.task.builder(
        title, reminders=['PT0S'], startDate=t, dueDate=t)
    client.task.create(task)


if __name__ == '__main__':
    load_dotenv()
    client_id = os.environ.get('TICKTICK_CLIENT_ID')
    client_secret = os.environ.get('TICKTICK_CLIENT_SECRET')
    uri = os.environ.get('TICKTICK_REDIRECT_URL', 'http://127.0.0.1:8080')
    username = os.environ.get('TICKTICK_USERNAME')
    password = os.environ.get('TICKTICK_PASSWORD')

    auth_client = OAuth2(client_id=client_id,
                         client_secret=client_secret,
                         redirect_uri=uri)

    client = TickTickClient(username, password, auth_client)

    if len(sys.argv) == 2:
        add_countdown_timer(time_string=sys.argv[1])
    elif len(sys.argv) == 3:
        add_countdown_timer(title=sys.argv[1], time_string=sys.argv[2])
