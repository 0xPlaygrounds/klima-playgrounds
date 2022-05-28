# klima-playgrounds
Deployment of Playgrounds application for KlimaDAO

# CI/CD Setup

Opening a pull request will automatically trigger a GitHub Actions pipeline to lint and smoketest your changes.

Changes merged to the following branches will be deployed to the corresponding URLs:
- `staging` => https://staging-klima.playgrounds.academy
- `main` => https://klima.playgrounds.academy

Please make sure you always open a PR when merging to either `staging` or `main` on the primary repo, so you can be
sure that your changes pass the lint and smoketest before merging them onto a deployed branch.

We require basic flake8 linting style to be adhered to in all Python code, or else the linter check will fail.

# Local Development with Docker

To run a local development environment using Docker, follow these steps.

1. `docker run -v $PWD:/usr/local/src -it -p 8050:8050 -w /usr/local/src python:3.10 bash`
2. `pip install -r requirements.txt`
3. `python -m src.index`

You should now be able to access your local development version of the site at
`http://localhost:8050`

_NOTE: since your local copy of the code is mounted in the container,_
_any changes will be automatically reflected when you reload the page._
