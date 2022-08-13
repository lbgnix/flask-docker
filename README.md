# python-flask-docker
Basic Python Flask app in Docker which prints the hostname and IP of the container and Application Version with background Color, this app is create for Kubernetes HPA testing

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/lbgnix/flask-docker.git
$ docker build -t flask-docker-test .
```

### Download precreated image
You can also just download the existing image from [DockerHub](https://hub.docker.com/r/lalbahadurv/flask-docker).
```
docker pull lalbahadurv/flask-docker:v2
```

### Run the container
Create a container from the image.
```
$ docker run --name my-container -d -p 8080:8080  lalbahadurv/flask-docker
```

Now visit http://localhost:8080
```
 The hostname of the container is 6095273a4e9b and its IP is 172.17.0.2. 
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-container
172.17.0.2
$ docker inspect -f '{{ .Config.Hostname }}' my-container
6095273a4e9b
```


