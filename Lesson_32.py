import psutil


class Test:
    def __init__(self):
        self.__process = None
        self.__cpu_count = None

    @property
    def process(self):
        if self.__process:
            return self.__process
        else:
            return 'There is no data'

    @property
    def cpu_count(self):
        if self.__cpu_count:
            return self.__cpu_count
        else:
            return 'There is no data'

    def get_process(self):
        self.__process = psutil.process_iter()

    def get_cpu(self):
        self.__cpu_count = psutil.cpu_count()
