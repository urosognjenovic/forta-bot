# We want to build a bot that will trigger an alert when a flash loan happens with Tether
from forta_agent import transaction_event
from typing import List

AAVE_V3_ADDRESS: str = "0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2".lower()

def handle_transaction(
        transaction_event: transaction_event.TransactionEvent
    ) -> List[transaction_event.TransactionEvent]:
    """
    Takes transaction event and returns a list of findings that have a flash loan in it.
    """    
    findings: List[transaction_event.TransactionEvent] = []

    addresses_lowered = [key.lower() for key in transaction_event.addresses.keys()]

    if AAVE_V3_ADDRESS not in addresses_lowered:
        return findings

    return findings