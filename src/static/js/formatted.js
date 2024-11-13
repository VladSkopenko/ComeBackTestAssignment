async function formatDocument(documentId) {

    const url = `/document_word/format/${documentId}`;

    try {
      const response = await fetch(url, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        alert("Документ успішно форматовано!");
        window.location.reload();
      } else {
        alert("Виникла помилка при форматуванні документа.");
      }
    } catch (error) {
      console.error('Помилка при запиті:', error);
      alert("Виникла помилка при відправці запиту.");
    }
  }