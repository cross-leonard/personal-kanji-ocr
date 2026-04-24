from plyer import notification


def send_notification() -> None:
    notify = notification.notify
    if notify is None:
        return

    notify(
        title="Kanji Detected",
        message="Kanji copied to clipboard",
        app_name="Kanji OCR",
        timeout=2
    )
