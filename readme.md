# Como Rodar o Projeto
Repositório do projeto criado no workshop de APIs Restfull com Django com o grupo LICA da Unimontes
Documentação postman disponível em [https://documenter.getpostman.com/view/3596206/2sAYkAQhQK#e7c23650-8895-4204-a6ab-278c93e0be58](https://documenter.getpostman.com/view/3596206/2sAYkAQhQK#e7c23650-8895-4204-a6ab-278c93e0be58).

## **Pré-requisitos**
Antes de iniciar, certifique-se de ter os seguintes requisitos instalados:
- Python 3.x
- Virtualenv (opcional, mas recomendado)

## **1. Clonar o Repositório**
```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

## **2. Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

## **3. Instalar as Dependências**
```bash
pip install -r requirements.txt
```

## **4. Aplicar as Migrations**
```bash
python src/manage.py migrate
```

## **5. Criar um Superusuário (Opcional)**
Se precisar acessar o Django Admin:
```bash
python src/manage.py createsuperuser
```

## **6. Rodar o Servidor**
```bash
python src/manage.py runserver
```
O servidor estará disponível em `http://127.0.0.1:8000/` (ou `http://localhost:8000/`).

---
Agora o seu projeto está pronto para ser utilizado! 🎉
