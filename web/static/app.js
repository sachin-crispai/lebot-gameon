const ws = new WebSocket(`ws://${location.host}/ws`);
const boardEl = document.getElementById("board");
const statusEl = document.getElementById("status");
const resetBtn = document.getElementById("reset-btn");

function renderBoard(board) {
    boardEl.innerHTML = "";
    board.forEach((cell, i) => {
        const btn = document.createElement("button");
        btn.className = "cell" + (cell ? ` ${cell}` : "");
        btn.textContent = cell || "";
        btn.onclick = () => ws.send(JSON.stringify({ type: "move", position: i }));
        boardEl.appendChild(btn);
    });
}

ws.onmessage = (e) => {
    const data = JSON.parse(e.data);
    if (data.board) renderBoard(data.board);
    if (data.message) statusEl.textContent = data.message;
};

ws.onopen = () => ws.send(JSON.stringify({ type: "reset" }));
resetBtn.onclick = () => ws.send(JSON.stringify({ type: "reset" }));