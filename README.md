# Ping bot

This tlegram bot can be useful to check status of any device through IPv4 protocol.  
For example, You can use this bot to check status of electricity in your home/office.

## Prerequisites

You have to run this bot on 24/7 environment with full access to internet network.  
For example you can use `AWS cloud` EC2 machine or `Hetzner` dedicated servers to run this bot.  
Also you can run it on baremetal, raspberry-pi or anywere you want.  

## How to using bot

1. First of all you have to ger `API_TOKEN` from telegram api. Please use [official documentaion](https://telegra.ph/Awesome-Telegram-Bot-11-11) to get `API_TOKEN`.
2. Build docker container:  
```
docker build -t <container_name> \ 
             --build-arg API_TOKEN=<your_api_token> \
             --build-arg ROUTER_IP=<destination_ip_address> .
```

3. Run your docker image:
```
docker run -itd <docker_image_name>
```

You can also build docker image without pass `API_TOKEN` and `ROUTER_IP` environment variables but use it with `docker run` option< for example:
```
docker run --name <container_name> \
           --env API_TOKEN=<your_api_token> \
           --env ROUTER_IP=<destination_ip_address> \
           -itd <docker_image_name>
```

When all configurations is done and bot us up you can check it by taping `/start` command in your telegram bot.

