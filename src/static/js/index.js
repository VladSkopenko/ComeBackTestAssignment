let selectedEdition = '';
let selectedFile = null;

function setSelectedEdition(edition) {
    selectedEdition = edition;
    document.getElementById('dropdownMenuButton').textContent = edition;
    checkInputs();
}

function checkInputs() {
    selectedFile = document.getElementById('fileInput').files[0];
    document.getElementById('uploadButton').disabled = !(selectedFile && selectedEdition);
}

function uploadFile() {
    if (!selectedFile || !selectedEdition) {
        alert('Будь ласка, виберіть файл і редакцію!');
        return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);
    formData.append('edition', selectedEdition);

    fetch('/document_word/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Помилка при завантаженні');
        }
        return response.json();
    })
    .then(data => {
        alert('Файл успішно завантажено!');
        window.location.href = '/formatted';
    })
    .catch(error => {
        alert('Помилка при завантаженні: ' + error.message);
    });
}