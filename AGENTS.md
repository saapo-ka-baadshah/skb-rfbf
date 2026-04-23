# SKB React-FastAPI Barebone Framework (RFBF)

It is a Barebone Framework that is developed for quick spin ups and agentic oriented development

## Technology used:
- FastAPI for backend
    - Code is located in `src`
- React for frontend
    - Code is located in `front`

## Usage of `scripts`:
This will orchestrate the spin ups of frontend and backend in the right dependency cycle

# Rules:
1. Keep all the `README.md` updated with each commit according to
    - changes made in the commit
2. Do not use any emojis in the `README.md`
3. When Opencode is told to do a git commit, always maintain the latest state of `requirements.txt`
    - command to do that:
        ```shell
        source 0_setup.sh && pip freeze > requirements.txt
        ```

