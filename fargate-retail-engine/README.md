Example of OpenTelemetry for Microservices using a single Fargate Task

Environment variables must be in a file in S3- the Task shows the example location which should have:
* AWS credentials
* OpenTelemetry Collector address
* Splunk credentials if using Splunk Observability


Requires DynamoDB populated by the example `itemtable` data generator in the Tools directory

Start the Fargate task to enable the four example microservices.
