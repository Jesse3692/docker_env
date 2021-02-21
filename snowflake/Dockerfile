FROM python:3.6.13-alpine

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && apk update
RUN apk add tzdata && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
RUN pip install pysnowflake -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD snowflake_start_server \
    --address=0.0.0.0\
    --port=8910 \
    --dc=1 \
    --worker=1 \
    --log_file_prefix=/opt/logs/pysnowflask.log