import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, "r") as f:
        data = json.load(f)

    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["reel", "imaginaire"])

        for real, imag in data:
            writer.writerow([real, imag])

json_to_csv("data.json", "complex.csv")
