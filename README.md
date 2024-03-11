# cecs-327-project-1
CECS 327 | Project 1 | Group 17 | A Bite of Distributed Communication

Huy Vu - 018494734
Kevin Tran - 029589454
Daniel Neri - 025500083

March 6Dth, 2024

Setup steps:
1. Download Docker
2. Ensure WSL2 is set up for docker (if you're using it)
3. Complete setup and sign out
4. In WSL2 or terminal, ~$ sudo usermod -aG docker $USER
5. To verify if it worked: ~$ getent group docker ---- ~$ getent group sudo
6. ~$ docker network create -d bridge Proj1-distributed-network
7. Run the YAML docker file: ~$ docker-compose build ---- ~$ docker-compose up

(if 4-5 doesn't work, ~$ newgrp docker (right after 4))


To run the program:
1. cd into the current working directory
2. run the command 'docker-compose up --build'
NOTE: Docker is required to be open in the background for the commands to work properly
