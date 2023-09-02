import os, sys, time, psutil
from datetime import datetime

class LogMaker:
    def __init__(self, log_dir):
        self.log_dir = log_dir

class LogMakerTxt(LogMaker):
    def __init__(self, log_dir):
        super().__init__(log_dir)

    def LogFunction(self, function):
        script = sys.argv[0]
        function_name = None
        if callable(function):
            function_name = function.__name__ # param
        else:
            raise ValueError("Input is not a valid function")

        start_time = time.time()
        start_datetime = datetime.fromtimestamp(start_time) # param

        try:
            returned = function() # param
            result = "succeed" # param
            success = True # param
            error_msg = None # param
        except Exception as e:
            result = "failed" # param
            success = False # param
            error_msg = str(e) # param

        end_time = time.time()
        end_datetime = datetime.fromtimestamp(end_time)
        runtime = end_time - start_time # param

        cpu_percent = psutil.cpu_percent(interval=1) # param
        memory_percent = psutil.virtual_memory().percent # param
        network_io = psutil.net_io_counters() # param

        log_content = f"""
=======================================================

 ____ ____ ____  __  _  _ ____  ___ ____ ____  __ _  _ 
(  _ (  __/ ___)/  \/ )( (  _ \/ __(  __(  _ \/  ( \/ )
 )   /) _)\___ (  O ) \/ ()   ( (__ ) _) ) _ (  O )  ( 
(__\_(____(____/\__/\____(__\_)\___(____(____/\__(_/\_)


======================= v1.0.0 =======================

script: {script}
function: {function_name}

runtime: {runtime:.2f} sec
Start time : {start_datetime}
End time : {end_datetime}

result: {result}
error: {error_msg}

Total CPU usage: {cpu_percent}%
Total Memory usage: {memory_percent}%

Network sent: {network_io.bytes_sent / (1024 * 1024):.2f} mb
Network received: {network_io.bytes_recv / (1024 * 1024):.2f} mb

Return : {returned}

===============================================
"""
        print_datetime = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        log_file_name = os.path.join(self.log_dir, f"{function_name}_{print_datetime}.txt")
        with open(log_file_name, "w") as log_file:
            log_file.write(log_content)


# Test
if __name__ == "__main__":
    def demo_function():
        for i in range(1000000):
            print("Hello, World!")

    log_dir = "resourcebox/logmaker/src/logs"
    logger = LogMakerTxt(log_dir)
    logger.LogFunction(demo_function)