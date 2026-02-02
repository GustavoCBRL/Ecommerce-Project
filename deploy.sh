#!/bin/bash

# Script de deploy para Railway
echo "🚀 Iniciando deploy..."

# Collect static files
echo "📦 Coletando arquivos estáticos..."
python commerce/manage.py collectstatic --noinput

# Run migrations
echo "🗃️ Executando migrações do banco de dados..."
python commerce/manage.py migrate --noinput

# Create superuser if needed (opcional)
# echo "👤 Criando superusuário (se necessário)..."
# python commerce/manage.py createsuperuser --noinput

echo "✅ Deploy concluído!"