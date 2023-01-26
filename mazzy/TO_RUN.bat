docker build -t mazzy .

:: TODO: decide the port (keeping it 6868 for now)
docker run -d -p 6868:6868 mazzy
