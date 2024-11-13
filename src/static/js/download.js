function downloadDocument(fileName) {
    const encodedFileName = encodeURIComponent(fileName);
    const url = `/document_word/download${encodedFileName}`;
    window.location.href = url;
}