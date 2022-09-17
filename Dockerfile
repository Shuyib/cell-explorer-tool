# Use latest Python runtime as a parent image
FROM python:3.8.13-slim-buster

# Meta-data
LABEL maintainer="Shuyib" \
      description="An image editing and annotation tool. It is focused on lab setting."
      
# Set the working directory to /app
WORKDIR /app

# ensures that the python output is sent to the terminal without buffering
ENV PYTHONUNBUFFERED=TRUE

# Copy the current directory contents into the container at /app
COPY . /app

# create a virtual environment and activate it
RUN python3 -m venv cell-exp

# activate virtual environment
CMD source cell-exp/bin/activate

# Install the required libraries
RUN pip --no-cache-dir install --upgrade pip &&\
		pip --no-cache-dir install -r requirements.txt

# Make port 1111 available to the world outside this container
EXPOSE 2323

# Create mountpoint
VOLUME /app

# Run jupyter when container launches
CMD ["jupyter", "notebook", "--ip='*'", "--port=1111", "--no-browser", "--allow-root"]
