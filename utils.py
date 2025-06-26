import logging

class _NoFunctionCallWarning(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        if "there are non-text parts in the response:" in message:
                return False
        else:
                return True

logging.getLogger("google_genai.types").addFilter(_NoFunctionCallWarning())