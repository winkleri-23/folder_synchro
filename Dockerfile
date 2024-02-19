# Use a base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY synchronize.py .

# Install any dependencies
RUN pip install requests

# Run the script with command line arguments
RUN mkdir src_folder
RUN mkdir replica_folder
RUN echo "Hello, World!" > src_folder/hello.txt

CMD ["python3", "synchronize.py", "./src_folder", "./replica_folder", "./logfile.txt", "10"]