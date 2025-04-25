services:
  - type: web
    name: telegram-moderation-bot
    env: python
    plan: free
    runtime: python
    buildCommand: ""
    startCommand: python main.py
    envVars:
      - key: BOT_TOKEN
        value: 7786341898:AAHdPjculC44KfjYmVyjvbloEgkfaCmkGwE
