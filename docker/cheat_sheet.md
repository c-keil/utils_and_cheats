# Docker Workflow
- The docker hierarchy is docer files > docker images > docker conrainers.
- Multiple containers identified with different ids and names can be made from 1 image
- When a container stops, by default it still exits and can be run again with the existing changes
- a container will exit as soon as the command stops

## Tips
- In an interactive docker session, `exit` will kill the container
- To leave an attached container without killing it, use `ctrl-p ctrl-q`
- `docker ps -a` is useful for seeing all containers
- to see all images use `docker image ls -a`

# Docker run
To initiate a container the syntax is:
```
docker container run [options] $image_name(ir id) [command to run] [args]
```
Useful variants include, to start with an interactive trminal with name test name
```
docker container run -it --name test_name $image_id(or name) /bin/bash
```
The `/bin/bash` is the command to run.
Alternatively:
```
docker container run -d $image_id [command]
```
Will start a detached image.

# Docker Checkpoint
Note, checkpoint is an experimental feature, it does not work on some linux kernel version.
The syntax is:
```
docker checkpoint create [OPTIONS] CONTAINER CHECKPOINT
```
Note the `--leave-running=false` option.
To resume:
```
docker start --checkpoint CHECKPOINT_ID [OTHER OPTIONS] CONTAINER
```

To enable checkpointing, you need to install [criu](https://launchpad.net/~criu/+archive/ubuntu/ppa) and add a file to enable experimental features:
Filename: `/etc/docker/daemon.json`
Contents:
```
{
"experimental": true
}
```