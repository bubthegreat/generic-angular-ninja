FROM node:14.15.4 as build

RUN npm install
RUN npm install -g @angular/cli@11.0.7

WORKDIR /app
COPY skill_matrix_app /app

RUN ng build --output-path=dist --base-href=/app/

FROM nginx:1.16.0-alpine

COPY --from=build /app/dist /usr/share/nginx/html/app
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
