FROM continuumio/miniconda3:latest

ENV APP_HOME=/app
WORKDIR ${APP_HOME}
COPY api ./
RUN conda env update --file environment.yml --name base --prune && \
    groupadd --system app && \
    useradd -g app --system app && \
    chown -R app:app ${APP_HOME} && \
    chmod -R 755 ${APP_HOME}
USER app
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "fastapi_api:app", "--bind", "0.0.0.0:6781", "--log-level", "INFO"]