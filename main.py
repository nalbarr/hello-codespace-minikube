from fastapi import FastAPI, status
import uvicorn

app = FastAPI()


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
	return {"status": "UP"}

if __name__ == "__main__":
	uvicorn.run(app, port=8080, host="0.0.0.0")
