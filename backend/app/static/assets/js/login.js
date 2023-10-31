const formLogin = document.getElementById("form-login");
formLogin.addEventListener("submit", function(e) {
  e.preventDefault();

  const xhr = new XMLHttpRequest();
  const url = "/api/auth/login";

  //get data from form
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  //validasi input
  if (email.length < 1) return alert("Email tidak boleh kosong");
  if (password.length < 1) return alert("Password tidak boleh kosong");

  const data = JSON.stringify({
    email: email,
    password: password,
  });

  xhr.open("POST", url);
  xhr.setRequestHeader("Content-Type", "application/json;charset=utf-8");

  xhr.onreadystatechange = function() {
    if (this.readyState == 4) {
      if (this.status == 200) {
        formLogin.reset();
        let res = JSON.parse(this.response);

        //save to token to localStorage
        localStorage.setItem("accessToken", res.data.access_token);
        localStorage.setItem("refreshToken", res.data.refresh_token);
        window.location.href = "/admin";
      } else {
        let res = JSON.parse(this.response);
        div.setAttribute("class", "alert alert-danger");
        div.innerHTML = res.message;
        div.setAttribute("role", "alert");
      }
    }
  };
  xhr.send(data);

  const alertLoc = document.getElementById("alert-loc");
  const div = document.createElement("div");
  alertLoc.append(div);
});
