## DOCKER PYTHON


### Init

#### Image build
```
docker build -t python-docker -f dockerfile .
```

#### start
```
docker run -d -p 5000:5000 --name pyton-teste python-docker:latest
```
