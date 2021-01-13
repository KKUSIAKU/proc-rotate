import os

def _validate_source(source):
    if not os.path.isfile(os.path.realpath(source)):
        raise ValueError('source_path must be a valid file path')


def _valide_destination(destination):
    if os.path.exists(os.path.realpath(destination)):
        raise ValueError('destination direcotr should be present on app start')


def _defaultProccesor(data):
    return data

def _migrateTempfileContent(tempfilePath, destination_path):
    pass


def _emptyFile(file):
    open(file, 'w').close()

def _rotateTempFileContent(tempfilePath, destination_path):
    _migrateTempfileContent(tempfilePath, destination_path)
    _emptyFile(tempfilePath)

def _rotate(source_path, destination_path, buffer_size, process=_defaultProccesor):
    tempfilePath = os.path.join(os.path.realpath(destination_path), 'temp.txt')
    with open(source_path) as source, \
            open(tempfilePath) as destination:
        for line in source:
            value = process(line)
            destination.write(value)
            if os.path.getsize(tempfilePath) >= buffer_size:
                _rotateTempFileContent(tempfilePath, destination_path)
        _rotateTempFileContent(tempfilePath, destination_path)
    return

def rotate(source_path, destination_path, buffer_size=100000):
    "Module to process large data source and rotate result in file of max size of buffer_size"
    _validate_source(source_path)
    _valide_destination(destination_path)
    if not os.path.getsize(os.path.realpath(source_path)):
        _rotate(source_path, destination_path, buffer_size)
    return 0
