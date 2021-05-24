# export OTEL_EXPORTER_OTLP_ENDPOINT=http://127.0.0.1:4317
export OTEL_RESOURCE_ATTRIBUTES=service.name=catalog,deployment.environment=aws-demo
# ensure path is correct
export PATH="$HOME/.local/bin:$PATH"
splk-py-trace python3 01-server.py