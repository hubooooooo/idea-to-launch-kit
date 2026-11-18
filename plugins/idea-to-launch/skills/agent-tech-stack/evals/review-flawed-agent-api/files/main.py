import os, json, traceback
from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key="sk-demo-123", base_url="https://api.deepseek.com")
TASKS = {}

@app.post("/upload")
async def upload(f: UploadFile):
    path = "uploads/" + f.filename
    open(path, "wb").write(await f.read())
    return {"path": path}

@app.post("/outline")
def outline(topic: str):
    try:
        r = client.chat.completions.create(model="deepseek-chat", messages=[{"role": "user", "content": f"为《{topic}》写大纲，返回 JSON 数组"}])
        data = json.loads(r.choices[0].message.content)
        TASKS[topic] = {"status": "done", "outline": data}
        return data
    except Exception as e:
        return {"err": traceback.format_exc()}

@app.get("/write")
def write(topic: str):
    def gen():
        for chunk in client.chat.completions.create(model="deepseek-chat", stream=True, messages=[{"role": "user", "content": "按大纲写正文：" + json.dumps(TASKS[topic]["outline"])}]):
            yield "data: " + (chunk.choices[0].delta.content or "") + "\n\n"
    return StreamingResponse(gen(), media_type="text/event-stream")

@app.post("/publish")
def publish(topic: str, channel: str):
    # 让模型决定要不要发到公众号
    r = client.chat.completions.create(model="deepseek-chat", messages=[{"role": "user", "content": f"这篇文章适合发到 {channel} 吗？适合就回答 yes"}])
    if "yes" in r.choices[0].message.content:
        os.system(f"curl -X POST https://example.com/publish?channel={channel}")
    return {"ok": True}
