import pytest
import os
import shutil
# source_dir, destination ... should be put in config 
@pytest.fixture(autouse=True)
def clean_destination():
  """
  Caution: CRITICAL SETUP, test first any change to make sure you won't erase any directory by error
  There are so much modules for path and directory handling in python :(
  """
  # destination = './destination'
  # os.removedirs(destination)
  shutil.rmtree('./tests/destination')
  print('&&&&&&&&&&&&&&&&&&&&&&&&&&')
  os.removedir('./tests/destination')