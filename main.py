import subprocess
import sys

from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI(title="Inlayo")


@app.get("/")
def root():
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Inlayo</title>
    <meta charset="utf-8">
    <style>
        body {
            background-color: #1f1f1f;
            font-family: Arial, sans-serif;
            margin: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #ffffff;
        }

        .container {
            text-align: center;
        }

        h1 {
            margin-bottom: 30px;
            font-weight: 500;
        }

        a {
            display: block;
            width: 200px;
            margin: 8px auto;
            padding: 10px;
            color: #ffffff;
            text-decoration: none;
            background: #2a2a2a;
            border-radius: 8px;
            transition: background 0.2s, transform 0.1s;
        }

        a:hover {
            background: #3a3a3a;
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>hello i'm Inlayo💩</h1>

        <a href="/skins">skins</a>
        <a href="/tw">twitter</a>
        <a href="/yt">youtube</a>
        <a href="/osu">osu!</a>
        <a href="/twitch">twitch</a>
        <a href="/discord">discord</a>
    </div>
</body>
</html>
"""
    return HTMLResponse(content=html_content)


@app.get("/skin")
@app.get("/skins")
def redirect_to_skins():
    return RedirectResponse(
        url="https://github.com/Inlayo/Inlayo-skins", status_code=302)


@app.get("/tw")
@app.get("/twitter")
def redirect_to_twitter():
    return RedirectResponse(url="https://twitter.com/Inlayo123", status_code=302)


@app.get("/yt")
@app.get("/youtube")
def redirect_to_youtube():
    return RedirectResponse(url="https://youtube.com/@Inlay123", status_code=302)


@app.get("/osu")
def redirect_to_osu():
    return RedirectResponse(url="https://osu.ppy.sh/users/27692994", status_code=302)


@app.get("/twitch")
def redirect_to_twitch():
    return RedirectResponse(url="https://twitch.tv/Inlayo", status_code=302)


@app.get("/discord")
def redirect_to_discord():
    return RedirectResponse(url="https://discord.gg/6PskvYDkpQ", status_code=302)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
