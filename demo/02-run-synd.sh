# export OTEL_EXPORTER_OTLP_ENDPOINT=http://127.0.0.1:4317
# set up OTEL env variables
export OTEL_RESOURCE_ATTRIBUTES=service.name=shopping-engine,deployment.environment=aws-demo
# ensure path is correct
export PATH="$HOME/.local/bin:$PATH"
splk-py-trace python3 02-synd.py