#!/bin/bash

# Script to rebuild and restart preview server
# Usage: ./rebuild-preview.sh

echo "🔨 Building site..."
npm run build

echo ""
echo "🛑 Stopping old preview server..."
pkill -f "npm run preview" 2>/dev/null || true

echo "⏳ Waiting for server to stop..."
sleep 2

echo "🚀 Starting preview server..."
npm run preview &

echo ""
echo "✅ Done! Preview server running at http://localhost:4173/hello_world"
echo "   Press Ctrl+C to stop this script (server will continue running)"
echo ""




