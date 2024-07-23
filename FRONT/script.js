const api = axios.create({
  baseURL: 'http://127.0.0.1:5000'
});

const produtos = async () => {
  try {
    const res = await api.get('/allprodutos');
    const produtosContainer = document.getElementById('produtos-container');

    res.data.forEach(produto => {
      const produtoDiv = document.createElement('div');
      produtoDiv.className = 'produto';

      const nameElement = document.createElement('h2');
      nameElement.textContent = produto.name;
      produtoDiv.appendChild(nameElement);

      const stockElement = document.createElement('p');
      stockElement.textContent = `Estoque: ${produto.stock}`;
      produtoDiv.appendChild(stockElement);

      const valueElement = document.createElement('p');
      valueElement.textContent = `Valor: R$ ${produto.value.toFixed(2)}`;
      produtoDiv.appendChild(valueElement);

      produtosContainer.appendChild(produtoDiv);
    });
  } catch (error) {
    console.error('Erro ao buscar produtos:', error);
  }
};

// Certifique-se de que o script seja carregado após o DOM estar pronto
window.addEventListener('load', produtos);
