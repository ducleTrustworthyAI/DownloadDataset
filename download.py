import argparse
import subprocess

dictation = {
    "imagenet": 
        {
            "2012": {
                "train": "wget https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_train.tar --no-check-certificate",
                "valid": "wget https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_val.tar --no-check-certificate"
                }
        },
    "mimiciv": {
        "2.2": "wget -r -N -c -np --user lengocduc195 --ask-password https://physionet.org/files/mimiciv/2.2/"
    },
    "mimiciii": {
        "1.4": "wget -r -N -c -np --user lengocduc195 --ask-password https://physionet.org/files/mimiciii/1.4/"
    },
    "mimic-cxr-jpg": {
        "2.1.0": "wget -r -N -c -np --user lengocduc195 --ask-password https://physionet.org/files/mimic-cxr-jpg/2.1.0/"
    },
    "cxr-pro": {
        "1.0.0": "wget -r -N -c -np --user lengocduc195 --ask-password https://physionet.org/files/cxr-pro/1.0.0/"
    }
}

def main():
    parser = argparse.ArgumentParser(description='Download data using wget based on input')
    parser.add_argument('input', type=str, help='Input to determine what to download')
    args = parser.parse_args()

    input_tokens = args.input.split()
    if input_tokens[0] in dictation.keys():
        if input_tokens[1] in dictation[input_tokens[0]].keys():
            if len(input_tokens) == 2:
                command = dictation[input_tokens[0]][input_tokens[1]]
                print(f'Downloading IMAGENET TRAIN data...')
                subprocess.run(command, shell=True)
                print('Download completed.')
            elif input_tokens[2] in dictation[input_tokens[0]][input_tokens[1]].keys():
                if len(input_tokens) == 3:
                    command = dictation[input_tokens[0]][input_tokens[1]][input_tokens[2]]
                    print(f'Downloading IMAGENET TRAIN data...')
                    subprocess.run(command, shell=True)
                    print('Download completed.')
        
    elif args.input.lower() == '--help':
        print(dictation)
    else:
        print('Input not recognized.')

if __name__ == '__main__':
    main()
