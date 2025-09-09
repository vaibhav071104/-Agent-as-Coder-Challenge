import pytest
from agent import BankParserAgent

class TestBankParserAgent:
    def test_icici_agent(self):
        # Initialize agent first
        agent = BankParserAgent()
        # Then run with target bank
        result = agent.run('icici')
        assert result is True

    @pytest.fixture
    def agent(self):
        return BankParserAgent()

    def test_parser_generation(self, agent):
        plan = agent.plan('icici')
        assert plan['target'] == 'icici'
        assert 'strategy' in plan