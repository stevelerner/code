export OTEL_SERVICE_NAME='db'
export OTEL_TRACES_EXPORTER='jaeger-thrift-splunk'
export OTEL_EXPORTER_JAEGER_ENDPOINT='http://${SMART_AGENT}:9080/v1/trace'
export OTEL_RESOURCE_ATTRIBUTES='deployment.environment=prod'