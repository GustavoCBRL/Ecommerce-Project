#!/bin/bash

# Script de deploy para Railway
echo "🚀 Iniciando deploy..."

# Navigate to commerce directory
cd commerce

# Collect static files
echo "📦 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# Run migrations
echo "🗃️ Executando migrações do banco de dados..."
python manage.py migrate --noinput

# Create superuser if needed (opcional)
# echo "👤 Criando superusuário (se necessário)..."
# python manage.py createsuperuser --noinput

echo "✅ Deploy concluído!"