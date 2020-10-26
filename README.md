# Bag Pzrocesser

## Execution
### 1.Build image
Run command

`dts devel build -f `

### 2.Run container with mounted volume

Run command

`docker run -it -v <path_to_bagfile>:/data/ duckietown/duckietown_bagprocesser:v2-amd64`

Replace `<path_to_bagfile>` with the absolute directory to where the bagfile you want to process is stored. The new bagfile named "processed_bag.bag" will be stored at the same folder.

### 3.Play the processed bagfile on duckiebot

#### Build communication between your PC and duckiebot using ROS
Run command

`docker run -it --net host -e ROS_MASTER_URI=http://<host_ip>:11311/ -e ROS_IP=<duckiebot_ip> -v <path_to_bagfile>:/home duckietown/dt-ros-commons:daffy-amd64 /bin/bash`

Replace `<host_ip>` and `<duckiebot_ip>` with the IP address of your PC and your duckiebot. You can check the IP address with command `ifconfig`. The `<path_to_bagfile>` should be replaced with the same directory you used to mount and store the bagfiles.

#### Play bagfile
Move to the container directory that you mounted the volume, with command `cd /home` in this case.

Run command

`rosbag play processed_bag.bag --loop /<MY_ROBOT>/camera_node/image/compressed:=/new_image/compressed`

Replace <MY_ROBOT> with the name of your duckiebot.
