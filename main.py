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

@keyframes gradientMove {
0% {background-position: 0% 50%}
50% {background-position: 100% 50%}
100% {background-position: 0% 50%}
}

@keyframes float {
0% {transform: translateY(0px)}
50% {transform: translateY(-10px)}
100% {transform: translateY(0px)}
}

body {
margin: 0;
height: 100vh;
display: flex;
align-items: center;
justify-content: center;
font-family: "Segoe UI", sans-serif;

background: linear-gradient(-45deg,#ffd6e7,#e5d4ff,#d4f1ff,#ffe6c7);
background-size: 400% 400%;
animation: gradientMove 15s ease infinite;
}

.card {
backdrop-filter: blur(15px);
background: rgba(255,255,255,0.25);
border-radius: 20px;
padding: 40px;
width: 320px;
text-align: center;
box-shadow: 0 10px 40px rgba(0,0,0,0.15);
animation: float 6s ease-in-out infinite;
}

h1 {
margin-bottom: 30px;
font-weight: 600;
color: #333;
}

a {
display: block;
margin: 10px auto;
padding: 12px;
border-radius: 12px;
text-decoration: none;

background: rgba(255,255,255,0.7);
color: #333;
font-weight: 500;

transition: all 0.25s ease;
}

a:hover {
transform: translateY(-4px) scale(1.03);
box-shadow: 0 8px 25px rgba(0,0,0,0.2);
background: white;
}

</style>
</head>

<body>

<div class="card">

<h1>hello i'm Inlayo 💩</h1>

<a href="/osu">osu!</a>
<a href="/skins">skins</a>
<a href="/tw">twitter</a>
<a href="/ttv">twitch</a>
<a href="/yt">youtube</a>
<a href="/gh">github</a>
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
    return RedirectResponse(url="https://youtube.com/@Inlayo23", status_code=302)


@app.get("/gh")
@app.get("/github")
def redirect_to_github():
    return RedirectResponse(url="https://github.com/Inlayo", status_code=302)


@app.get("/osu")
def redirect_to_osu():
    return RedirectResponse(url="https://osu.ppy.sh/users/27692994", status_code=302)


@app.get("/ttv")
@app.get("/twitch")
def redirect_to_twitch():
    return RedirectResponse(url="https://twitch.tv/Inlayo", status_code=302)


@app.get("/discord")
def redirect_to_discord():
    return RedirectResponse(url="https://discord.gg/6PskvYDkpQ", status_code=302)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
