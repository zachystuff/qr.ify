#!/usr/bin/python3
"""
Main Entry point for the QR.ify application.
QR.ify is a marketing tool designed to help small business owners convert links into qr code
Start the application
"""

import sys

sys.path.append('./qr_ify')
"""
Importing sys and using path append allows us to import functions from modules outside our main directory
"""

from qr_ify import app


def main():
    app.initializer()


if __name__ == "__main__":
    main()
