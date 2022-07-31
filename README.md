# node-express-traefik
Play area for using node express and traefik as a gateway

This project is all dockerised, and can be set up using
```
# in services
docker-compose build
docker-compose up
```

The services brough up consist of
- a simple python app with hello endpoints
- another simple python app with hola endpoints
- a traefik app for routing
- a node express app for exposure

The set up allows users to query the node express app, which then routes to the traefik app, which in turn routes individually to each of the Python apps.

The node express app can be queried using
```
# purely to node express
curl http://localhost:3000/hello-world
# to node express, then traefik, and then python hello
curl http://localhost:3000/traefik/api-hello/hello
curl http://localhost:3000/traefik/api-hello/sub-path/goodbye
# to node express, then traefik, and then python hola
curl http://localhost:3000/traefik/api-hola/hola
curl http://localhost:3000/traefik/api-hola/sub-path/adios
```

The state of traefik routing can be seen on
```
http://localhost:8080/dashboard/#/
```