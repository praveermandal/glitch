name: PRAVEER.OWNS - KERNEL STRIKE

on:
  workflow_dispatch:

jobs:
  strike:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Playwright & Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install playwright
          # This single line downloads Chromium AND safely installs all required Ubuntu OS libraries
          playwright install --with-deps chromium

      - name: Launch 1-ID Strike
        env:
          SESSION_ID: ${{ secrets.SESSION_ID }}
          GROUP_URL: ${{ secrets.GROUP_URL }}
          TARGET_NAME: ${{ secrets.TARGET_NAME }}
          MACHINE_ID: "1"
        run: python -u praveer_gh.py
