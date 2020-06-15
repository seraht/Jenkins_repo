FROM python:3.6-jessie

WORKDIR /opt
ADD / /opt
ENV URL = $URL

ENTRYPOINT ["python", "-u", "/opt/get_html.py" ,"$URL"]
