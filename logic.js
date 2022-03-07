async function generateElementalBreakdown() {
  var word = document.getElementById("word").value;
  var elementalBreakdown = document.getElementById("elementalBreakdown");
  var output = "<p>No elemental breakdown found</p>";

  console.log("http://localhost:3000/" + word);
  var response = await fetch("http://localhost:3000/" + word, {
    method: "GET", // *GET, POST, PUT, DELETE, etc.
    mode: "cors", // no-cors, *cors, same-origin
    cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
    credentials: "same-origin", // include, *same-origin, omit
    headers: {
      "Content-Type": "application/json",
      "Content-Type": "application/x-www-form-urlencoded",
      "Access-Control-Allow-Credentials": "*",
    },
    redirect: "follow", // manual, *follow, error
    referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
  }).then((response) => {
    return response.json();
  });

  console.log(response);
  elementalBreakdown.innerHTML = response.json();
}
