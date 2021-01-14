from proc_rotate import main
import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
import getpass

class TestMain:
  def test_source_path_notexists(self):
    "Raise error if source file doest not exists"
    with pytest.raises(ValueError) as error:
      main.rotate('./tests/fileNotFound.test', './tests/destination')
    assert error.exconly() == "ValueError: source_path must be a valid file path"

  def test_source_path_dir(self):
    "Source path sould be file not dir"
    with pytest.raises(ValueError) as error:
      main.rotate('./source_dir', './destination')
    assert error.exconly() == "ValueError: source_path must be a valid file path"

  def test_destination_path_dir(self):
    "Destination dir should not present on start"
    with pytest.raises(ValueError) as error:
      main.rotate('./tests/file.txt', './tests/destination_dir')
    assert error.exconly() == "ValueError: destination directory should be present on app start"

  def test_call_onData(self):
    "Should call onData with arg"
    onDataMagicMock = MagicMock()
    main.rotate('./tests/file.txt', './tests/destination', 10000, onData=onDataMagicMock)
    onDataMagicMock.assert_called()
 
  