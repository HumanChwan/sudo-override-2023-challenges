var count = 10;
var element = document.getElementById("counter");

// Function to update the counter
async function updateCounter() {
    while (count > 0) {
        count--;
        element.innerHTML = count;
        await new Promise(resolve => setTimeout(resolve, 1000));
    }
    // Do something after the counter ends
    fetchFlag();
    
}

function fetchFlag() {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
      };
      
      fetch("/get-flag", requestOptions)
        .then(response => response.text())
        .then(result => {
            let data = JSON.parse(result);
            element.innerHTML = data.flag;
            element.style.border = "0px solid #000000"
            element.style.width = "100%"
        })
        .catch(error => console.log('error', error));
}

// Start the counter
updateCounter();