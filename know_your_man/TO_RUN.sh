docker build -t know_your_man .
if [ $? -ne 0 ];
then
    echo "poo poo: at build"
    exit 1
fi

# TODO: decide the port (keeping it 4545 for now)
docker run -d -p 4545:22 know_your_man
if [ $? -ne 0 ];
then
    echo "poo poo: at run"
    exit 1
fi
