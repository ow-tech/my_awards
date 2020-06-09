![license](https://img.shields.io/github/license/mashape/apistatus.svg)


## Name of Project
- My_Awards
    ##### Description
    - The website basically works in away that you can post your projects that you have done with their descriptions and also the live link to the projects that you have done throughout. Another User can rate the uploaded application and get average scores.
### Author
- Alex M. Barasa

## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)
- [Django]
- [Django-RESTful]

## Technologies & Languages

**Project management (Agile)** [https://www.pivotaltracker.com](url)

**Version control (Git)** [https://git-scm.com/](url)

**Version control (Python)** [https://www.python.org/](url)

# Installation and Setup

Clone the repository below

```
git clone https://github.com/ow-tech/my_awards.git
```

### Create and activate a virtual environment

    virtualenv venv --python=python3.6

    source venv/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

### Copy environment variable

    cp env.sample .env

### Load/refresh .environment variables

    source .env

## Running the application

```
python manage.py server
```


## Endpoints Available
 - update your available endpoints

| Method | Endpoint                        | Description                           | Roles         |
| ------ | ------------------------------- | ------------------------------------- | ------------  |
| POST   |        /auth/signup             | sign up a user                        | users         |
| POST   |        /auth/login              | log in  a user                        | users         |



## License

MIT