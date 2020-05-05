# remove noname images
docker rmi $(docker images -f 'dangling=true' -q)

# remove unused volumes
docker volume prune
