import os
from zipfile import ZipFile

base_dir = "HopeHub_Advanced"
os.makedirs(f"{base_dir}/css", exist_ok=True)
os.makedirs(f"{base_dir}/js", exist_ok=True)

pages = {
    "index.html": "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>Hope Hub - Home</title><link rel='stylesheet' href='css/styles.css'></head><body><div id='google_translate_element'></div><nav><a href='index.html'>Home</a><a href='resources.html'>Resources</a><a href='map.html'>Map</a><a href='emergency.html'>Emergency</a><a href='donate.html'>Donate</a><a href='volunteer.html'>Volunteer</a><a href='contact.html'>Contact</a><a href='admin.html'>Admin</a><a href='deck.html'>Pitch D...
    "contact.html": "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>Contact Us</title><link rel='stylesheet' href='css/styles.css'></head><body><nav><a href='index.html'>Home</a><a href='contact.html' class='active'>Contact</a></nav><main><h2>Contact Us</h2><form><input type='text' placeholder='Your Name' required><br><input type='email' placeholder='Your Email' required><br><textarea placeholder='Message'></textarea><br><button type='submit'>Send</button></form></main></body></html>",
    "admin.html": "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>Admin Login</title><link rel='stylesheet' href='css/styles.css'></head><body><main><h2>Admin Login</h2><form onsubmit='return login(event)'><input type='text' id='username' placeholder='Username' required><br><input type='password' id='password' placeholder='Password' required><br><button type='submit'>Login</button></form><p id='loginMsg'></p></main><script src='js/main.js'></script></body></html>",
    "deck.html": "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>Pitch Deck</title><link rel='stylesheet' href='css/styles.css'></head><body><nav><a href='index.html'>Home</a><a href='deck.html' class='active'>Pitch Deck</a></nav><main><h2>Our Vision</h2><iframe src='https://docs.google.com/presentation/d/e/2PACX-1vTEMPLATE/embed?start=false&loop=false' width='100%' height='480'></iframe></main></body></html>"
}

for name, content in pages.items():
    with open(f"{base_dir}/{name}", "w") as f:
        f.write(content)

with open(f"{base_dir}/css/styles.css", "w") as f:
    f.write("""body { font-family: Arial, sans-serif; background: #121212; color: white; margin: 0; padding: 0; }
nav { background: #1f1f1f; padding: 10px; display: flex; gap: 10px; }
nav a { color: white; text-decoration: none; }
main { padding: 20px; }
form input, form textarea { width: 100%; margin-bottom: 10px; padding: 10px; }
form button { padding: 10px 20px; }
""")

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
    f.write("""// Firebase Configuration (replace with your own project settings)
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project-id",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "XXXXXX",
  appId: "YOUR_APP_ID"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
""")

# Zip folder
zip_path = f"{base_dir}.zip"
with ZipFile(zip_path, "w") as zipf:
    for folder, _, files in os.walk(base_dir):
        for file in files:
            full_path = os.path.join(folder, file)
            arcname = os.path.relpath(full_path, base_dir)
            zipf.write(full_path, arcname)

print(f"✅ Project zipped as {zip_path}")
