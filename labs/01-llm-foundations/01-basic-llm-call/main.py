import os

from dotenv import load_dotenv
from openai import OpenAI


# 1. 加载 .env 文件
load_dotenv()

# 2. 从环境变量读取配置
api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL_NAME")
base_url = os.getenv("OPENAI_BASE_URL")

# 3. 最基本的配置检查
if not api_key:
    raise ValueError("OPENAI_API_KEY is not configured")

if not model_name:
    raise ValueError("MODEL_NAME is not configured")


# 4. 创建 OpenAI Client
client_kwargs = {
    "api_key": api_key,
}

if base_url:
    client_kwargs["base_url"] = base_url

client = OpenAI(**client_kwargs)


# 5. 准备用户输入
user_input = "什么是 AI Agent？"


# 6. 调用 LLM API
response = client.responses.create(
    model=model_name,
    instructions="你是一个帮助我学习 Agent Engineering 的助手，请简洁回答。",
    input=user_input,
)


# 7. 提取最终文本
#print(response.output_text)

#查看output结构
# print("=== RESPONSE TYPE ===")
# print(type(response))
#
# print("\n=== RAW RESPONSE ===")
# print(response)
#
# print("\n=== OUTPUT TEXT ===")
# print(response.output_text)

print("=== RESPONSE INFO ===")
print("Response ID:", response.id)
print("Request ID:", response._request_id)
print("Model:", response.model)
print("Status:", response.status)

print("\n=== TOKEN USAGE ===")
print("Input Tokens:", response.usage.input_tokens)
print("Output Tokens:", response.usage.output_tokens)
print("Total Tokens:", response.usage.total_tokens)

print("\n=== OUTPUT TEXT ===")
print(response.output_text)