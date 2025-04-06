# We want to build a bot that will trigger an alert when a flash loan happens with Tether
from forta_agent import transaction_event
from typing import List

AAVE_V3_ADDRESS: str = "0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2".lower()
FLASH_LOAN_TOPIC: str = "0xefefaba5e921573100900a3ad9cf29f222d995fb3b6045797eaea7521bd8d6f0".lower()

def handle_transaction(
        transaction_event: transaction_event.TransactionEvent
    ) -> List[transaction_event.TransactionEvent]:
    """
    Takes transaction event and returns a list of findings that have a flash loan in it.
    """    
    findings: List[transaction_event.TransactionEvent] = [] # type: ignore

    addresses_lowered = [key.lower() for key in transaction_event.addresses.keys()]

    if AAVE_V3_ADDRESS not in addresses_lowered:
        return findings
    
    flash_loan_events = []

    for log in transaction_event.logs:
        for topic in log.topics:
            if topic.lower == FLASH_LOAN_TOPIC:
                flash_loan_events.append(log)

    if len(flash_loan_events) == 0:
        return findings

    return findings