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
                background-color: #d3d3d3;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
            }
            @keyframes scroll {
                0% {
                    transform: translateX(-100vw);
                }
                100% {
                    transform: translateX(100vw);
                }
            }
            .marquee {
                overflow: hidden;
                white-space: nowrap;
                margin: 20px 0;
                font-size: 24px;
                font-weight: bold;
            }
            .marquee-text {
                display: inline-block;
                animation: scroll 8s linear infinite;
            }
            a {
                display: block;
                padding: 10px;
                margin: 5px 0;
                color: #000;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="marquee">
            <span class="marquee-text">hello i'm Inlayo</span>
        </div>
        <a href="/skin">/skin</a>
        <a href="/skins">/skins</a>
        <a href="/tw">/twitter</a>
        <a href="/yt">/youtube</a>
        <a href="/osu">/osu</a>
        <a href="/twitch">/twitch</a>
        <a href="/discord">/discord</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/skin")
@app.get("/skins")
def redirect_to_skins():
    return RedirectResponse(url="https://github.com/Inlayo/Inlayo-skins", status_code=302)

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
