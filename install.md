Create a conda python 2 environment with mongoDb:
`conda create -n yarnings python=2 mongodb

acitvate conda env: `source activate yarnings`

run `pip install -r requirements.txt`
note: need to version lock above at some point

make mongodb data folder if needed:
`sudo mkdir -p /data/db`

launch mongo: `mongod`

add test user to db:
`python populateDb.py`

Use "yarn" for username and password for now

run using flask webserver in dev:
`python run-dev.py`
