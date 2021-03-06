import os
import re
import sys

search_path = ""


def main():
    global search_path
    if len(sys.argv) == 1:
        invalid_argument_list()
    else:
        search_path = sys.argv[1]
        search_for_files()


def invalid_argument_list():
    print "Invalid argument list. Please specify root directory of the project."


def create_string_for_write(found_strings):
    ready_string = "/*\nCreated by genstrings.py app. \n"
    ready_string += "The source code and more information is available on \n"
    ready_string += "https://github.com/Noiseapps/SwiftGenstringsPy\n*/\n\n"
    for string in found_strings:
        str_format = "\"{0}\"=\"PLACEHOLDER\";\n".format(string)
        ready_string += str_format
    return ready_string


def search_for_files():
    found_strings = list()
    print "\nSearching for files in directory {0}".format(search_path)

    files = os.listdir(search_path)
    print "\nFound {0} files total".format(len(files))

    # todo recursive folder traversal

    filtered_files = filter(lambda name: ".swift" in name, files)
    print "Left {0} Swift source files".format(len(filtered_files))

    for filename in filtered_files:
        process_file(filename, found_strings)

    print "\nFound {0} localized strings in source files".format(len(found_strings))

    strings = set(found_strings)
    save_to_file(strings)


def save_to_file(found_strings):
    """Save string containing located in the project localized strings to a 'Localized.strings' file
    :param found_strings: set containing found string keys
    """
    formatted_string = create_string_for_write(found_strings)
    output_file = open("Localizable.strings", "w")
    output_file.write(formatted_string)
    output_file.close()


def process_file(filename, found_strings):
    full_path = search_path + filename
    print "\nProcessing file: " + full_path
    with open(full_path) as f:
        search_single_file(f, found_strings)


def search_single_file(f, found_strings):
    lines = f.readlines()
    print "The line count for this file is {0}".format(len(lines))
    for line in lines:
        parse_line(found_strings, line)


def parse_line(found_strings, line):
    pattern = re.compile("\"([^\"]*)\"\.localize\(\)", re.I|re.U)
    for match in pattern.finditer(line):
        if match is not None:
            found_string = match.groups()[0]
            print "Pattern match for string {0}".format(found_string)
            found_strings.append(found_string)

if __name__ == '__main__':
    main()
