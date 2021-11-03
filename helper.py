from datetime import datetime
import uuid
from Constants import date_format
import os;

def get_time_from_string(timestr):
        return datetime.strptime(timestr, date_format)

def create_random_file_name(filename ):
        return ''.join([str(uuid.uuid4().hex[:8]), filename])

def get_time_in_string(timestamp :datetime):
        return timestamp.strftime(date_format)

def get_current_timestamp_in_string():
        return get_time_in_string(datetime.now())    
