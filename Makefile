NAME=python-for-datascience
all: up

up:
	docker-compose up -d --build

down:
	docker-compose down

exec:
	docker exec -it ${NAME}-app-1 /bin/bash

rm-none:
	docker rmi $$(docker images -f "dangling=true" -q)

rm-volumes:
	-docker volume rm $(docker volume ls -qf "dangling=true")

rmi:
	-docker image rm $$(docker image ls -q "${NAME}*")

clean: down rmi

fclean: clean rm-none rm-volumes