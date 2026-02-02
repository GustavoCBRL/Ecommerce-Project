# Commerce - Projeto CS50W

Aplicação Django de leilões online preparada para hospedagem no Railway.

## 🚀 Deploy no Railway

### Pré-requisitos
- Conta no [Railway](https://railway.app/)
- Git instalado

### Passos para Deploy

1. **Clone e prepare o repositório**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Faça o deploy no Railway**
   - Acesse [Railway](https://railway.app/)
   - Clique em "New Project"
   - Conecte seu repositório GitHub ou faça upload dos arquivos
   - Railway detectará automaticamente que é um projeto Django

3. **Configure as variáveis de ambiente**
   No painel do Railway, adicione estas variáveis:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=*.railway.app
   ```

4. **Adicione banco PostgreSQL**
   - No Railway, adicione o plugin PostgreSQL
   - A variável `DATABASE_URL` será configurada automaticamente

5. **Deploy automático**
   - Railway executará automaticamente as migrações e coletará os arquivos estáticos
   - A aplicação estará disponível na URL fornecida

### Estrutura do Projeto

- `Procfile` - Comando para iniciar o servidor Gunicorn
- `runtime.txt` - Versão do Python
- `requirements.txt` - Dependências Python
- `railway.toml` - Configurações específicas do Railway
- `.env.example` - Exemplo de variáveis de ambiente

### Comandos Úteis

```bash
# Executar localmente
python commerce/manage.py runserver

# Coletar arquivos estáticos
python commerce/manage.py collectstatic

# Executar migrações
python commerce/manage.py migrate

# Criar superusuário
python commerce/manage.py createsuperuser
```

### Dependências de Produção

- `gunicorn` - Servidor WSGI para produção
- `psycopg2-binary` - Driver PostgreSQL
- `whitenoise` - Servir arquivos estáticos
- `dj-database-url` - Configuração de banco via URL
- `python-dotenv` - Carregar variáveis de ambiente

### Segurança

✅ Secret key configurada via variável de ambiente  
✅ Debug desabilitado em produção  
✅ ALLOWED_HOSTS configurado  
✅ HTTPS redirect em produção  
✅ Configurações de segurança habilitadas  

### Troubleshooting

- Verifique os logs no painel do Railway em caso de erro
- Certifique-se de que todas as variáveis de ambiente estão configuradas
- Verifique se o banco PostgreSQL está ativo

## 📝 Funcionalidades

- Sistema de autenticação
- Criação e gerenciamento de leilões
- Sistema de lances
- Watchlist de usuários
- Categorias de produtos
- Interface responsiva