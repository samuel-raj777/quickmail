let email = "";

document.getElementById("generate").onclick = async () => {
  let res = await fetch("https://quickmail-api.onrender.com/generate");
  let data = await res.json();
  email = data.email;
  document.getElementById("email-display").innerText = email;
  fetchInbox();
};

document.getElementById("refresh").onclick = () => fetchInbox();

async function fetchInbox() {
  if (!email) return;
  let res = await fetch(`https://quickmail-api.onrender.com/inbox/${email}`);
  let data = await res.json();
  let inbox = document.getElementById("inbox");
  inbox.innerHTML = "";
  data.emails.forEach((msg) => {
    let div = document.createElement("div");
    div.innerHTML = `
      <strong>${msg.subject}</strong><br>
      From: ${msg.sender}<br>
      ${msg.preview}
    `;
    inbox.appendChild(div);
  });
}
