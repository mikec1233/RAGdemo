from RAGdemo : python -m backend.src.api.api_handler
from /Users/spencercolon/GitRepos/RAGdemo/frontend/rag_frontend : npm run dev

commit to my branch:

    check if I am on the branch: git branch
    switch to branch: git checkout <your-branch-name>
    git add .
    git commit -m ""
    git push origin <your-branch-name>

Current time in video: 28:08

docker run --rm -p 8000:8000 \
--entrypoint python \
--env-file .env \
aws_rag_app /var/task/backend/src/api/api_handler.py

docker build -t rag-local -f Dockerfile .

docker run -p 8000:8000 rag-local

backend:

npm run generate-api-client -- -i http://localhost:80/openapi.json -g typescript-fetch -o src/api-client







