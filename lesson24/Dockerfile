FROM selenium/standalone-firefox
RUN sudo apt update
RUN sudo apt-get install -y software-properties-common git \
python3-venv
RUN sudo apt-add-repository ppa:qameta/allure
RUN sudo apt-get update
RUN sudo apt-get install -y allure
RUN sudo mkdir /tests
RUN sudo chmod 777 /tests -R
RUN git clone https://github.com/avdvnk/qa-otus-course.git /tests
RUN cd /tests
RUN python3 -m venv /tests/venv
RUN cd venv/bin/
RUN ./python3 -m pip install -r ../../requirements