var modal = document.getElementById('id01');

window.onclick = function(event) {
    if (event.target == modal) {
    modal.style.display = "none";
    }
}

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting in the traditional way
    
    var username = document.getElementsByName('uname')[0].value;
    var password = document.getElementsByName('psw')[0].value;

    async function hashPassword(password) {
    // Convert the password string to a Uint8Array
    const encoder = new TextEncoder();
    const passwordData = encoder.encode(password);

    // Use the SubtleCrypto API to compute the SHA-256 hash
    const hashBuffer = await crypto.subtle.digest('SHA-256', passwordData);

    // Convert the hash buffer to a hexadecimal string
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(byte => byte.toString(16).padStart(2, '0')).join('');

    return hashHex;
    }

    hashPassword(password).then(hash => {
    // Make an AJAX request to the Flask server
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/login", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
        if (xhr.status == 200) {
        try{
            //console.log(xhr.responseText)
            var response = JSON.parse(xhr.responseText);
            //console.log(response);
            if (response.success){
                location.reload()
            }else{
                alert("Login failed. Please check your credentials.");
            }
            
        }catch(e){
            document.body.innerHTML = xhr.responseText;
        }
        } else {
        // Handle other HTTP status codes (e.g., 404, 500)
        alert("Server error. Please try again later.");
        }
    }
    };


       // Send the data to the server, including the hashed password
    xhr.send(JSON.stringify({ "username": username, "password": hash }));
    });
});

// Check if username and password are stored in local storage
const storedUsername = localStorage.getItem('username');
const storedPassword = localStorage.getItem('password');

if (storedUsername && storedPassword) {

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/login", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
        if (xhr.status == 200) {
        try{
            //console.log(xhr.responseText)
            var response = JSON.parse(xhr.responseText);
            //console.log(response);
            if (response.success == "true"){
                location.reload()
            }else{
                alert("Login failed. Please check your credentials.");
            }
            
        }catch(e){
            document.body.innerHTML = xhr.responseText;
        }
        } else {
        // Handle other HTTP status codes (e.g., 404, 500)
        alert("Server error. Please try again later.");
        }
    }
    };

    // Send the data to the server, including the hashed password
    xhr.send(JSON.stringify({ "username": username, "password": hash }));
}

