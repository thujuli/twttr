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
