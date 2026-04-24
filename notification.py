from plyer import notification


def send_notification() -> None:
    if notification.notify is None:
        return

    notification.notify(
        title="Kanji Detected",
        message="Kanji copied to clipboard",
        app_name="Kanji OCR",
        timeout=2
    )
