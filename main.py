from fastapi import FastAPI
import sys

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello from Docker Python container!",
        "python": sys.version
    }

@app.get("/health")
def health():
    return {"status": "ok"}
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello Python on Docker!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
# from flask import Flask, jsonify
# import sys

# app = Flask(__name__)

# @app.route('/')
# def root():
#     return jsonify({
#         "message": "Hello from Docker Python container!",
#         "python": sys.version
#     })

# @app.route('/health')
# def health():
#     return jsonify({"status": "ok"})

# if __name__ == '__main__':
#     # 这里可以修改 port=8000 为你需要的端口
#     app.run(host='0.0.0.0', port=8000)from flask import Flask
# import sys

# app = Flask(__name__)

# @app.route('/')
# def root():
#     # 返回 HTML 格式，浏览器会直接渲染
#     return f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Docker Python App</title>
#         <style>
#             body {{ font-family: Arial, sans-serif; margin: 40px; background: #f0f2f5; }}
#             .container {{ max-width: 600px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
#             h1 {{ color: #2c3e50; }}
#             .python-version {{ background: #e8f4f8; padding: 10px; border-radius: 5px; margin-top: 20px; }}
#     </style>
# </head>
# <body>
#     <div class="container">
#         <h1>🐳 Hello from Docker Python Container!</h1>
#         <div class="python-version">
#             <strong>Python Version:</strong> {sys.version}
#         </div>
#         <p style="color: #7f8c8d; margin-top: 20px;">Flask app running inside Docker ✅</p>
#     </div>
# </body>
# </html>
# """

# @app.route('/health')
# def health():
#     # 健康检查接口保持 JSON 格式（给监控工具用）
#     return {"status": "ok"}, 200, {'Content-Type': 'application/json'}

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)
# from flask import Flask
# import sys

# app = Flask(__name__)

# @app.route('/')
# def root():
#     # 返回 HTML 格式，浏览器会直接渲染
#     return f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Docker Python App</title>
#         <style>
#             body {{ font-family: Arial, sans-serif; margin: 40px; background: #f0f2f5; }}
#             .container {{ max-width: 600px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
#             h1 {{ color: #2c3e50; }}
#             .python-version {{ background: #e8f4f8; padding: 10px; border-radius: 5px; margin-top: 20px; }}
#     </style>
# </head>
# <body>
#     <div class="container">
#         <h1>🐳 Hello from Docker Python Container!</h1>
#         <div class="python-version">
#             <strong>Python Version:</strong> {sys.version}
#         </div>
#         <p style="color: #7f8c8d; margin-top: 20px;">Flask app running inside Docker ✅</p>
#     </div>
# </body>
# </html>
# """

# @app.route('/health')
# def health():
#     # 健康检查接口保持 JSON 格式（给监控工具用）
#     return {"status": "ok"}, 200, {'Content-Type': 'application/json'}

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)