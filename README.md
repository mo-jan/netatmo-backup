# netatmo-backup


## What is it

- Download sensor data from Netatmo Smart Home Weather Station using Github Workflow
- Big thanks to rene-d's [netatmo](https://github.com/rene-d/netatmo) library


## Getting started

- Clone this repository
- Install libraries from `requirements.txt`
- Rename `.env.tmpl` into `.env` and add your credentials 
- Check `DATA_PATH` in `main.py`, adapt if you want
- Run `python main.py`


## Github workflow

- The workflow is setup through `.github/workflows/run_updater.yml` 
- Add environment secrets to github secrets, using the same names as in `.env`. This way the `.env` file is obsolete.
- The script will download new sensor data every week, and store the data within the repository. 
