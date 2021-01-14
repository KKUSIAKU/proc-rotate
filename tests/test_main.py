from proc_rotate import main
import pytest
from unittest.mock import patch
from unittest.mock import MagicMock

class TestMain:
  def test_source_path_notexists(self):
    "Raise error if source file doest not exists"
    with pytest.raises(ValueError) as error:
      main.rotate('./proc_rotate/fileNotFound.test', './destination')
    assert error.exconly() == "ValueError: source_path must be a valid file path"

  def test_source_path_dir(self):
    "Source path sould be file not dir"
    with pytest.raises(ValueError) as error:
      main.rotate('./source_dir', './destination')
    assert error.exconly() == "ValueError: source_path must be a valid file path"

  def test_destination_path_dir(self):
    "Destination dir should not present on start"
    with pytest.raises(ValueError) as error:
      main.rotate('./proc_rotate/file.txt', './proc_rotate/destination_dir')
    assert error.exconly() == "ValueError: destination direcotr should be present on app start"

def test_call_onData(self):
  "Should call onData with arg"
  # use magicmock to check called