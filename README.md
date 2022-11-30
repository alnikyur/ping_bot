# Ping bot
<p align="center">
<img width="200" height="200" src="https://raw.githubusercontent.com/alnikyur/ping_bot/main/img/img.png">
<p/>

[Link to Git-hub](https://github.com/alnikyur/ping_bot) of this repo  

This tlegram bot can be useful to check status of any device through IPv4 protocol.  
For example, You can use this bot to check status of electricity in your home/office.

## Prerequisites

You have to run this bot on 24/7 environment with full access to internet network.  
For example you can use `AWS cloud` EC2 machine or `Hetzner` dedicated servers to run this bot.  
Also you can run it on baremetal, raspberry-pi or anywere you want.  

## How to using bot

1. First of all you have to ger `API_TOKEN` from telegram api. Please use [official documentaion](https://core.telegram.org/bots/faq#how-do-i-create-a-bot) to get `API_TOKEN`.
2. If you want to check availability of your home/office router the last one should have static IP address.  
Or you can use `DynamicDNS` service or any other dyndns-like services. In this case you have to use your `FQDN` record in `REMOTE_IP` variable instead IP address.
3. Build docker container:  
```
docker build -t <container_name> \
             --build-arg API_TOKEN=<your_api_token> \
             --build-arg REMOTE_IP=<destination_ip_address> \
             -f docker/Dockerfile .
```

Or build docker image without `API_TOKEN` and `REMOTE_IP`

```
docker build -t ping_bot -f docker/Dockerfile .
```

3. Run your docker image:
```
docker run --restart=always -itd <docker_image_name>
```

You can also pass `API_TOKEN` and `REMOTE_IP` environment variables with `docker run` option, for example:
```
docker run --name <container_name> \
           --env API_TOKEN=<your_api_token> \
           --env REMOTE_IP=<destination_ip_address> \
           -itd <docker_image_name>
```

When all configurations is done and bot us up you can check it by taping `/start` command in your telegram bot.
