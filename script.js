document.getElementById("toggle-dark").addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});

document.getElementById("data").innerText = "Estimated Homeless Population in Stockton: 1,200+ (Simulated)";

const resources = [
  { name: "Stockton Shelter for the Homeless", type: "Shelter", address: "611 W Church St", phone: "209-465-3612" },
  { name: "Gospel Center Rescue Mission", type: "Shelter", address: "445 S San Joaquin St", phone: "209-466-2138" },
  { name: "Emergency Food Bank Stockton", type: "Food", address: "7 W Scotts Ave", phone: "209-464-7369" },
  { name: "Sutter Health – Stockton", type: "Medical", address: "2545 W Hammer Ln", phone: "209-467-6333" },
  { name: "Catholic Charities", type: "Non-profit", address: "111 N San Joaquin St", phone: "209-444-5900" }
];

const container = document.getElementById("resource-list");
resources.forEach(resource => {
  const div = document.createElement("div");
  div.innerHTML = `<strong>${resource.name}</strong> <br/>${resource.type}<br/>${resource.address}<br/>📞 ${resource.phone}<hr/>`;
  container.appendChild(div);
});