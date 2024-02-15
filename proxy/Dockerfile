FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/templates/default.conf.template

EXPOSE 7000

CMD ["nginx", "-g", "daemon off;"]