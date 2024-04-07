var inputFile = document.getElementById('csv_file');
var fileBtn = document.getElementById('fileBtn');
const uploadForm = document.getElementById('upload-form');
        // Get the button element
        var seeResultButton = document.getElementById('see-result');

        // Event listener for input file change
        inputFile.addEventListener('change', function() {
            // Check if a file is selected
            if (inputFile.files.length > 0) {
                // Show the button
                seeResultButton.style.display = 'block';
                fileBtn.innerText = inputFile.files[0].name;
            } else {
                // Hide the button if no file is selected
                seeResultButton.style.display = 'none';
            }
        });

        uploadForm.addEventListener('submit', (e)=>{
            e.preventDefault();
            // Get the selected file
            var file = inputFile.files[0];
            // Create a FormData object to store the file data
            var formData = new FormData();
            formData.append('csv_file', file);
            
            // Create a new XMLHttpRequest object
            var xhr = new XMLHttpRequest();
            // Configure the request
            xhr.open('POST', '', true);
            // Set up a callback function to handle the response
            xhr.onreadystatechange = function() {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        // Display the result in the 'result' div
                        document.getElementById('result').innerHTML = xhr.responseText;
                    } else {
                        // Handle error
                        console.error('Error:', xhr.status);
                    }
                }
            };
            // Send the request with the FormData object as the payload
            xhr.send(formData);
        })