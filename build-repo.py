#!/usr/bin/env python3

from pathlib import Path
import os

root = os.path.realpath(__file__)
rootPath = Path(root).parent

queue = [rootPath]

buf = """# Directory Contents - /{DirectoryPath}/

This file contains a table of contents for {DirectoryName}

"""


while len(queue) is not 0:
    currentPath = queue.pop()

    if currentPath.name[0] is '.':
        continue

    currentOutputBuffer = buf
    currentOutputBuffer = currentOutputBuffer.replace('{DirectoryPath}', currentPath.relative_to(rootPath).as_posix())
    currentOutputBuffer = currentOutputBuffer.replace('{DirectoryName}', currentPath.name)
    
    # get directory children
    dirs = [path for path in currentPath.iterdir() if path.is_dir()]

    # get file children
    files = [path for path in currentPath.iterdir() if path.is_file()]

    for directory in dirs:
        queue.append(Path(directory))
        relPath = directory.relative_to(rootPath)

        currentOutputBuffer += '- (/%s/)[/%s/]\n' % (directory.relative_to(rootPath).as_posix(), directory.relative_to(rootPath).as_posix())

    for fil in files:
        currentOutputBuffer += '- (/%s)[/%s]\n' % (fil.relative_to(rootPath).as_posix(), fil.relative_to(rootPath).as_posix())

    outputFilePath = currentPath.joinpath('index.md')
    with outputFilePath.open('w') as writeBuffer:
        writeBuffer.write(currentOutputBuffer)
