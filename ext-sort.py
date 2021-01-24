#!/usr/bin/env python3
"""
ext-sort
Desc: A utility that sorts files based on their extension
v.0.1
2020 by radicalarchivist

Usage:
  ext-sort [-kr] -x EXTENSION SCAN-DIR TARGET-DIR
  ext-sort --help
  ext-sort --version

Options:
  SCAN-DIR                              Directory to be scanned
  TARGET-DIR                            Directory to copy files into
  -x --extension EXTENSION              extension(s) of the files to move
  -r --recursive                        Scan recursively
  -k --keep-structure                   Retains directory structure when moving
  -h --help                             Show this screen
  --version                             Show version info

"""

#
# TODO:
#
#

from docopt import docopt
import os
import shutil

def diff_path(file_dir,scan_dir):
    return file_dir.replace(scan_dir,"")

def get_filelist(path,exts,recurse):
    abspath = os.path.abspath(path)
    retlist = []
    if not recurse:
        for item in os.listdir(abspath):
            if os.path.isdir(os.path.join(path,item)):
                continue
            if item.split('.')[-1] in exts:
                retlist.append(os.path.join(path,item))
    else:
        for root,dirs,files in os.walk(abspath):
            for name in files:
                if name.split('.')[-1] in exts:
                    retlist.append(os.path.join(root,name))
    return retlist

def yn_prompt(prompt: str):
    '''
    Yes or no prompt
    '''
    while True:
        try:
            answer = input(f"{prompt} (y/[n]) ")
            if answer[0] == 'y' or answer[0] == 'n':
                if answer[0] == 'y':
                    return True
                else:
                    return False                    
            else:
                raise ValueError
        except ValueError:
            print('You must enter y or n.\n')
        except IndexError:
            return False

def main(args):
    print(f"Moving files with extension(s) {args['--extension']} from {args['SCAN-DIR']} to {args['TARGET-DIR']}",flush=True)
    print("Recursive Mode: " + ("On" if args['--recursive'] else "Off"),flush=True)
    print(f"Keep File Structure: {args['--keep-structure']}",flush=True)
    print(f"Scanning {args['SCAN-DIR']}",end="...",flush=True)
    filelist = get_filelist(args['SCAN-DIR'],args['--extension'].split(','),args['--recursive'])
    print("Done.",flush=True)
    if not len(filelist):
        print(f"No files were found with the extension(s): {args['--extension']}")
        exit()
    print(f"Found {len(filelist)} files with the extension(s): {args['--extension']}")
    if not yn_prompt(f"Do you wish to move the files to {args['TARGET-DIR']}?"): 
        print("Operation cancelled.",flush=True)
        exit()
    print(f"Moving files to {args['TARGET-DIR']}...",flush=True)
    for path in get_filelist(args['SCAN-DIR'],args['--extension'].split(','),args['--recursive']):
        if args['--keep-structure']:
            target = os.path.join(args['TARGET-DIR'],diff_path(path,args['SCAN-DIR']))
        else:
            _, name = os.path.split(path)
            target = os.path.join(args['TARGET-DIR'],name)
        try:
            tPath, _ = os.path.split(target)
            try:
                os.makedirs(tPath,exist_ok=True)
            except:
                print("Unable to create the target directory. Do you have the correct permissions?")
                exit(1)
            print(f"{path} --> {target}")
            shutil.move(path,target)
        except Exception as e:
            print(f"There was a problem moving the file: {e}")
            exit(1)

if __name__ == "__main__":
    main(docopt(__doc__, version='ext-sort v.0.1'))
    print("Done!",flush=True)
    exit()