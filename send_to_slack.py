def send_slack_messge(message):
    import requests

    payload = '{"text": "%s"}' % message
    response = requests.post(
        # Edit this
        'your slack webhoook goes here',
        data = payload
    )
    # print(response.text)

def main(message_text):
    send_slack_messge(message=message_text)

# if __name__ == "__main__":
with open('active.txt', 'r') as fp:
    content = fp.read()
msg = content

if len(msg) > 0:
    main(message_text=msg)