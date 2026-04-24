from plyer import notification

def send_notification(notifications_enabled : bool, copied_char : str) -> None:
    """Show the completion notification when enabled."""
    if notification.notify is None:
        return

    if notifications_enabled == True:
        notification.notify(
            title="kanji ocr",
            message= copied_char + " copied to clipboard",
            app_name="Kanji OCR",
            timeout=2
        )
