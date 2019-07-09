import datetime


class MyLogger:

    @staticmethod
    def write_to_file(filename, info, log_time):
        with open(filename, "a") as file:
            file.write("{}:{}\n".format(log_time, info))

    @staticmethod
    def get_datetime():
        time = datetime.datetime.now()
        result = "{} {}.{}.{}".format(time.date(), time.hour, time.minute, time.second)
        return result
