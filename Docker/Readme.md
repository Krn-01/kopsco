## Docker Containers

### Usefull Commands
```
docker build -t <app-name> .
docker run -p 8080:80 <app-name> [-d (Run in Detach mode)]


# Debugging Command
docker images       [List the Images]
docker ps           [Check the running process]
docker inspect      [Get detailed info about image]


-q  [Output only ID]

```