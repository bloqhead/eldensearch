#!/bin/bash

echo "🚀 Elden Ring Weapon Search Setup"
echo "=================================="

# Check if FONTAWESOME_TOKEN is set
if [ -z "$FONTAWESOME_TOKEN" ]; then
    echo "❌ FONTAWESOME_TOKEN environment variable is not set."
    echo ""
    echo "To set it up:"
    echo "1. Get your FontAwesome Pro token from: https://fontawesome.com/account"
    echo "2. Set the environment variable:"
    echo "   export FONTAWESOME_TOKEN=\"your-token-here\""
    echo ""
    echo "Or create a .env file with:"
    echo "FONTAWESOME_TOKEN=your-token-here"
    echo ""
    exit 1
fi

echo "✅ FONTAWESOME_TOKEN is set"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pnpm install

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
    echo ""
    echo "🎉 Setup complete! You can now run:"
    echo "   docker-compose up --build"
else
    echo "❌ Failed to install dependencies. Please check your FontAwesome token."
    exit 1
fi 