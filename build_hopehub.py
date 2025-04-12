import os
from zipfile import ZipFile

# Create folders
os.makedirs("HopeHub/css", exist_ok=True)
os.makedirs("HopeHub/js", exist_ok=True)

# Basic HTML template for all pages
def make_page(title, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Hope Hub - {title}</title>
  <link rel="stylesheet" href="css/styles.css" />
</head>
<body>
  <div class="topbar">
    <div id="google_translate_element"></div>
    <button id="toggle-dark">🌓</button>
  </div>
  <nav>
    <a href="index.html">Home</a>
    <a href="resources.html">Resources</a>
    <a href="map.html">Map</a>
    <a href="emergency.html">Emergency</a>
    <a href="donate.html">Donate</a>
    <a href="volunteer.html">Volunteer</a>
    <a href="about.html">About</a>
  </nav>
  <main>{body}</main>
  <script src="js/main.js"></script>
</body>
</html>"""

# Pages
pages = {
    "index.html": make_page("Home", "<h1>Welcome to Hope Hub</h1><p>Your resource for help in Stockton.</p>"),
    "resources.html": make_page("Resources", "<h1>Resource List</h1><ul><li>Local Shelter</li><li>Food Bank</li></ul>"),
    "map.html": make_page("Map", "<h1>Interactive Resource Map Coming Soon</h1>"),
    "emergency.html": make_page("Emergency", "<h1>Emergency Help</h1><button>Call Now</button>"),
    "donate.html": make_page("Donate", "<h1>Donate</h1><p>Support our mission.</p>"),
    "volunteer.html": make_page("Volunteer", "<h1>Volunteer Form</h1><form><input placeholder='Name' /></form>"),
    "about.html": make_page("About", "<h1>About Hope Hub</h1><p>Helping Stockton’s unhoused community.</p>")
}

# Save HTML pages
for filename, content in pages.items():
    with open(f"HopeHub/{filename}", "w") as f:
        f.write(content)

# CSS
with open("HopeHub/css/styles.css", "w") as f:
    f.write("""
body { font-family: sans-serif; background: #121212; color: white; margin: 0; padding: 0; }
nav { background: #1f1f1f; padding: 10px; display: flex; gap: 15px; }
nav a { color: #fff; text-decoration: none; }
.topbar { display: flex; justify-content: space-between; padding: 10px; background: #000; }
main { padding: 20px; }
""")

# JavaScript for dark mode & translate
with open("HopeHub/js/main.js", "w") as f:
    f.write("""
document.getElementById('toggle-dark').addEventListener('click', () => {
  document.body.classList.toggle('dark');
});

function googleTranslateElementInit() {
  new google.translate.TranslateElement({
    pageLanguage: 'en',
    includedLanguages: 'en,es,fr,de,it,pt,tl,zh-CN,ja,ko'
  }, 'google_translate_element');
}
""")

# Zip it
with ZipFile("HopeHub_MultiPage.zip", "w") as zipf:
    for folder, _, files in os.walk("HopeHub"):
        for file in files:
            filepath = os.path.join(folder, file)
            zipf.write(filepath, arcname=os.path.relpath(filepath, "HopeHub"))
print("HopeHub_MultiPage.zip created successfully!")
