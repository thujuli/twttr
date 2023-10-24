const refreshToken = function () {
  const xhr = new XMLHttpRequest();
  const url = "/api/auth/refresh";

  xhr.open("POST", url);
  xhr.setRequestHeader(
    "Authorization",
    `Bearer ${localStorage.getItem("refreshToken")}`
  );
  xhr.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 200) {
        const res = JSON.parse(this.response);
        localStorage.setItem("accessToken", res.data.access_token);
      } else {
        localStorage.removeItem("accessToken");
        localStorage.removeItem("refreshToken");
        window.location.href = "/login";
      }
    }
  };
  xhr.send();
};

// refreshing token every 30 minutes
const timeToRefresh = 30 * 60 * 1000;
setTimeout(refreshToken, timeToRefresh);

const getData = function () {
  const xhr = new XMLHttpRequest();
  const url = "/api/tweets";

  xhr.open("GET", url);
  xhr.setRequestHeader(
    "Authorization",
    `Bearer ${localStorage.getItem("accessToken")}`
  );
  xhr.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 200) {
        const tweets = JSON.parse(this.response);
        tweets["data"].forEach((tweet) => {
          const tweetSection = document.getElementById("section-tweets");
          const card = document.createElement("div");
          card.setAttribute("class", "card mt-3 mb-2");
          const cardHeader = document.createElement("div");
          cardHeader.setAttribute("class", "card-header");
          cardHeader.innerHTML = "Tweet from user " + tweet.user.username;
          const cardBody = document.createElement("div");
          cardBody.setAttribute("class", "card-body");
          const blockquote = document.createElement("blockquote");
          blockquote.setAttribute("class", "blockquote mb-2 mt-2");
          const p = document.createElement("p");
          p.innerHTML = tweet.content;
          const imgEl = document.createElement("img");
          const imgAnchor = document.createElement("a");
          imgAnchor.append(imgEl);
          imgAnchor.setAttribute("href", tweet.image_path);
          imgAnchor.setAttribute("download", tweet.image_path);
          if (tweet.image_name !== null) {
            imgEl.setAttribute("src", tweet.image_path);
            imgEl.setAttribute("class", "w-100");
          }
          blockquote.append(p, imgAnchor);
          cardBody.append(blockquote);
          card.append(cardHeader, cardBody);
          tweetSection.append(card);
        });
      } else {
        localStorage.removeItem("accessToken");
        localStorage.removeItem("refreshToken");
        window.location.href = "/login";
      }
    }
  };
  xhr.send();
};

// get access when have accessToken
window.addEventListener("load", function () {
  if (!localStorage.getItem("accessToken")) {
    window.location.replace("/login");
  } else {
    refreshToken();
    getData();
  }
});

// block refreshToken
const logout = document.getElementById("logout");
logout.addEventListener("click", function () {
  const xhr = new XMLHttpRequest();
  const url = "/api/auth/logout";

  xhr.open("DELETE", url);
  xhr.setRequestHeader(
    "Authorization",
    `Bearer ${localStorage.getItem("refreshToken")}`
  );
  xhr.send();
});

// block accessToken and redirect to login
logout.addEventListener("click", function () {
  const xhr = new XMLHttpRequest();
  const url = "/api/auth/logout";

  xhr.open("DELETE", url);
  xhr.setRequestHeader(
    "Authorization",
    `Bearer ${localStorage.getItem("accessToken")}`
  );
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4) {
      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
      window.location.href = "/login";
    }
  };
  xhr.send();
});

//POST NEW TWEET
const formTweet = document.getElementById("form-tweet");
formTweet.addEventListener("submit", function (e) {
  e.preventDefault();
  const xhr = new XMLHttpRequest();
  const url = "/api/tweets";

  //get data from form
  const content = document.getElementById("tweets").value;

  //validasi input
  if (content == "") return alert("Content tidak boleh kosong");

  let data = JSON.stringify({
    content: content,
  });

  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=utf-8");
  xhr.setRequestHeader(
    "Authorization",
    `Bearer ${localStorage.getItem("accessToken")}`
  );
  xhr.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 201) {
        let res = JSON.parse(this.response);
        formTweet.reset();
        divEl.setAttribute("class", "alert alert-success");
        divEl.setAttribute("role", "alert");
        divEl.innerHTML = res.message;
      } else {
        let res = JSON.parse(this.response);
        divEl.setAttribute("class", "alert alert-danger");
        divEl.setAttribute("role", "alert");
        divEl.innerHTML = res.message;
      }
    }
  };
  xhr.send(data);

  //give feedback
  const alertLoc = document.getElementById("tweet-alert");
  const divEl = document.createElement("div");
  alertLoc.appendChild(divEl);
});

//POST NEW TWEET MODAL
const modalFormTweet = document.getElementById("form-upload");
modalFormTweet.addEventListener("submit", function (e) {
  e.preventDefault();
  const xhr = new XMLHttpRequest();
  const url = "/api/tweets";

  // upload file
  const formData = new FormData();
  const content = document.getElementById("tweets-modal").value;
  const file = document.getElementById("file");
  if (content.length < 1) return alert("Content tidak boleh kosong");
  else {
    console.log(content, file.files[0]);
    formData.append("content", content);
    formData.append("file", file.files[0]);
  }

  xhr.open("POST", url);
  xhr.setRequestHeader(
    "Authorization",
    `Bearer ${localStorage.getItem("accessToken")}`
  );
  xhr.send(formData);
  xhr.onreadystatechange = function () {
    if (this.status == 201) {
      let res = JSON.parse(this.response);
      formTweet.reset();
      divEl.setAttribute("class", "alert alert-success");
      divEl.setAttribute("role", "alert");
      divEl.innerHTML = res.message;
    } else {
      let res = JSON.parse(this.response);
      divEl.setAttribute("class", "alert alert-danger");
      divEl.setAttribute("role", "alert");
      divEl.innerHTML = res.message;
    }
  };

  //give feedback
  const alertLoc = document.getElementById("tweet-alert");
  const divEl = document.createElement("div");
  alertLoc.appendChild(divEl);
});
