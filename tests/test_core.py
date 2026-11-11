import pytest
from app.ingestion import chunk_text
from app.agent import safe_calculate,calculator_query
def test_chunks(): assert chunk_text("one two three four five six",4,1)==["one two three four","four five six"]
def test_calculator(): assert safe_calculate("2+3*4")==14
def test_detect(): assert calculator_query("calculate 12 / 3")==4
def test_reject_code():
    with pytest.raises(ValueError): safe_calculate("__import__('os').system('whoami')")
