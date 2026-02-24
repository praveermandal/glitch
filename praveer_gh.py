name: PRAVEER.OWNS - KERNEL STRIKE

on:
  workflow_dispatch:

jobs:
  strike:
    # 🛑 THE FIX: We downgrade the runner OS to 22.04 to bypass the Python block
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Playwright & Dependencies
        run: |
          pip install playwright
          # This will now work flawlessly on Ubuntu 22.04
          playwright install --with-deps chromium

      - name: Launch 1-ID Strike
        env:
          SESSION_ID: ${{ secrets.SESSION_ID }}
          GROUP_URL: ${{ secrets.GROUP_URL }}
          TARGET_NAME: ${{ secrets.TARGET_NAME }}
        run: python -u praveer_gh.py
