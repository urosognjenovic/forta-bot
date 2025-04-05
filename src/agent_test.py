from unittest.mock import Mock
from forta_agent import TransactionEvent, create_transaction_event
from agent import handle_transaction
from typing import List

mock_tx_dictionary = {
    "transaction": {
        "hash": "0x1234"
    }, 
    "addresses": {
        "0x5678": True
    }
}

mock_tx_event: TransactionEvent = create_transaction_event(
    mock_tx_dictionary
) 
mock_tx_event.filter_log = Mock()

class TestFlashLoanDetector:
    def test_returns_empty_if_no_aave_contract(self):
        findings: List[TransactionEvent] = handle_transaction(mock_tx_event)
        assert len(findings) == 0