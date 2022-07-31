const ROUTES = [
    {
        url: '/traefik',
        auth: false,
        creditCheck: false,
        proxy: {
            target: "http://link-traefik:80",
            changeOrigin: true,
            pathRewrite: {
                [`^/traefik`]: '',
            },
        }
    }
]

exports.ROUTES = ROUTES;
