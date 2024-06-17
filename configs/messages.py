from dataclasses import dataclass
from typing import Literal


@dataclass
class FunnelMessage:
    delay: float | int
    text: str
    triggers: tuple[str, ...] = ()
    trigger_action: Literal["continue", "break"] = "continue"


MESSAGES: tuple[FunnelMessage] = (
    FunnelMessage(
        delay=6 * 60,
        text="Текст1",
    ),
    FunnelMessage(
        delay=39 * 60,
        text="Текст2",
        triggers=("Триггер1",),
        trigger_action="continue",
    ),
    FunnelMessage(
        delay=26 * 60 * 60,
        text="Текст3",
    ),
)
"""Format: (delay_seconds, message)"""
