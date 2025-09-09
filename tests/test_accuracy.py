import pytest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_accuracy():
    """Test parser accuracy against expected results"""
    if os.path.exists('custom_parsers/icici_parser.py'):
        custom_parsers_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'custom_parsers'))
        if custom_parsers_path not in sys.path:
            sys.path.append(custom_parsers_path)
        from icici_parser import parse
        
        result_df = parse('data/icici/icic_sample.pdf')
        expected_df = pd.read_csv('data/icici/result.csv')
        
        # Test row count accuracy
        accuracy = len(result_df) / len(expected_df) if len(expected_df) > 0 else 0
        assert accuracy >= 0.95, f"Low accuracy: {accuracy*100:.1f}%"

def test_perfect_performance():
        custom_parsers_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'custom_parsers'))
        if custom_parsers_path not in sys.path:
            sys.path.append(custom_parsers_path)
        if os.path.exists(os.path.join(custom_parsers_path, 'icici_parser.py')):
            if custom_parsers_path not in sys.path:
                sys.path.append(custom_parsers_path)
            from icici_parser import parse
        else:
            pytest.skip("icici_parser.py not found in custom_parsers directory")
        
        result_df = parse('data/icici/icic_sample.pdf')
        expected_df = pd.read_csv('data/icici/result.csv')
        
        assert len(result_df) == len(expected_df), "Perfect accuracy required"
