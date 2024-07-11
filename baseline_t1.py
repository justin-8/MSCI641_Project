import json
import csv
import os

def run_baseline(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['id', 'spoilerType'])  # Write header

        for line in infile:
            data = json.loads(line)
            
            # Print the keys in the data dictionary
            print("Available keys:", data.keys())
            
            # Try to get the id using different possible keys
            id_value = data.get('uuid') or data.get('id') or data.get('postId')
            
            if id_value is None:
                print("Warning: Could not find an id for this entry:", data)
                continue
            
            prediction = 'passage'  # Naive prediction: always 'passage'
            csv_writer.writerow([id_value, prediction])

if __name__ == '__main__':
    base_path = "/Users/abiwaqasyasir/Desktop/UWaterloo_Academics/TERM_3/MSCI_641/Project"
    input_file = os.path.join(base_path, "test.jsonl")
    output_file = os.path.join(base_path, "naive_baseline_output.csv")
    
    run_baseline(input_file, output_file)
    print(f"Baseline predictions written to {output_file}")
    