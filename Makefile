cnf ?= config.env
include $(cnf)

build:
	docker build -t ping_bot:latest \
		     -f docker/Dockerfile .

build_arg:
	docker build -t ping_bot:latest \
		     --build-arg API_TOKEN=${API_TOKEN} \
		     --build-arg REMOTE_IP=${REMOTE_IP} \
		     -f docker/Dockerfile .

run:
	docker run --name ping_bot -itd ping_bot:latest

run_arg:
	docker run --name ping_bot \
		   --env API_TOKEN=${API_TOKEN} \
		   --env REMOTE_IP=${REMOTE_IP} \
		   -itd ping_bot:latest

stop:
	docker rm --force ping_bot
