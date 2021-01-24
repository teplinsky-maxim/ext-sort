# ext-sort

## Usage
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

## Examples

Move video files to /home/user/Videos
    # *nix/Mac
    $ ext-sort -x mp4,mov,avi,mkv /some/source/directory /home/user/Videos

    # Windows
    C:\ext-sort path> C:\Path\to\Python.exe ext-sort -x mp4,mov,avi,mkv C:\some\source\directory C:\home\user\Videos

Move gifs recursively to /home/user/Pictures/gifs 
    # *nix/Mac
    $ ext-sort -r -x gif /some/source/directory /home/user/Pictures/gifs

    # Windows
    C:\ext-sort path> C:\Path\to\Python.exe ext-sort -k -x gif C:\some\source\directory C:\home\user\Pictures\gifs

Move video files recursively to /home/user/Videos and keep the file structure
    # *nix/Mac
    $ ext-sort -kr -x mp4,mov,avi,mkv /some/source/directory /home/user/Videos

    # Windows
    C:\ext-sort path> C:\Path\to\Python.exe ext-sort -kr -x mp4,mov,avi,mkv C:\some\source\directory C:\home\user\Videos