thonimport json

def export_data(data, output_file="output.json"):
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)