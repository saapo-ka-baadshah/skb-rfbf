# FastAPI Backend

## Structure

```
src/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/    # API endpoints
│   ├── schemas/             # Pydantic schemas
│   └── main.py             # FastAPI app
└── README.md
```

## Running

```bash
cd src
python -m uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /api/v1/status/` - Health check

## Development

The backend uses a modular structure:
- `app/api/v1/endpoints/` - Add new endpoints here
- `app/schemas/` - Add Pydantic models here