docker build -t know_your_man .

:: TODO: decide the port (keeping it 4545 for now)
docker run -d -p 4545:22 know_your_man
