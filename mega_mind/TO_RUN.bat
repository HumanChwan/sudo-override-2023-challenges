docker build -t mega_mind .

:: TODO: decide the port (keeping it 3141 for now)
docker run -d -p 3141:3141 mega_mind
