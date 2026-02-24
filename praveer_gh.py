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

      - name: Install System Dependencies
        run: |
          sudo apt-get update
          sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
            libasound2t64 \
            libasound2-plugins \
            alsa-utils \
            fonts-freefont-ttf \
            fonts-ipafont-gothic \
            fonts-wqy-zenhei

      - name: Install Playwright & Browsers
        run: |
          pip install playwright
          # No sudo needed here. It safely downloads to the local runner cache.
          playwright install chromium

      - name: Launch 1-ID Strike
        env:
          SESSION_ID: ${{ secrets.SESSION_ID }}
          GROUP_URL: ${{ secrets.GROUP_URL }}
          TARGET_NAME: ${{ secrets.TARGET_NAME }}
          MACHINE_ID: "1"
        run: python -u praveer_gh.py
