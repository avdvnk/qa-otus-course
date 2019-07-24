

class Logger:
    @staticmethod
    def write_logs(filename, log_info):
        try:
            with open(filename, "a") as log_file:
                log_file.write(log_info + "\n")
        except IOError as error:
            print(error)
