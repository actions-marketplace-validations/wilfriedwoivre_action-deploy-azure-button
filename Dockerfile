FROM python:3.8-alpine

LABEL version="0.1.0"

LABEL maintainer="Wilfried Woivré <wilfried.woivre@gmail.com>"

LABEL "com.github.actions.name"="Deploy to Azure Button"
LABEL "com.github.actions.description"="Add deploy to Azure button to your markdown file"
LABEL "com.github.actions.actions.icon"="activity"
LABEL "com.github.actions.color"="blue"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
RUN ls -l
RUN chmod +x generator.py
RUN ls -l
RUN cat generator.py

CMD python /usr/src/app/generator.py