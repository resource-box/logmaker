from logmaker import logmaker

def demo_function():
    for i in range(1000000):
        print("Hello, World!")

log_dir = "resourcebox/logmaker/demo/logs"
logger_1 = logmaker.LogMakerTxt(log_dir=log_dir)

csv_dir = "resourcebox/logmaker/demo/logs"
logger_2 = logmaker.LogMakerCsv(csv_dir=csv_dir)

logger_2.LogFunction(0.2, demo_function)
# logger_1.LogFunction(demo_function)