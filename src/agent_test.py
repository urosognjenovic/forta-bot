from unittest.mock import Mock
from forta_agent import TransactionEvent, create_transaction_event
from agent import handle_transaction, AAVE_V3_ADDRESS, PROTOCOL, FLASH_LOAN_TOPIC
from typing import List

mock_tx_dictionary = {"transaction": {"hash": "0x1234"}, "addresses": {"0x5678": True}}

mock_tx_dictionary_for_USDT = {
    "transaction": {"hash": "0x1234"},
    "addresses": {AAVE_V3_ADDRESS: True, PROTOCOL: True},
    "logs": [{"topics": [FLASH_LOAN_TOPIC], "address": AAVE_V3_ADDRESS}],
}

mock_tx_event: TransactionEvent = create_transaction_event(mock_tx_dictionary)
mock_tx_event.filter_log = Mock()

mock_tx_event_for_USDT: TransactionEvent = create_transaction_event(
    mock_tx_dictionary_for_USDT
)
mock_tx_event_for_USDT.filter_log = Mock()


class TestFlashLoanDetector:
    def test_returns_empty_if_no_aave_contract(self):
        findings: List[TransactionEvent] = handle_transaction(mock_tx_event)
        assert len(findings) == 0

    def test_returns_empty_if_no_flash_loan_events(self):
        mock_tx_event.addresses = {AAVE_V3_ADDRESS: True}
        findings: List[TransactionEvent] = handle_transaction(mock_tx_event)
        assert len(findings) == 0

    def test_returns_finding_in_a_flash_loan(self):
        findings: List[TransactionEvent] = handle_transaction(mock_tx_event_for_USDT)
        assert len(findings) == 1
