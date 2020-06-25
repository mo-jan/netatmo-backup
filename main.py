#! /usr/bin/env python
import json
import os
import datetime

import netatmo

from dotenv import load_dotenv


def main():
    load_dotenv()
    DATA_PATH = "netatmo_data"

    # credentials
    ws = netatmo.WeatherStation(
        {
            "client_id": os.environ.get("CLIENT_ID"),
            "client_secret": os.environ.get("CLIENT_SECRET"),
            "username": os.environ.get("USERNAME"),
            "password": os.environ.get("PASSWORD"),
            "default_station": os.environ.get("DEFAULT_STATION"),
        }
    )
    ws.get_data()

    mod_living_room = {
        "id": ws.devices[0]["_id"],
        "csv_path": f"{DATA_PATH}/mod_living_room.csv",
        "fields": ws.devices[0]["data_type"],
    }
    mod_bedroom = {
        "id": ws.devices[0]["modules"][1]["_id"],
        "csv_path": f"{DATA_PATH}/mod_bedroom.csv",
        "fields": ws.devices[0]["modules"][1]["data_type"],
    }
    mod_outdoor = {
        "id": ws.devices[0]["modules"][0]["_id"],
        "csv_path": f"{DATA_PATH}/mod_outdoor.csv",
        "fields": ws.devices[0]["modules"][0]["data_type"],
    }
    modules_details = [mod_living_room, mod_bedroom, mod_outdoor]

    date_end = datetime.datetime.now()
    update_csv_files(ws, modules_details, date_end)


def update_csv_files(ws, modules_details, date_end):
    for mod in modules_details:
        netatmo.dl_csv(
            ws=ws,
            csv_file=mod["csv_path"],
            device_id="70:ee:50:29:15:e6",
            module_id=mod["id"],
            fields=mod["fields"],
            date_end=date_end.timestamp(),
        )


if __name__ == "__main__":
    main()
