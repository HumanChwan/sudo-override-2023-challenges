docker build -t mazzy .
if [ $? -ne 0 ];
then
    echo "poo poo: at build"
    exit 1
fi

# TODO: decide the port (keeping it 6868 for now)
docker run -d -p 6868:6868 mazzy
if [ $? -ne 0 ];
then
    echo "poo poo: at run"
    exit 1
fi
