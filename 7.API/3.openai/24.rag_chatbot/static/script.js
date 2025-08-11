async function uploadFile() {
    console.log('업로드 실행');
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    // console.log(file);
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    alert(result.message);
}

async function askQuestion() {
    const questionInput = document.getElementById('questionInput');
    const question = questionInput.value;

    const response = await fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({question})
    })

    const data = await response.json();
    const result = document.getElementById('answer');
    result.innerHTML = data.message;
}
