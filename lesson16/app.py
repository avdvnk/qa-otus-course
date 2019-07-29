import sys

from lesson16.my_parser import MyParser

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Need all arguments")
        print("RUN EXAMPLE: python app.py <method> <input_dir> <output_file> <additional_arguments>")
        exit(1)
    method = sys.argv[1]
    input_dir = sys.argv[2]
    output_file = sys.argv[3]
    if method == "total_requests":
        MyParser.get_total_requests(input_dir, output_file)
    elif method == "top_ip":
        MyParser.get_top_ip(input_dir, output_file)
    elif method == "top_requests":
        request_type = sys.argv[4]
        MyParser.get_requests(request_type, input_dir, output_file)
    elif method == "top_long_requests":
        MyParser.get_long_requests(input_dir, output_file)
    elif method == "top_client_error":
        MyParser.get_client_error(input_dir, output_file)
    elif method == "top_server_error":
        MyParser.get_server_error(input_dir, output_file)
    else:
        print("UNSUPPORTED COMMAND")
        print("SUPPORTED COMMANDS: total_requests top_ip top_requests top_long top_client_error top_server_error")

