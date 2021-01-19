from proc_rotate import main
import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
import getpass
import os 
import shutil
import tempfile

class TestMain:
  @pytest.fixture(autouse=True)
  def cleandir(self):
      old_cwd = os.getcwd()
      newpath = tempfile.mkdtemp()
      os.chdir(newpath)
      os.makedirs('./source_dir')
      open('./source_dir/file.txt','w').close()
      os.makedirs('./results')
      os.makedirs('./destination')
      yield
      os.chdir(old_cwd)
      shutil.rmtree(newpath)

  def test_source_path_notexists(self):
    "Raise error if source file doest not exists"
    with pytest.raises(ValueError) as error:
      main.rotate('./tests/fileNotFound.test', './tests/destination')
    assert error.exconly() == 'ValueError: The directory ./tests/fileNotFound.test cannot be found'

  def test_source_path_dir(self):
    "Source path sould be file not dir"
    with pytest.raises(ValueError) as error:
      main.rotate('./source_dir', './destination')
    assert error.exconly() == "ValueError: source_path must be a valid file path"

  def test_destination_path_dir(self):
    "Destination dir should not present on start"
    with pytest.raises(ValueError) as error:
      main.rotate('./source_dir/file.txt', './results')
    assert error.exconly() == "ValueError: destination directory should be present on app start"


 
  