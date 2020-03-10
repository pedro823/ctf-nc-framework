import argparse
import os.path
import shutil

ARGUMENT_TO_FILES = {
    'configfile': {
        'source': 'lib/templates/config.py',
        'dest': 'config/config.py',
    },
    'main': {
        'source': 'lib/templates/main.py',
        'dest': 'src/main.py',
    },
}

def generate(parser: argparse.ArgumentParser, args: argparse.Namespace) -> None:
    if args.generatable is None:
        print('You need to specify a file of file to generate.')
        parser.print_usage()
        return

    generatable_info = ARGUMENT_TO_FILES[args.generatable]
    if os.path.exists(generatable_info['dest']) and not confirm_prompt(generatable_info['dest']):
            return
    
    shutil.copyfile(generatable_info['source'], generatable_info['dest'])

def confirm_prompt(destination: str) -> bool:
    print(f'WARNING: this will override your current file in {destination}.')
    confirmation = input('Continue? [Y/n]').strip()
    return confirmation == '' or confirmation.lower().startswith('y')
