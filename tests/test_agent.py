import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import BankParserAgent

def test_agent_initialization():
    """Test agent initialization"""
    agent = BankParserAgent()
    assert agent is not None
    assert agent.max_attempts == 3

def test_agent_methods_exist():
    """Test that all required methods exist"""
    agent = BankParserAgent()
    # Update required methods to match actual implementation
    required_methods = [
        'plan', 
        'observe_pdf_structure', 
        'generate_parser_code',
        'test_parser', 
        'run'
    ]
    for method in required_methods:
        assert hasattr(agent, method), f"Missing method: {method}"

def test_groq_generate_function_exists():
    """Test that groq_generate exists as a module-level function"""
    from agent import groq_generate
    assert callable(groq_generate)
