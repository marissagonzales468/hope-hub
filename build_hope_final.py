import os
from zipfile import ZipFile

base_dir = "HopeHub_Final"
os.makedirs(f"{base_dir}/css", exist_ok=True)
os.makedirs(f"{base_dir}/js", exist_ok=True)

html_files = {
    "resources.html": """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/><title>Hope Hub - Resources</title><link rel="stylesheet" href="css/styles.css"/><script src="https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js"></script><script src="https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js"></script></head><body><nav><a href="index.html">Home</a><a href="resources.html" class="active">Resources</a><a href="map.html">Map</a><a href="donate.html">Donate</a><a href="volunteer.html">Volunteer</a><a href="contact.html">Contact</a><a href="admin.html">Admin</a></nav><main><h2>Available Community Resources</h2><div id="resource-list">Loading...</div></main><script src="js/firebase.js"></script><script>const resourceList = document.getElementById("resource-list");db.collection("resources").get().then(snapshot => {resourceList.innerHTML = "";if (snapshot.empty) {resourceList.innerHTML = "<p>No resources found. Check back later.</p>";return;}let list = document.createElement("ul");snapshot.forEach(doc => {const r = doc.data();const li = document.createElement("li");li.innerHTML = `<strong>${r.name}</strong><br>Type: ${r.type}<br>Address: ${r.address}<br>Phone: <a href="tel:${r.phone}">${r.phone}</a><br><br>`;list.appendChild(li);});resourceList.appendChild(list);}).catch(err => {resourceList.innerHTML = `<p style="color:red;">Error loading data: ${err.message}</p>`;});</script></body></html>""",
    "index.html": "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Hope Hub - Home</title><link rel='stylesheet' href='css/styles.css'></head><body><nav><a href='index.html'>Home</a><a href='resources.html'>Resources</a><a href='map.html'>Map</a><a href='donate.html'>Donate</a><a href='volunteer.html'>Volunteer</a><a href='contact.html'>Contact</a><a href='admin.html'>Admin</a><a href='deck.html'>Pitch Deck</a></nav><main><h1>Welcome to Hope Hub</h1></main></body></html>",
    "contact.html": "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Contact</title><link rel='stylesheet' href='css/styles.css'></head><body><nav><a href='index.html'>Home</a><a href='contact.html' class='active'>Contact</a></nav><main><h2>Contact Us</h2><form><input type='text' placeholder='Your Name' required><br><input type='email' placeholder='Your Email' required><br><textarea placeholder='Message'></textarea><br><button type='submit'>Send</button></form></main></body></html>",
    "admin.html": "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Admin Login</title><link rel='stylesheet' href='css/styles.css'></head><body><main><h2>Admin Login</h2><form onsubmit='return login(event)'><input type='text' id='username' placeholder='Username' required><br><input type='password' id='password' placeholder='Password' required><br><button type='submit'>Login</button></form><p id='loginMsg'></p></main><script src='js/main.js'></script></body></html>",
    "deck.html": "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Pitch Deck</title><link rel='stylesheet' href='css/styles.css'></head><body><nav><a href='index.html'>Home</a><a href='deck.html' class='active'>Pitch Deck</a></nav><main><h2>Our Vision</h2><iframe src='https://docs.google.com/presentation/d/e/2PACX-1vTEMPLATE/embed?start=false&loop=false&delayms=3000' width='100%' height='480'></iframe></main></body></html>"
}

for name, content in html_files.items():
    with open(f"{base_dir}/{name}", "w") as f:
        f.write(content)

with open(f"{base_dir}/css/styles.css", "w") as f:
    f.write("""body { font-family: Arial, sans-serif; background: #121212; color: white; margin: 0; padding: 0; }
nav { background: #1f1f1f; padding: 10px; display: flex; gap: 10px; }
nav a { color: white; text-decoration: none; }
main { padding: 20px; }
form input, form textarea { width: 100%; margin-bottom: 10px; padding: 10px; }
form button { padding: 10px 20px; }""")

with open(f"{base_dir}/js/main.js", "w") as f:
    f.write("""function login(event) {
  event.preventDefault();
  const user = document.getElementById('username').value;
  const pass = document.getElementById('password').value;
  const msg = document.getElementById('loginMsg');
  if (user === 'admin' && pass === 'hope123') {
    msg.textContent = "✅ Login successful!";
    window.location.href = 'resources.html';
  } else {
    msg.textContent = "❌ Invalid credentials.";
  }
}""")

with open(f"{base_dir}/js/firebase.js", "w") as f:
    f.write("""const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project-id",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "XXXXXX",
  appId: "YOUR_APP_ID"
};
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();""")

zip_path = f"{base_dir}.zip"
with ZipFile(zip_path, "w") as zipf:
    for folder, _, files in os.walk(base_dir):
        for file in files:
            full_path = os.path.join(folder, file)
            arcname = os.path.relpath(full_path, base_dir)
            zipf.write(full_path, arcname)

print(f"✅ Zipped as {zip_path}")
