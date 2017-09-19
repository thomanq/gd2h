from __future__ import print_function

import os
import subprocess
import argparse
import codecs

def exists(command_name):
    return os.system("which -s " + command_name) == 0

def run(cmd):
    result = os.system(cmd)
    if result != 0:
        print("error: ", cmd)
    return not result

def gitdiff2html(args):
    changed_files = [fp for fp in subprocess.check_output("git diff {commit} --name-only".format(commit=args.commit).split()).decode("utf-8").split("\n") if fp.strip() != '']
    output_file_temp = args.output_file + '.tmp'
    all_dependancies_are_installed = True

    if args.auto:
        if args.output_file == 'diff.html':
            args.output_file = changed_files[0].replace('.txt', '') + '.html'
        if args.title == 'Git Diff':
            args.title = 'Correction'
        args.line_through = True
        args.drop_header = True

    for dependency in ["git", "aha"]:
        if not exists(dependency):
            all_dependancies_are_installed = False
            print('Command not found: "' + dependency + '". Please install this dependency.')
    
    if all_dependancies_are_installed:
        command_string = "git diff --patience  --color-words {commit} | aha -s -w --title '{title}' > {output_file_temp}".format(commit=args.commit, output_file_temp=output_file_temp, title=args.title)

        if args.print:
            print(command_string)
        else:
            if run(command_string): # execute command
                with codecs.open(output_file_temp, "r", "utf-8") as output_file_temp_handle:
                    with codecs.open(args.output_file, "w", "utf-8") as output_file_handle:
                        for line in output_file_temp_handle:
                            if line == ".green       {color: green;}\n":
                                output_file_handle.write(".green       {color: #00C900;}\n")
                            elif args.line_through and line == ".red         {color: red;}\n":
                                output_file_handle.write(".red         {color: red; text-decoration: line-through;}\n")
                            elif args.drop_header and len(line) > len('<span class="bold ">') \
                                                  and line[:len('<span class="bold ">')] in ['<span class="bold ">', '<span class="cyan ">']:
                                pass
                            else:
                                output_file_handle.write(line)
                try:
                    os.remove(output_file_temp)
                except:
                    print("error: could'nt delete ", output_file_temp)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--commit', default='HEAD^ HEAD', help="commits to diff, defaults to 'HEAD^ HEAD'")
    parser.add_argument('-o', '--output-file', default='diff.html', help="output file, defaults to 'diff.html'")
    parser.add_argument('-t', '--title', default='Git Diff', help="output file title, defaults to 'Git Diff'")
    parser.add_argument('-p', '--print', action='store_true', help="print output command instead of running it'")
    parser.add_argument('-l', '--line-through', action='store_true', help="line through deleted words'")
    parser.add_argument('-d', '--drop-header', action='store_true', help="drop git diff header")
    parser.add_argument('-a', '--auto', action='store_true', help="correction mode: set default flags for pretty file correction layout")
    parser.set_defaults(func=gitdiff2html)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()