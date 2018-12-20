[![Build Status](https://travis-ci.org/nadralia/iReporter_Api.svg?branch=data_structures)](https://travis-ci.org/nadralia/iReporter_Api)
[![Coverage Status](https://coveralls.io/repos/github/nadralia/iReporter_Api/badge.svg?branch=data_structures)](https://coveralls.io/github/nadralia/iReporter_Api?branch=data_structures)
[![Maintainability](https://api.codeclimate.com/v1/badges/4ebc197ca3dd76fa3ef7/maintainability)](https://codeclimate.com/github/nadralia/iReporter_Api/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4ebc197ca3dd76fa3ef7/test_coverage)](https://codeclimate.com/github/nadralia/iReporter_Api/test_coverage)
# iReporter_Api
Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.


## Features 
- Create a red-flag record
- Get all red-flag records
- Get a specific red-flag record.
- Edit a specific red-flag record.
- Delete a red-flag record.

## API Endpoints
| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| POST | api/v1/red-flags | Creates a redflag |
| GET | /api/v1/red-flags | Fetches all red-flags|
| GET | api/v1/red-flags/&lt;redflag_id&gt; | Fetch a single redflag |

**Getting started with the app**

**Technologies used to build the application**

* [Python 3.7](https://docs.python.org/3/)

* [Flask](http://flask.pocoo.org/)