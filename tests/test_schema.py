import pytest
import pandas as pd
import os
import sys
import importlib.util

def test_schema_compliance():
    """Test that parser output matches expected schema"""
    if os.path.exists('custom_parsers/icici_parser.py'):
        spec = importlib.util.spec_from_file_location("icici_parser", "custom_parsers/icici_parser.py")
        if spec is not None and spec.loader is not None:
            parser_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(parser_module)
        else:
            pytest.fail("Could not load icici_parser module spec or loader")
        
        if os.path.exists('data/icici/icic_sample.pdf'):
            result_df = parser_module.parse('data/icici/icic_sample.pdf')
            expected_columns = ['Date', 'Description', 'Debit Amt', 'Credit Amt', 'Balance']
            assert list(result_df.columns) == expected_columns, "Schema mismatch"

def test_classification_logic():
    """Test that classification logic works correctly (either/or, never both)"""
    if os.path.exists('custom_parsers/icici_parser.py'):
        spec = importlib.util.spec_from_file_location("icici_parser", "custom_parsers/icici_parser.py")
        if spec is not None and spec.loader is not None:
            parser_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(parser_module)
        else:
            pytest.fail("Could not load icici_parser module spec or loader")
        
        if os.path.exists('data/icici/icic_sample.pdf'):
            result_df = parser_module.parse('data/icici/icic_sample.pdf')
            
            # Check that no row has both debit and credit amounts
            both_filled = sum(1 for _, row in result_df.iterrows() 
                            if str(row['Debit Amt']).strip() != '' and str(row['Credit Amt']).strip() != '')
            assert both_filled == 0, f"Classification error: {both_filled} rows have both amounts"
