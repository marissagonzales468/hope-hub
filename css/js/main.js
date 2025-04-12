firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

db.collection("resources").get().then(snapshot => {
  let list = document.createElement('ul');
  snapshot.forEach(doc => {
    let data = doc.data();
    let item = document.createElement('li');
    item.textContent = `${data.name} (${data.type}) - ${data.address}`;
    list.appendChild(item);
  });
  document.body.appendChild(list);
});
