module.exports = {
  apps: [
    {
      name: "web",
      script: "/usr/bin/python3",
      args: "-m uvicorn main:app --host 127.0.0.1 --port 8000",
      interpreter: "none",
      cwd: "/home/Inlayo/Inlayo-web",
      autorestart: true,
      watch: false,
      max_memory_restart: "500M",
      time: true
    }
  ]
};
