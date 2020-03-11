FROM python:3-alpine

WORKDIR /chall
COPY . .
CMD ["./ctfnc", "prod"]