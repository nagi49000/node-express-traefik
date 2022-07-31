/* app set up taken from https://medium.com/geekculture/create-an-api-gateway-using-nodejs-and-express-933d1ca23322 */
const express = require('express')
const app = express()
const port = 3000

/* logging set up */
const morgan = require("morgan");
app.use(morgan('combined'));

/* routing set up */
const routes = require("./routes").ROUTES;
const createProxyMiddleware = require('http-proxy-middleware').createProxyMiddleware;
routes.forEach(r => {
    app.use(r.url, createProxyMiddleware(r.proxy));
})

/* app definition */
app.get('/hello-world', (req, res) => {
    res.send('Hello World!')
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})
