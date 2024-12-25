FROM androidhub.wps.kingsoft.net/common/python:3.10.14

WORKDIR /code

ENV TZ=Asia/Shanghai

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt -i https://mirrors.wps.cn/pypi/simple/

COPY . /code

CMD ["python", "main.py"]