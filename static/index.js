const table = document.getElementById("table");
const tableBase = table.innerHTML;
const socketio = io();

function clearTable() {
    table.innerHTML = tableBase;
}

function push() {
    socketio.send({
        name: document.getElementById("name").value,
        message: document.getElementById("message").value
    });
    
    document.getElementById("message").value = "";
}

function checkKey(e) {
    if (e.key === "Enter") {
        push();
    }
}

socketio.on('json', function(json) {
    let messages = json.messages;
    clearTable();
    
    messages.forEach(message => {
        let row = document.createElement("tr");
        let t = document.createElement("td");
        let n = document.createElement("td");
        let m = document.createElement("td");
        
        t.innerHTML = message[0];
        n.innerHTML = message[1];
        m.innerHTML = message[2];
        
        row.appendChild(t);
        row.appendChild(n);
        row.appendChild(m);
        table.appendChild(row);
    });
});