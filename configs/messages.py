MESSAGES: tuple[tuple[float | int, str]] = {
    (6 * 60, "Текст1"),  # 6min
    (39 * 60, "Текст2"),  # 39min
    (26 * 60 * 60, "Текст3"),  # 1d 2h
}
"""Format: (delay_seconds, message)"""
