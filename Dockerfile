# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# VEGETA-USERBOT
# CuteInspire


RUN git clone -b Vegeta-Userbot https://github.com/UserbotMaps/Hiroki-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/UserbotMaps/Hiroki-Userbot/Vegeta-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
