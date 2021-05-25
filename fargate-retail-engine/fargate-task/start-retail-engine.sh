aws ecs create-service \
--cluster YOURCLUSTERHERE \
--service-name retail-engine \
--task-definition retail-engine:1 \
--desired-count 1 --launch-type "FARGATE" \
--network-configuration \
"awsvpcConfiguration={subnets=[subnet-YOURSUBNETHERE],securityGroups=[sg-YOURSGHERE],assignPublicIp=ENABLED}"