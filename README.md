[![Build Status](https://travis-ci.org/nadralia/iReporter_Api.svg?branch=data_structures)](https://travis-ci.org/nadralia/iReporter_Api)
[![Coverage Status](https://coveralls.io/repos/github/nadralia/iReporter_Api/badge.svg?branch=data_structures)](https://coveralls.io/github/nadralia/iReporter_Api?branch=data_structures)
[![Maintainability](https://api.codeclimate.com/v1/badges/4ebc197ca3dd76fa3ef7/maintainability)](https://codeclimate.com/github/nadralia/iReporter_Api/maintainability)

# iReporter_Api
Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.


## Features 
- Create a red-flag record
- Get all red-flag records
- Get a specific red-flag record.
- Edit a specific red-flag record.
- Delete a red-flag record.

## API Endpoints
| Methods | EndPoint                               | Functionality                                   |Access
| ------- | -------------------------------------- | ----------------------------------------------- |------
| POST    | /api/v1/auth/signup                    | Sign up a user                                  |PUBLIC
| POST    | /api/v1/auth/login                     | Login a user                                    |PUBLIC
| POST    | /api/v1/red-flags                      | Create a red-flag record a user                 |PRIVATE
| GET     | /api/v1/red-flags                      | Fetch all red-flag records.                     |PRIVATE
| GET     | /api/v1/red-flags/redflag_id           | Fetch a specific red-flag-record                |PRIVATE
| PATCH   | /api/v1/red-flags/redflag_id/location  | Edit the location of a specific red-flag record |PRIVATE
| PATCH   | /api/v1/red-flags/redflag_id/comment   | Edit the comment of a specific red-flag record  |PRIVATE
| DELETE  | /api/v1/red-flags/redflag_id           | Delete a specific red flag record.              |PRIVATE


**Getting started with the app**

### Technologies used to build the application
- `Python3` - A programming language that lets us work more quickly.
- `Flask` - A microframework for Python based on Werkzeug, Jinja 2 and good intentions.
- `Virtualenv` - A tool to create an isolated virtual environment.
- `Git` - Version Control System for tracking your changes.
### Installation

Create a new directory and initialize git in it. Clone this repository by running

```sh
git clone https://github.com/nadralia/iReporter_Api
```

Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using

```sh
virtualenv venv
```

Activate the virtual environment

```sh
cd venv/scripts/activate
```

Install the dependencies in the requirements.txt file using pip

```sh
pip install -r requirements.txt
```

Start the application by running

```sh
python run.py
```
## How to run tests

Enter the command below in the terminal to run the tests with coverage using
 pytest

```sh
  python -m pytest tests/
```
### Link to iReporter on Heroku

### [iReporter](https://nadralia-ireporter.herokuapp.com)

## Author

Adralia Nelson

## Acknowledgements

Big thanks to LFA's and fellow colleagues at [Andela](https://andela.com) for reviewing the project and the guiding on the basic principles.