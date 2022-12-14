#!make

cnf ?= config.env
include $(cnf)

build:  ## Build generic docker image witout configuration.
	docker build -t ping_bot:latest \
		     -f docker/Dockerfile .

build_arg:  ## Build docker image with configuration from config.env file.
	docker build -t ping_bot:latest \
		     --build-arg API_TOKEN=$(API_TOKEN) \
		     --build-arg REMOTE_IP=$(REMOTE_IP) \
		     -f docker/Dockerfile .

run:  ## Run docker container as is.
	docker run --name ping_bot -itd ping_bot:latest

run_arg:  ## Run docker container with configuration from config.env file.
	docker run --name ping_bot \
		   --env API_TOKEN=$(API_TOKEN) \
		   --env REMOTE_IP=$(REMOTE_IP) \
		   -itd ping_bot:latest

stop:  ## Stop docker container (container will be killed)
	docker rm --force ping_bot

.PHONY: build build_arg run run_arg stop help
help: ## Display this help screen
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
