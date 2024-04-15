FROM python

RUN apt update &&\
    apt install -y sudo chromium chromium-driver

RUN pip3 install selenium webdriver-manager
WORKDIR /app

CMD ["python3", "sign.py"]
