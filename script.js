// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAsKu5nNIM2QcYdS6DriGT7wFuVq3rbS18",
  authDomain: "marvelmirror-2b1de.firebaseapp.com",
  databaseURL: "https://marvelmirror-2b1de-default-rtdb.firebaseio.com",
  projectId: "marvelmirror-2b1de",
  storageBucket: "marvelmirror-2b1de.appspot.com",
  messagingSenderId: "82649048793",
  appId: "1:82649048793:web:d2c50cf03e15e313edc0c8",
  measurementId: "G-WFYBV90RGY",
};

firebase.initializeApp(firebaseConfig);

// Get a reference to the file storage service
const storage = firebase.storage();
// Get a reference to the database service
const database = firebase.database();

// Create camera database reference
const camRef = database.ref("file");
// Sync on any updates to the DB. THIS CODE RUNS EVERY TIME AN UPDATE OCCURS ON THE DB.

camRef.limitToLast(1).on("value", function (snapshot) {
  snapshot.forEach(function (childSnapshot) {
    const image = childSnapshot.val()["image"];
    const time = childSnapshot.val()["timestamp"];
    const storageRef = storage.ref(image);

    storageRef
      .getDownloadURL()
      .then(function (url) {
        console.log(url, "url");
        document.getElementById("photo").src = url;
        document.getElementById("time").innerText = time;
      })
      .catch(function (error) {
        console.log(error);
      });
  });
});

//Get gallery element ID

camRef.limitToLast(7).on("value", async function (snapshot) {
  await snapshot.forEach(function (childSnapshot) {
    const image = childSnapshot.val()["image"];
    const time = childSnapshot.val()["timestamp"];
    const storageRef = storage.ref(image);

    storageRef
      .getDownloadURL()
      .then(function (url) {
        //creating new Div
        var galleryDiv = document.getElementById("gallery_div");
        var img = document.createElement("img");
        img.src = url;
        // creating html cards for Photo gallery
        var Cards = document.createElement("div");
        Cards.innerHTML = `
     
      
      <div class="ui grid grid-center">
    
    
    <div class="ui main text container">
      <div class="ui card">
        <div class="image">
        <img src=${url}>
        </div>
        <div class="content">
          <a class="header">Marvel Mirror</a>
          <div class="meta">
            <span class="date">
              Last Photo taken at Mirror at ${time}: <br />
            </span>
          </div>
          <div>
            <span> Marvel Mirror....... </span>
          </div>
        </div>
      </div>
    </div>`;
        galleryDiv.appendChild(Cards);
      })
      .catch(function (error) {
        console.log(error);
      });
  });
});
