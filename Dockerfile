# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# HIROSHI-USERBOT
# CuteInspire
# VEGETA-USERBOT


RUN git clone -b Hiroshi-Userbot https://github.com/UserbotMaps/Hiroshi-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/UserbotMaps/Hiroshi-Userbot/Hiroshi-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
