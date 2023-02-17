# send 1 sms / day
import requests

phone = input("enter phone number [+91xxxxxxxxxx]: ")
msg = input("enter your text : ")
print(f'----------\n*** </OƝioN ***\nphone number:{phone} \nsms:{msg}\n')
input("send?")

resp = requests.post('https://textbelt.com/text',
                    {
                    'phone': phone,
                    'message': msg,
                    'key': 'textbelt',
                    })
print(resp.json())

