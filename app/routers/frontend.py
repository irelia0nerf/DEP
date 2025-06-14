from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/ui", response_class=HTMLResponse, tags=["FrontEnd"])
async def ui_page() -> str:
    """Serve a minimal HTML interface for score calculation."""
    return """
    <html>
      <head><title>FoundLab UI</title></head>
      <body>
        <h1>Score Wallet</h1>
        <form id='score-form'>
          Wallet: <input name='wallet_address'><br>
          Tx Volume: <input type='number' name='tx_volume'><br>
          Age Days: <input type='number' name='age_days'><br>
          <button type='submit'>Submit</button>
        </form>
        <pre id='result'></pre>
        <script>
        const form = document.getElementById('score-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const data = Object.fromEntries(new FormData(form));
            const resp = await fetch('/score/', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
            const json = await resp.json();
            document.getElementById('result').textContent =
                JSON.stringify(json, null, 2);
        });
        </script>
      </body>
    </html>
    """
