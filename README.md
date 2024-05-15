# Calculapiz
Calculapiz is a service that performs calculations on demand.
The main objective of this service is to be used for practicing test automation skills.
The nearest plans are including features that allow to perform:
- API testing
- Data base testing
- Web UI testing

Service is build based on Flask web framework.
Releases will be uploaded to [Docker Hub](https://hub.docker.com/repository/docker/alexlitvino/calculapiz/).

## Running service
Download image locally. Specify required version in `<tagname>`:

    docker pull alexlitvino/calculapiz:<tagname>

Start container. `<LOCAL_MOUNTED_DIR>` - directory on your machine where file with statistics will be saved

    docker run --rm -p 5000:5000 -v <LOCAL_MOUNTED_DIR>:/calculapiz/data alexlitvino/calculapiz:<tagname>

Service will be available at [http://localhost:5000/](http://localhost:5000/)
