# Docker image names and versions
IMAGE_NAME := oculus_dei
IMAGE_VERSION := 1.0

# Docker build command
DOCKER_BUILD := docker build

# Docker build options
DOCKER_BUILD_FLAGS := --rm

# Docker tag command
DOCKER_TAG := docker tag

# Docker push command
DOCKER_PUSH := docker push

# Location for the venv
VENV_PATH :=

# Build the Docker image
.PHONY: build
build:
	@echo "Building Docker image..."
	$(DOCKER_BUILD) $(DOCKER_BUILD_FLAGS) -t $(IMAGE_NAME):$(IMAGE_VERSION) .

# Tag the Docker image with a specific version
.PHONY: tag
tag:
	@echo "Tagging Docker image..."
	$(DOCKER_TAG) $(IMAGE_NAME):$(IMAGE_VERSION) $(IMAGE_NAME):latest

# Push the Docker image to a registry
.PHONY: push
push:
	@echo "Pushing Docker image..."
	$(DOCKER_PUSH) $(IMAGE_NAME):$(IMAGE_VERSION)

# Clean up Docker images and containers
.PHONY: clean
clean:
	@echo "Cleaning up Docker images and containers..."
	docker container prune -f
	docker image prune -f