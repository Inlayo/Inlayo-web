import subprocess
import sys

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI(title="Inlayo")


@app.get("/")
def root():
    html_content = """
<!DOCTYPE html>
<html>
<head>
<title>Inlayo</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

@keyframes bgMove {
0% {background-position:0% 50%}
50% {background-position:100% 50%}
100% {background-position:0% 50%}
}

body {
margin:0;
min-height:100vh;
display:flex;
align-items:center;
justify-content:center;
font-family:Segoe UI, sans-serif;
color:white;
padding:20px;

background: linear-gradient(-45deg,#111,#1c1c1c,#222,#181818);
background-size:400% 400%;
animation:bgMove 18s ease infinite;
}

.card {
width:100%;
max-width:360px;
padding:40px;
text-align:center;

background: rgba(30,30,30,0.65);
backdrop-filter: blur(18px);

border-radius:18px;

box-shadow:
0 0 40px rgba(200,200,255,0.05),
0 20px 50px rgba(0,0,0,0.6);
}

h1 {
margin-bottom:30px;
font-weight:500;
color:#eaeaea;
font-size:24px;
}

a {
display:block;
width:100%;
margin:10px 0;
padding:13px;

border-radius:10px;

text-decoration:none;
font-weight:500;

color:#eee;

background:rgba(255,255,255,0.06);

transition: all .25s ease;
}

a:hover {
transform: translateY(-2px);
background: rgba(255,255,255,0.12);

box-shadow:
0 0 12px rgba(255,190,220,0.35),
0 0 22px rgba(190,210,255,0.25);
}

@media (max-width:480px) {

.card {
padding:30px 22px;
}

h1 {
font-size:20px;
margin-bottom:22px;
}

a {
padding:12px;
font-size:15px;
}

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
        url="https://github.com/Inlayo/Inlayo-skins",
        status_code=302,
    )


@app.get("/tw")
@app.get("/twitter")
def redirect_to_twitter():
    return RedirectResponse(
        url="https://twitter.com/Inlayo123",
        status_code=302,
    )


@app.get("/yt")
@app.get("/youtube")
def redirect_to_youtube():
    return RedirectResponse(
        url="https://youtube.com/@Inlayo123",
        status_code=302,
    )


@app.get("/gh")
@app.get("/github")
def redirect_to_github():
    return RedirectResponse(
        url="https://github.com/Inlayo",
        status_code=302,
    )


@app.get("/osu")
def redirect_to_osu():
    return RedirectResponse(
        url="https://osu.ppy.sh/users/27692994",
        status_code=302,
    )


@app.get("/ttv")
@app.get("/twitch")
def redirect_to_twitch():
    return RedirectResponse(
        url="https://twitch.tv/Inlayo",
        status_code=302,
    )


@app.get("/discord")
def redirect_to_discord():
    return RedirectResponse(
        url="https://discord.gg/6PskvYDkpQ",
        status_code=302,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)