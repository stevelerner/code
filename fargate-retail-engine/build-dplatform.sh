sudo docker build . -f dockerbuild/dockerfile-dplatform -t dplatform && \
sudo docker tag dplatform stevelerner/dplatform && \
sudo docker push stevelerner/dplatform