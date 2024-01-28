1. docker build -t can-communication-pi .
2. docker run --rm --privileged -v /dev:/dev --network host can-communication-pi
