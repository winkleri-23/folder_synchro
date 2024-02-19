# Test task: Folder synchronization program

This program was implemented as a part of the recruitment process for the developer position. 

## Assignment

This program synchronizes two folders - a source folder and a replica folder - to maintain an identical copy of the source folder in the replica folder. The synchronization is one-way, ensuring that the content of the replica folder is modified to exactly match the content of the source folder.

## Features
- One-way synchronization: after the synchronization content of the replica folder should be modified to exactly match the content of the source folder
- Periodic synchronization: Synchronization is performed at specified intervals.
- Logging: File creation, copying, and removal operations are logged to both the console output and a log file.
- Command line arguments: Folder paths, synchronization interval, and log file path are provided as command line arguments.

## Usage

### Command Line Arguments
`source_path`: Path to the source folder.
`replica_path`: Path to the replica folder.
`log_file`: Path to the log file.
`interval_seconds`: Synchronization interval in seconds.

### Example 
`python synchronize.py ./src_folder ./replica_folder ./logfile.txt 10`

### Docker 
Besides running the program locally, you can also run it in a docker container. The docker can be started 
by `docker compose up` command. The program will be executed with the default arguments. Then you can 
access the container by `docker exec -it <container_id> bash` and modify directories `src_folder` and `replica_folder`.
The synchronization period is set to 10 seconds. 
