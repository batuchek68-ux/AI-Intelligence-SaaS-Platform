async function load() {

  const res = await fetch("http://localhost:8000/run");
  const data = await res.json();

  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
}
