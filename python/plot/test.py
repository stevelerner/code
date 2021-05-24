from slack_webhook import Slack
slack = Slack(url='https://hooks.slack.com/services/T010034DFV3/B01NV387HDL/SECRET')
slack.post(text="Hello, world.")
