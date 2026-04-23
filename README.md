# RFBF - React FastAPI Barebone Framework

A clean, scalable, easy spinup framework for quick project initialization with FastAPI backend and React frontend.

## Technology Stack

- **Backend**: FastAPI
- **Frontend**: React

## Project Structure

```
.
├── front/          # React frontend (Vite)
├── front/app/      # React app
├── scripts/        # Orchestration scripts
│   ├── 00_create_env.sh
│   ├── 01_start_dev.sh
│   └── common.sh
├── src/            # FastAPI backend
├── tests/          # Test files
├── 0_setup.sh      # Virtual environment setup
├── AGENTS.md       # Agent instructions
└── requirements.txt
```

## Quick Start (Full Stack)

```bash
# One-time setup
source 0_setup.sh

# Start development servers
./scripts/01_start_dev.sh
```

## Optional Modes

### Backend Only

```bash
cd src
pip install -r ../requirements.txt
python -m uvicorn app.main:app --reload
```

### Frontend Only

```bash
cd front/app
npm install
npm run dev
```

## License

MIT