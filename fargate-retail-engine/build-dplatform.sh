sudo docker build . -f dockerfile-dplatform -t dplatform && \
sudo docker tag dplatform stevelerner/dplatform && \
sudo docker push stevelerner/dplatform