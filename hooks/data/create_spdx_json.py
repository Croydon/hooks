from conans import tools
import json

tools.download("https://raw.githubusercontent.com/spdx/license-list-data/v3.11/json/licenses.json", "licenses_raw.json", overwrite=True, retry=1, retry_wait=10)

licensesID = []

with open("licenses_raw.json", mode="r", encoding="utf-8") as file_raw:
    licenses_data = json.load(file_raw)
    for a_license in licenses_data["licenses"]: 
        licensesID.append(a_license["licenseId"])


with open("spdx.json", mode="w", encoding="utf-8") as spdx_file:
    json.dump(licensesID, spdx_file)
