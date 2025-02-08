document.getElementById('submitButton').addEventListener('click', function() {
    const number = document.getElementById('numberInput').value;
    const resultDiv = document.getElementById('result');

    // Validate input
    if (!number || isNaN(number)) {
        resultDiv.innerHTML = `<p>Error: Please enter a valid number.</p>`;
        return;
    }

    // Update the URL based on your environment (local or deployed)
    fetch(`http://localhost:5000/api/classify-number?number=${number}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
                return;
            }
            resultDiv.innerHTML = `
                <h2>Results for ${data.number}</h2>
                <p>Is Prime: ${data.is_prime}</p>
                <p>Is Even: ${data.properties.includes('even')}</p>
                <p>Is Odd: ${data.properties.includes('odd')}</p>
                <p>Is Armstrong: ${data.properties.includes('armstrong')}</p>
                <p>Sum of Digits: ${data.digit_sum}</p>
                <p>Fun Fact: ${data.fun_fact}</p>
            `;
        })
        .catch(error => {
            resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
            console.error('API Error:', error);
        });
});
