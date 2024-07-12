from nginx:latest

# run --mount=type=bind,source=frontend,target=/usr/share/nginx/html

copy frontend/index.html /usr/share/nginx/html/index.html

expose 80/tcp

cmd ["nginx", "-g", "daemon off;"]