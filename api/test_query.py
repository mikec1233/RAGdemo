from app.server.chat.chat_service import ChatService

chat_service = ChatService()
response = chat_service.query("What is ARTool used for?")
print("Query Response:", response)
