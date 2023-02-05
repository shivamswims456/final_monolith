from sdks.messages.user_message.errors.errors import ERRORS as _ERRORS



ERRORS = {"NO_SUPER_VENDOR":"Please add your ecom creds, Vendor creds dosn't exists",
          "SUMMARY_UNAVAIALBLE":"Unable to generate summary for the import"}

ERRORS.update(_ERRORS)