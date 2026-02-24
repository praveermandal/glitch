name: PRAVEER PAPA - 10 AGENT MATRIX

on:
  workflow_dispatch: # Manual trigger only

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        machine: [1, 2, 3, 4, 5] # 5 Machines = 10 Agents total
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y google-chrome-stable
          pip install selenium

      - name: Run Matrix Blitz
        env:
          SESSION_ID: ${{ secrets.SESSION_ID }}
          GROUP_URL: ${{ secrets.GROUP_URL }}
          TARGET_NAME: ${{ secrets.TARGET_NAME }}
          MACHINE_ID: ${{ matrix.machine }}
          PYTHONUNBUFFERED: "1"
        run: python -u praveer_gh.py
