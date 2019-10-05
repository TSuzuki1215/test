import pya3rt

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply=create_reply(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))

def create_reply(res):
	apikey = "DZZPvqr1PTtbfoMsvJUshDwDIzw6rEMd"
	client = pya3rt.TalkClient(apikey)
	hello=client.talk(res)
	return hello["results"][0]["reply"]


#apikey = "DZZPvqr1PTtbfoMsvJUshDwDIzw6rEMd"
#client = pya3rt.TalkClient(apikey)

#print(client.talk("おはよう"))
#hello = client.talk("おはよう")
#print(hello["results"][0]["reply"])

#print(create_reply("おはよう"))

#test
