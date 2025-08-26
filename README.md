# LekoMapa Lite

LekoMapa Lite is a simplified version of our medication search tool. It provides a basic API to look up medications by name and returns details such as the active ingredient and common indications.

## Features

* **Lightweight API** built with Flask that allows searching for medications.
* **Sample dataset** (`medications.csv`) with fictional medication data to demonstrate functionality.
* **Free tier**: The public repo includes a mock dataset.
* **Premium tier**: A separate private version can include real datasets, mobile apps, and additional integrations.

## Usage

1. Install dependencies: `pip install flask pandas`.
2. Run the API server: `python lekomapa_api.py`.
3. Query the API: `http://localhost:8000/search?query=aspirin`.

## Funding

If you find LekoMapa Lite useful, please consider supporting us through sponsors or donations.
