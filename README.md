# klima-playgrounds
Deployment of Playgrounds application for KlimaDAO

# Local Development with Docker

To run a local development environment using Docker, follow these steps.

1. `docker run -v $PWD:/usr/local/src -it -p 8050:8050 -w /usr/local/src python:3.10 bash`
2. `pip install -r requirements.txt`
3. `python src/index.py`

You should now be able to access your local development version of the site at
`http://localhost:8050`

_NOTE: since your local copy of the code is mounted in the container,_
_any changes will be automatically reflected when you reload the page._
