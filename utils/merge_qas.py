import argparse
import os
import json

# Parse CLI arguements
parser = argparse.ArgumentParser(description='Merge JSON QAs')

parser.add_argument('-i', '--qa_dir', type=str, help='Path to QA directory', required=True)
parser.add_argument('-o', '--output_path', type=str, help='Path for merged QA output ', required=True)
args = parser.parse_args()

def main():
    # Set input and output file paths
    qa_dir = os.path.expanduser(args.qa_dir)
    output_path = args.output_path
    if not output_path.endswith('.json'):
        output_path += '.json'
    output_path = os.path.expanduser(output_path)
    
    # Initialise merged QA dict
    qas = {'data': []}

    # Open each QA file and apped to merged QA dict
    for file in sorted(os.listdir(qa_dir)):
        fpath = os.path.join(qa_dir, file)
        with open(fpath, 'r') as fp:
            data = json.load(fp)['data']
        qas['data'] += data

    # Write merged to QA dict to file
    with open(output_path, 'w') as f:
        f.write(json.dumps(qas, indent=2))

    print(f'Merged QA written to: {output_path}')

if __name__ == '__main__':
    main()