# logmaker
logmaker for python functions

# about
This module is for resource management and performance analysis.
This checks the used resources during the funtion's runtime,
and you can create some log files with .txt or .csv.

# requirements
1. python >= v3.0.0

# install
``` bash
$ pip install logmaker
```

# usage
``` python
# import modules
from logmaker import logmaker

# to make txt log file
logger_txt = logmaker.LogmakerTxt(log_dir ='<txt_file_dir>')
logger_txt.LogFunction(function=<function_you_want_to_monitor>)

# to make csv log data
logger_csv = logmaker.LogmakerCsv(csv_dir='<csv_file_dir>')
logger_csv.LogFunction(duration=0.2, function=<function_you_want_to_monitor>)
```

# demo files
### .txt
```

=======================================================
       __                             _             
      / /  ___   __ _ _ __ ___   __ _| | _____ _ __ 
     / /  / _ \ / _` | '_ ` _ \ / _` | |/ / _ | '__|
    / /__| (_) | (_| | | | | | | (_| |   |  __| |   
    \____/\___/ \__, |_| |_| |_|\__,_|_|\_\___|_|   
                |___/                               
======================= v1.0.0 =======================

script: /Users/kimdohoon/git/resourcebox/logmaker/src/logmaker_func.py
function: demo_function

runtime: 9.60 sec
Start time : 2023-09-06 00:25:46.390970
End time : 2023-09-06 00:25:55.990559

result: succeed
error: None

Total CPU usage: 11.3%
Total Memory usage: 78.8%

Network sent: 1395.44 mb
Network received: 2093.69 mb

Return : None

===============================================

```

### .csv
```
Timestamp,CPU (%),Memory (%),Network (bytes_sent),Network (bytes_recv)
2023-09-05 19:16:11.791257,0.0,67.9,1357989888,4210591744
2023-09-05 19:16:11.996423,0.0,67.9,1357989888,4210591744
2023-09-05 19:16:12.201739,0.0,68.0,1357989888,4210591744
2023-09-05 19:16:12.407050,0.0,67.9,1357989888,4210591744
2023-09-05 19:16:12.612306,0.0,67.9,1357989888,4210591744
2023-09-05 19:16:12.813519,56.5,67.9,1357989888,4210591744
```