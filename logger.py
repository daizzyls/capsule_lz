import getpass
import os
from datetime import datetime
from functools import wraps

import pandas as pd


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        pc_username = getpass.getuser()
        function_name = func.__name__ 

        now = datetime.now()  
        date = now.strftime("%d.%m.%Y")
        time = now.strftime("%H:%M:%S")

        log_file = "logs.csv"  
        next_id = 1 

        if os.path.isfile(log_file) and os.path.getsize(log_file) > 0: 
            df= pd.read_csv(log_file)  
            if 'id' in df.columns and not df.empty: 
                next_id = df['id'].max() + 1  

        new_row = pd.DataFrame([{  
            'id': next_id,
            'pc_username': pc_username,
            'function_name': function_name,
            'Date': date,
            'Time': time
        }])

        if not os.path.isfile(log_file): 
            new_row.to_csv(log_file, index=False)  
        else:  
            new_row.to_csv(log_file, mode='a', header=False, index=False)

        return func(*args, **kwargs)

    return wrapper