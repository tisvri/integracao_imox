import argparse
import uvicorn


def main():
    parser = argparse.ArgumentParser(description="Run REDCap DET Webhook")
    parser.add_argument("--host", default="0.0.0.0", help="Bind host (default: 0.0.0.0)")
    parser.add_argument("--port", default=8000, type=int, help= "Bind port (default: 8000)")
    parser.add_argument("--reload", action="store_true", help="Auto-reload on changes")
    args = parser.parse_args()

    uvicorn.run(
        "integracao.webhook:app",
        host=args.host,
        port=args.port,
        reload=args.reload
    )

if __name__ == "__main__":
    main()