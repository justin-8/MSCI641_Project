import argparse
import json
import os
import csv

def parse_args():
    parser = argparse.ArgumentParser(description='This is a baseline for task 2 that spoils each clickbait post with the title of the linked page.')

    parser.add_argument('--input', type=str, help='The input data filename (expected in jsonl format).', default='test.jsonl')
    parser.add_argument('--output', type=str, help='The output filename for spoiled posts in csv format.', default='baseline_task2_output.csv')

    return parser.parse_args()

def predict(inputs):
    for i in inputs:
        # Try to get the id using different possible keys
        id_value = i.get('uuid') or i.get('id') or i.get('postId')
        
        if id_value is None:
            print(f"Warning: Could not find an id for this entry. Available keys: {i.keys()}")
            continue
        
        # Use the title as the spoiler, but if it's empty, use the first sentence of the first paragraph
        spoiler = i.get('targetTitle', '')
        if not spoiler and i.get('targetParagraphs'):
            first_paragraph = i['targetParagraphs'][0]
            spoiler = first_paragraph.split('.')[0] + '.'  # First sentence of the first paragraph
        
        yield {'id': id_value, 'spoiler': spoiler}

def run_baseline(input_file, output_file):
    with open(input_file, 'r') as inp, open(output_file, 'w', newline='') as out:
        inp = [json.loads(i) for i in inp]
        writer = csv.DictWriter(out, fieldnames=['id', 'spoiler'])
        writer.writeheader()
        for output in predict(inp):
            writer.writerow(output)

if __name__ == '__main__':
    args = parse_args()
    
    # Set the base path
    base_path = "/Users/abiwaqasyasir/Desktop/UWaterloo_Academics/TERM_3/MSCI_641/Project"
    
    # Construct full paths for input and output files
    input_file = os.path.join(base_path, args.input)
    output_file = os.path.join(base_path, args.output)
    
    run_baseline(input_file, output_file)
    print(f"Baseline predictions written to {output_file}")