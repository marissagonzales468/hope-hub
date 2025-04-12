<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Hope Hub - Resources</title>
  <link rel="stylesheet" href="css/styles.css" />
  <!-- Firebase SDKs -->
  <script src="https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js"></script>
  <script src="https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js"></script>
</head>
<body>
  <nav>
    <a href="index.html">Home</a>
    <a href="resources.html" class="active">Resources</a>
    <a href="map.html">Map</a>
    <a href="donate.html">Donate</a>
    <a href="volunteer.html">Volunteer</a>
    <a href="contact.html">Contact</a>
    <a href="admin.html">Admin</a>
  </nav>

  <main>
    <h2>Available Community Resources</h2>
    <div id="resource-list">Loading...</div>
  </main>

  <script src="js/firebase.js"></script>
  <script>
    const resourceList = document.getElementById("resource-list");

    db.collection("resources").get().then(snapshot => {
      resourceList.innerHTML = ""; // Clear 'Loading...'
      if (snapshot.empty) {
        resourceList.innerHTML = "<p>No resources found. Check back later.</p>";
        return;
      }

      let list = document.createElement("ul");
      snapshot.forEach(doc => {
        const r = doc.data();
        const li = document.createElement("li");
        li.innerHTML = `
          <strong>${r.name}</strong><br>
          Type: ${r.type}<br>
          Address: ${r.address}<br>
          Phone: <a href="tel:${r.phone}">${r.phone}</a><br><br>
        `;
        list.appendChild(li);
      });
      resourceList.appendChild(list);
    }).catch(err => {
      resourceList.innerHTML = `<p style="color:red;">Error loading data: ${err.message}</p>`;
    });
  </script>
</body>
</html>
