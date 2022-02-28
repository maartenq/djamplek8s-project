FROM python:3.9 AS builder

ENV PACKAGE_NAME=djamplek8s
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv $VIRTUAL_ENV
COPY dist /opt/dist
RUN python3 -m pip install -U pip wheel
RUN python3 -m pip install -U $PACKAGE_NAME --find-links=/opt/dist

# Final image
FROM python:3.9-slim 
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
CMD ["/app/entrypoint.sh"]
