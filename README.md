# gd2h
Git diff to HTML Tool

```code
$ python gd2h.py -h

usage: gd2h.py [-h] [-c COMMIT] [-o OUTPUT_FILE] [-t TITLE] [-p] [-l] [-d]
               [-a]

optional arguments:
  -h, --help            show this help message and exit
  -c COMMIT, --commit COMMIT
                        commits to diff, defaults to 'HEAD^ HEAD'
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        output file, defaults to 'diff.html'
  -t TITLE, --title TITLE
                        output file title, defaults to 'Git Diff'
  -p, --print           print output command instead of running it'
  -l, --line-through    line through deleted words'
  -d, --drop-header     drop git diff header
  -a, --auto            correction mode: set default flags for pretty file
                        correction layout
```

# Dependencies

- git
- [aha](https://github.com/theZiz/aha)