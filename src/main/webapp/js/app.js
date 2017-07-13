function login() {

  const email = document.formulario.email.value;
  const password = document.formulario.password.value;
  const auth = firebase.auth()

  auth.signInWithEmailAndPassword(email, password)
  if(email != null){
        window.location.replace("http://localhost:8080/dashboard.html");    
  }
}

function signup() {
  firebase.auth().signOut()
  const email = document.formulario.email.value;
  const password = document.formulario.password.value;
  const auth = firebase.auth()

  auth.createUserWithEmailAndPassword(email, password)
  firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    user.sendEmailVerification()
    window.location.replace("http://localhost:8080/login.html");    

  }
});
}

function verify() {

var user = firebase.auth().currentUser;
var name, email, photoUrl, uid, emailVerified;

if (user != null) {
name = user.displayName;
email = user.email;
photoUrl = user.photoURL;
emailVerified = user.emailVerified;
uid = user.uid;
}
alert("E-mail: " + email + "\nNome: " + name);
};

function sair(){
    firebase.auth().signOut()
}
