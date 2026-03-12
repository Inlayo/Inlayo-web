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
@import url('https://fonts.googleapis.com/css2?family=Comic+Relief:wght@400;700&display=swap');

@keyframes bgMove {
0% {background-position:0% 50%}
50% {background-position:100% 50%}
100% {background-position:0% 50%}
}

@keyframes glowPulse {
0% {opacity:.4}
50% {opacity:.8}
100% {opacity:.4}
}

html, body {
margin:0;
height:100%;
overflow:hidden;
}

body {
height:100dvh;
display:flex;
flex-direction:column;
align-items:center;
justify-content:center;

font-family:"Comic Relief", system-ui;
font-weight:400;

color:white;

background: linear-gradient(-45deg,#2b2d42,#3a3d5c,#3f3a57,#2f3f46);
background-size:300% 300%;
animation:bgMove 16s ease infinite;
}

body::before,
body::after{
content:"";
position:fixed;
width:420px;
height:420px;
border-radius:50%;
filter:blur(120px);
z-index:-1;
animation:glowPulse 6s ease-in-out infinite;
}

body::before{
background:#a78bfa;
top:-120px;
left:-120px;
}

body::after{
background:#7dd3fc;
bottom:-120px;
right:-120px;
}

.card {

width:75vw;
max-width:380px;

padding:38px 28px;

display:flex;
flex-direction:column;
align-items:center;

background: rgba(40,40,55,0.75);
backdrop-filter: blur(16px);

border-radius:18px;

box-shadow:
0 0 30px rgba(180,160,255,0.15),
0 10px 40px rgba(0,0,0,0.45);

box-sizing:border-box;
}

h1 {
margin-bottom:26px;
font-size:26px;
font-weight:700;
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

color:#f0f0f0;

background:rgba(255,255,255,0.08);

transition: all .25s ease;

box-sizing:border-box;
}

.osu:hover{
box-shadow:
0 0 18px rgba(255,102,170,.9),
0 0 28px rgba(255,102,170,.6);
}

.skins:hover{
box-shadow:
0 0 18px rgba(255,255,255,.9),
0 0 28px rgba(255,255,255,.6);
}

.twitter:hover{
box-shadow:
0 0 18px rgba(29,161,242,.9),
0 0 28px rgba(29,161,242,.6);
}

.twitch:hover{
box-shadow:
0 0 18px rgba(145,70,255,.9),
0 0 28px rgba(145,70,255,.6);
}

.youtube:hover{
box-shadow:
0 0 18px rgba(255,0,0,.9),
0 0 28px rgba(255,0,0,.6);
}

.github:hover{
box-shadow:
0 0 18px rgba(255,255,255,.9),
0 0 28px rgba(255,255,255,.6);
}

.discord:hover{
box-shadow:
0 0 18px rgba(88,101,242,.9),
0 0 28px rgba(88,101,242,.6);
}

.footer{
margin-top:14px;
font-size:13px;
opacity:.6;
}

@media (max-width:480px){

.card{
width:75vw;
padding:28px 20px;
}

h1{
font-size:22px;
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

<a class="osu" href="/osu" target="_blank" rel="noopener">osu!</a>
<a class="skins" href="/skins" target="_blank" rel="noopener">skins</a>
<a class="twitter" href="/tw" target="_blank" rel="noopener">twitter</a>
<a class="twitch" href="/ttv" target="_blank" rel="noopener">twitch</a>
<a class="youtube" href="/yt" target="_blank" rel="noopener">youtube</a>
<a class="github" href="/gh" target="_blank" rel="noopener">github</a>
<a class="discord" href="/discord" target="_blank" rel="noopener">discord</a>

</div>

<div class="footer">
© 2026 Inlayo
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
