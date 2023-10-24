const formRegister = document.getElementById("form-register");
formRegister.addEventListener("submit", function (e) {
  e.preventDefault();

  const xhr = new XMLHttpRequest();
  const url = "/api/users";

  //get data from form
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const confirm_password = document.getElementById("confirm-password").value;
  const role = document.getElementById("role").value;

  //validasi input
  if (username == "") return alert("Username tidak boleh kosong");
  if (email == "") return alert("Email tidak boleh kosong");
  if (password == "") return alert("Password tidak boleh kosong");
  if (password != confirm_password)
    return alert("Password yang dimasukan tidak sama");
  if (role == "") return alert("Pilih role yang tersedia");

  const data = JSON.stringify({
    username: username,
    email: email,
    password: password,
    role: role,
  });

  xhr.open("POST", url);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(data);
  xhr.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 201) {
        formRegister.reset();
        let res = JSON.parse(this.response);
        div.innerHTML = res.message;
        div.setAttribute("class", "alert alert-success");
        div.setAttribute("role", "alert");
        formRegister.reset();
      } else {
        let res = JSON.parse(this.response);
        div.setAttribute("class", "alert alert-danger");
        div.innerHTML = res.message;
        div.setAttribute("role", "alert");
      }
    }
  };

  //give feedback
  const alertLoc = document.getElementById("alert-loc");
  const div = document.createElement("div");
  alertLoc.append(div);
});
