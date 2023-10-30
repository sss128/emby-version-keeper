FROM python:3.12.0-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY . ./

ENTRYPOINT [ "python3", "emby_version_handler.py" ]
