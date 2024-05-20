FROM node:lts AS build

LABEL maintainer="Arvind .A"
LABEL email="pingarvindforquestions@gmail.com"

WORKDIR /app

COPY . .

RUN npm install pnpm -g && \
    ls -la && \
    cd src/ui && \
    pnpm install && \
    pnpm collect

FROM python:3.10-slim AS dev

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY --from=build /app /app

WORKDIR /app

RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r /app/src/requirements.txt && \
    chmod +x /app/src/commands/run-prod.sh && \
    chmod +x /app/src/commands/docker-entrypoint.sh

FROM python:3.10-slim AS prod

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY --from=dev /app /app
COPY --from=dev /opt/venv /opt/venv

WORKDIR /app

ENTRYPOINT [ "/app/src/commands/docker-entrypoint.sh" ]
CMD ["/app/src/commands/run-prod.sh"]
