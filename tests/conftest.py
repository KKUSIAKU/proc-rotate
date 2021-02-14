import pytest
import os
import shutil
import stat
# source_dir, destination ... should be put in config 
# def retry_rmtree(func, path, exec_info):
#   os.chmod(path, stat.S_ISVTX)
#   func(path)

# @pytest.fixture(autouse=True)
# def clean_destination():
#   """
#   Caution: CRITICAL SETUP, test first any change to make sure you won't erase any directory by error
#   There are so much modules for path and directory handling in python :(
#   """
#   # destination = './destination'
#   # os.removedirs(destination)
#   print('&&&&&&&&&&&&&&&&&&&&&&&&&')
#   print(os.getcwd())

#   shutil.rmtree('./tests/destination/', onerror=retry_rmtree)
#   # print('&&&&&&&&&&&&&&&&&&&&&&&&&&')
#   # os.removedir('./tests/destination/')