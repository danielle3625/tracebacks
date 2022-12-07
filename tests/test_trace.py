from codeinsights.trace import time_elapsed
from codeinsights.trace import counter as trace_counter
from unittest.mock import Mock,patch,mock_open
from codeinsights.trace import trace


def test_time_elapsed_is_positive():
    assert time_elapsed() > 0

def test_line_event_returns_trace ():
    mock_frame = Mock()
    expected = trace
    with patch('codeinsights.trace.open', mock_open()) as m:
        assert trace(mock_frame, 'line', None) == expected

def test_line_event_records_fileline():
    mock_frame = Mock()
    mock_frame.f_lineno = 12
    mock_frame.f_code.co_filename = "foo.py"    
    with patch('codeinsights.trace.open', mock_open()) as m:
        trace_counter.clear()
        trace(mock_frame, 'line', None)
        assert trace_counter['foo.py', 12] == 1

def test_line_event_records_fileline_multiple():
    mock_frame = Mock()
    mock_frame.f_lineno = 12
    mock_frame.f_code.co_filename = "foo.py"    
    with patch('codeinsights.trace.open', mock_open()) as m:
        trace_counter.clear()
        trace(mock_frame, 'line', None)
        trace(mock_frame, 'line', None)
        assert trace_counter['foo.py', 12] == 2
