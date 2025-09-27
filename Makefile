NAME=python-for-datascience
all: up

up:
	docker-compose up -d --build

exec:
	docker exec -it ${NAME}-app-1 /bin/bash

rm-none:
	docker rmi $(docker images -f "dangling=true" -q)

rm-volumes:
	-docker volume rm $(docker volume ls -qf "dangling=true")

clean:
	docker-compose down --rmi $(docker image "${NAME}-*" -q)

fclean: clean rm-none