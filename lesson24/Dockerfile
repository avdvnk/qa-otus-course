FROM selenium/standalone-firefox
RUN sudo apt update
RUN sudo apt-get install -y software-properties-common git \
python3-venv
RUN sudo apt-add-repository ppa:qameta/allure
RUN sudo apt-get update
RUN sudo apt-get install -y allure
RUN cd /home/seluser
RUN mkdir tests
RUN cd tests/
RUN git clone https://github.com/avdvnk/qa-otus-course.git
RUN python3 -m venv ./venv
RUN cd venv/bin/
RUN ./python3 -m pip install -r ../../requirements