from pathlib import Path

from loader_factory import input_loader


def test_txt_loader_returns_loader_for_txt_files():
    file_path = Path("text.txt")
    loader = input_loader(file_path)
    assert loader is not None
