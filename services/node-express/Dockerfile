FROM docker.io/node:latest

WORKDIR app
RUN npm install express morgan http-proxy-middleware
COPY ./api/ ./api/

CMD ["node", "./api/app.js"]