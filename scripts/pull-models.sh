#\!/bin/bash
# PROTOCOL ZERO: Pull Ollama Models

MODELS=(
    "llama3.1"
    "mxbai-embed-large"
    "mistral"
)

for model in ""; do
    echo "Pulling ..."
    docker exec -it ollama ollama pull ""
done

echo ""
echo "Models pulled successfully\!"
echo "Verify with: docker exec -it ollama ollama list"
