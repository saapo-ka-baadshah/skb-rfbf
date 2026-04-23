# RFBF - React FastAPI Barebone Framework

A clean, scalable, easy spinup framework for quick project initialization with FastAPI backend and React frontend.

## Technology Stack

- **Backend**: FastAPI
- **Frontend**: React

## Project Structure

```
.
├── front/          # React frontend (Vite)
├── front/app/      # React app (new)
├── scripts/        # Orchestration scripts
├── src/            # FastAPI backend
├── tests/          # Test files
├── 0_setup.sh      # Setup script
├── AGENTS.md       # Agent instructions
└── requirements.txt
```

## Quick Start

### Backend

```bash
cd src
pip install -r ../requirements.txt
python -m uvicorn app.main:app --reload
```

### Frontend

```bash
cd front
npm install
npm run dev
```

### Full Stack

```bash
source 0_setup.sh
```

## License

MIT