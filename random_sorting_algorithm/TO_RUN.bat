docker build -t random_sorting_algorithm .

:: TODO: decide the port (keeping it 6553 for now)
docker run -d -p 6553:6553 random_sorting_algorithm
