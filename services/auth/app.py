from flask import Flask, request, jsonify, Response
import os, time, jwt

app = Flask(__name__)
SECRET = os.getenv("JWT_SECRET", "devsecret")
ALGO = "HS256"

@app.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    if data.get("username") == "admin" and data.get("password") == "123456":
        now = int(time.time())
        payload = {"sub": "admin", "role": "admin", "iat": now, "exp": now + 3600}
        token = jwt.encode(payload, SECRET, algorithm=ALGO)
        return jsonify({"token": token, "expires_in": 3600})
    return jsonify({"error": "invalid credentials"}), 401

@app.get("/validate")
def validate():
    auth = request.headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        token = auth.split(" ", 1)[1]
        try:
            payload = jwt.decode(token, SECRET, algorithms=[ALGO])
            resp = Response(status=200)
            resp.headers["X-User"] = payload.get("sub", "")
            resp.headers["X-Role"] = payload.get("role", "user")
            return resp
        except Exception:
            pass
    return Response(status=401)

@app.get("/healthz")
def healthz():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
