
    async function checkCode() {
      const code = document.getElementById('codeInput').value;
      const resultDiv = document.getElementById('result');

      if (!code) {
        resultDiv.textContent = 'Please enter a code.';
        return;
      }

      try {
        const response = await fetch('http://127.0.0.1:5000/check_code', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ code })
        });

        const data = await response.json();

        if (response.ok) {
          console.log(data)
          resultDiv.innerText = data.is_active
          resultDiv.style.color = data.exists ? 'green' : 'red';
        } else {
          resultDiv.textContent = data.error || 'Something went wrong.';
          resultDiv.style.color = 'orange';
        }
      } catch (error) {
        resultDiv.textContent = 'Error connecting to server.';
        resultDiv.style.color = 'orange';
      }
    }