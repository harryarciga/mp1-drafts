from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument('stage_file')
    args = parser.parse_args()
    with open(args.stage_file, encoding="utf-8") as f:
        for index, line in enumerate(f):
            if index >= 2:
                print(line, end="")
    print(f"Previous moves:")
    print(f"Remaining moves:")
    print(f"Points:")
    print(f"Enter move/s:")




if __name__ == "__main__":
    main()


###### this is for the clearing the terminal

#import os
#import subprocess
#import sys

#def clear_screen():
#    """Clears the terminal screen, if any"""
#    if sys.stdout.isatty():
#        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
#        subprocess.run([clear_cmd])

#def main():
#    if len(sys.argv) < 2:
#        print('The game requires a filename to start.', file=sys.stderr)
#        return
#    with open(sys.argv[1], encoding='utf-8') as f:
#        # add input code here
#        for line in f:
#            print(line,end='')
            
            