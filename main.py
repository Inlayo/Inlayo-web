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
display:grid;
place-items:center;
font-family:Segoe UI, sans-serif;
color:white;
padding:20px;

background: linear-gradient(
-45deg,
#2b2d42,
#3a3d5c,
#3f3a57,
#2f3f46
);

background-size:300% 300%;
animation:bgMove 16s ease infinite;
}

.card {

width:100%;
max-width:380px;

padding:38px 32px;

display:flex;
flex-direction:column;
align-items:center;

background: rgba(40,40,55,0.75);
backdrop-filter: blur(16px);

border-radius:18px;

box-shadow:
0 10px 40px rgba(0,0,0,0.45);

}

h1 {
margin-bottom:28px;
font-weight:500;
color:#f1f1f1;
font-size:24px;
text-align:center;
}

a {

display:flex;
align-items:center;
justify-content:center;

width:100%;

margin:10px 0;
padding:13px;

border-radius:10px;

text-decoration:none;
font-weight:500;

color:#f0f0f0;

background:rgba(255,255,255,0.08);

transition: all .25s ease;

box-sizing:border-box;

}

a:hover {

transform: translateY(-2px);

background: rgba(255,255,255,0.15);

box-shadow:
0 0 14px rgba(210,180,255,0.35),
0 0 18px rgba(150,200,255,0.25);

}

@media (max-width:480px){

.card{
padding:30px 22px;
}

h1{
font-size:20px;
}

a{
font-size:15px;
padding:12px;
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